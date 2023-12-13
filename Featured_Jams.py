#Imports
from bs4 import BeautifulSoup
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
    def Event_and_Description(info):
        #Get Event Name and Description
        for number,line in enumerate(info):
            jam_name=re.search("<a href=\"/jam/[a-zA-Z0-9_\s'-éñ]*\">",str(line)).group(0)[14:-2].replace('-',' ').upper()
            short_text=re.search(">[a-zA-Z0-9_\s'-éñ!\(\)\$]*</p>",str(line)).group(0)[1:-4]
            featured_jam[number]={'Name':jam_name,'Description':short_text}
    def Host_info(info):
        #Get Host Names
        for number,line in enumerate(info):
            host_names=re.findall("\"[a-zA-Z0-9_\s'-éñ]*\">",str(line))
            if len(host_names)==2:
                host_names[1]=host_names[1][1:-2]
            elif len(host_names)==3:
                host_names[1]=host_names[1][1:-2]
                host_names[2]=host_names[2][1:-2]
            featured_jam[number]['Link to Host(s)']=host_names[1:]
    def Date_info(info):
        #Get Start or End Date
        for number,line in enumerate(Duration):
            duration=re.findall('>[0-9a-z\s\-\:A-Z]*<',str(line))[:3]
            if duration[0]=='><':
                featured_jam[number]['Start']=duration[-1][1:-11].replace('-','/')
            elif duration[0]!='><':
                featured_jam[number]['Ends']=duration[-2][1:-11].replace('-','/')
    Event_and_Description(Event)
    Host_info(Host)
    Date_info(Duration)
    return featured_jam