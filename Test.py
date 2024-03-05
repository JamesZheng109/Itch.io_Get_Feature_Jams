import requests
from Featured_Jams import get_featured_jams
from datetime import datetime
from json import loads

def validate_url(url):
    verified=0
    for link in url:
        response=requests.get(link)
        if response.status_code==200:
            print(f'{i}. {link}: Verified')
            verified+=1
        elif response.status_code!=200:
            print(f'{i}. {link} produced status code: {response.status_code}, not 200.')
    print(f'Link(s) Verified for event: {verified}/{len(url)}')

def validate_date(current_time,time,key):
    if current_time<time and key=='Start':
        print('Jam has not started yet')
    elif current_time<time and key=='Ends':
        print('Jam is currently running')
    elif current_time==time and key=='Start':
        print('Jam Starts Today')
    elif current_time==time and key=='Ends':
        print('Jam Ends Today')
    elif current_time>time:
        print('Error: Date has passed')

print('Execute function and print outcome')
test=loads(get_featured_jams())
print(test)
print('\n')
print('Validate Event')
for i in test:
    validate_url([test[i]['Link to event']])
print('\n')
print('Validate Host URL')
for i in test:
    validate_url(test[i]['Link to Host(s)'])
print('\n')
print('Validate Date')
current_time=datetime.now().strftime('%Y/%m/%d')
print(f'Current Date: {current_time}')
for i in test:
    key=list(test[i].keys())[4]
    print(f"{i}. {test[i]['Name']}: {test[i][key]}")
    validate_date(current_time,test[i][key],key)
