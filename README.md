# Itch.io_Get_Feature_Jams
Webscrapes info about the latest featured jams from [itch.io](https://itch.io). It provides the following information:
- Name of the jam
- Short description of the jam
- Link to the jam
- Links to the itch.io accounts of the host(s)
- Start (if it has not started yet) or end (if it already started) date of the jam
## Requirements
For [Featured_Jams.py](Featured_Jams.py):
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
- [requests](https://pypi.org/project/requests/)
- re(should be pre-installed)
- json (should be pre-installed)
  
For [Test.py](Test.py):
- [request](https://pypi.org/project/requests/)
- datetime(should be pre-installed)
- json (should be pre-installed)

Another option is the pip install:
```cmd
pip install -r /path/to/requirements.txt
```
## Installation
1. Download repository
2. Unzip Zip file
3. Move or copy/paste [Featured_Jams.py](Featured_Jams.py) to the desired project
4. Import Featured_Jams.py
   - If it is placed in the same directory as the file that is calling it:
     ```python
     from Freatured_Jams import get_featured_jams
     ```
   - If it is placed in a different directory than the file that is calling it:
     ```python
     from {insert_directory_path_here}.Freatured_Jams import get_featured_jams
     ```
## Usage
The imported method requireds no parameters so simply call put get_featured_jams(). It should be noted that the function returns the output so in order to see the output, do the following:
```python
variable=json.loads(get_featured_jams()) #Assuming one imported the entire json library
print(variable)
```
Assuming the internet connection is not failing, the function should produce dictionary object like so:
```python
{0:{'Name':'JAM NAME','Description':'Short description of jam','Link to Event':'https://itch.io/jams/{insert_jam_link_here}',
'Link to Host(s)':'https://itch.io/{insert_user_here}','Start/Ends':'yyyy/mm/dd'}}
```
## Test
In the repository is a file named [Test.py](Test.py). It should run as long as it is in the same directory as [Featured_Jams.py](Featured_Jams.py). The test includes:
1. 2 additional functions:
   - validate_url(url:list)
   - validate_date(current_time:str,time:str,key:str)
3. print the output of the get_featured_jams() function
4. Test if the url of jam works
5. Tests if the url of the users hosting the event works
6. Compares the provided date with the current date on the computer
