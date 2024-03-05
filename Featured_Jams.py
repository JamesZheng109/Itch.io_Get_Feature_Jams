#Imports
from bs4 import BeautifulSoup
from json import dump,dumps
import requests,re

def get_featured_jams():
    #Get info
    response=requests.get('https://itch.io/jams')
    soup=BeautifulSoup(response.text,'html.parser')
    Event=soup.select('div.primary_info')
    Host=soup.select('div.hosted_by.meta_row')
    Duration=soup.select('div.timestmap')
    #Create Dictionary
    featured_jam={}
    #Helper functions
    def Event_and_Description(info):
        #Get Event Name and Description
        for number,line in enumerate(info):
            jam_name=re.search("<a href=\"/jam/[a-zA-Z0-9_\s'-éñ]*\">",str(line)).group(0)
            short_text=re.search('''<p class="short_text" dir="auto">[\w\W]*</p>''',str(line)).group(0)[33:-4]
            featured_jam[number]={'Name':jam_name[14:-2].replace('-',' ').upper(),'Description':short_text,
                                  'Link to event':'https://itch.io'+jam_name[9:-2]}
    def Host_info(info):
        #Get Host Names
        urls=[]
        for number,line in enumerate(info):
            host_names=re.findall("\"[a-zA-Z0-9_\s'-éñ]*\">",str(line))
            #remove index 0 because it is not a url
            host_names.pop(0)
            for item in host_names:
                #Check if itch.io is a host
                if item.replace('>','')[1:-1]=='/':
                    urls.append('https://itch.io')
                else:
                    urls.append(item.replace('>','')[1:-1])
            featured_jam[number]['Link to Host(s)']=urls
            urls=[]
    def Date_info(info):
        #Get Start or End Date
        for number,line in enumerate(Duration):
            duration=re.findall('>[0-9a-z\s\-\:A-Z]*<',str(line))[:3]
            if duration[0]=='><':
                featured_jam[number]['Start']=duration[-1][1:-11].replace('-','/')
            elif duration[0]!='><':
                featured_jam[number]['Ends']=duration[-2][1:-11].replace('-','/')
    #Call helper functions
    Event_and_Description(Event)
    Host_info(Host)
    Date_info(Duration)
    #Dumps dictionary to .json
    with open('Game_Jam.json','w') as file:
        dump(featured_jam,file,indent=6)
    #return json object
    return dumps(featured_jam)
