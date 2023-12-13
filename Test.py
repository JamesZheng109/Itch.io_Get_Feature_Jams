import requests
from Featured_Jams import get_featured_jams
from datetime import datetime

def event_name_to_url(name):
    name_list=name.split()
    url='https://itch.io/jam/'
    for num,i in enumerate(name_list):
        url+=i.lower()
        if num!=len(name_list)-1:
            url+='-'
    return url
def validate_url(url):
    verified=0
    fail=0
    for link in url:
        response=requests.get(link)
        if response.status_code==200:
            print(f'{i}. {link}: Verified')
            verified+=1
        elif response.status_code!=200:
            print(f'{i}. {link} produced status code: {response.status_code}, not 200.')
            fail+=1
    print(f'Link(s) Verified for event: {verified}/{verified+fail}')

def validate_date(current_time,time,key):
    if current_time<time and key=='Start':
        print('Jam has not started yet')
    elif current_time<time and key=='Ends':
        print('Jam is happening')
    elif current_time==time and key=='Start':
        print('Jam Starts Today')
    elif current_time==time and key=='Ends':
        print('Jam Ends Today')
    elif current_time>time:
        print('Error: Date has passed')

print('Execute function and print outcome')
test=get_featured_jams()
print(test)
print('\n')
print('Validate Event')
for i in test:
    link=event_name_to_url(test[i]['Name'])
    print(f"{test[i]['Name']}")
    validate_url([link])
print('\n')
print('Validate Host URL')
for i in test:
    validate_url(test[i]['Link to Host(s)'])
print('\n')
print('Validate Date')
current_time=datetime.now().strftime('%Y/%m/%d')
print(f'Current Date: {current_time}')
for i in test:
    key=list(test[i].keys())[3]
    print(f"{i}. {test[i]['Name']}: {test[i][key]}")
    validate_date(current_time,test[i][key],key)