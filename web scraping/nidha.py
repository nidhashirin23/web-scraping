# create a folder in file and under that create a file 

# install
# extension :python

# 1st method :
# in terminal : pip3 install beautifulsoup4
# version : pip3 show beautifulsoup

# to get all datas


import requests
from bs4 import BeautifulSoup

# beauty = requests.get("https://www.w3schools.com/")
# store = BeautifulSoup(beauty.content,"html.parser")  #The "html.parser" is simply telling BeautifulSoup to use Python's built-in tool to read and understand the HTML content.
# print(store.prettify())     #The prettify() method adds line breaks and indentation, making the document easier to read and understand.


# TO GET TEXT
# print(store.get_text())


# TO GET DIV DATA

var_req = requests.get("https://www.w3schools.com/")
all_data = var_req.text
soup = BeautifulSoup(all_data, 'html.parser')

# Print out a portion of the HTML to check the structure
print(soup.prettify())

data1 = soup.find_all("div", {'class': "w3-col l6 w3-center"})
print(f"Found {len(data1)} elements.")
for element in data1:
    print(element)





# TO GET THE HEADING OF DIV
# for item in data1:
#     nested_div = item.find('div') #try to find the nested 'div' in each 'div'
#     h2_element = nested_div.find('h5') if nested_div else None

#     if h2_element:
#         print(h2_element.text)









