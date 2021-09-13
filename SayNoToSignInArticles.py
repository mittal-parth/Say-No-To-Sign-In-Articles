# Dependencies
import docx
import re
import requests
from bs4 import BeautifulSoup

# Create a new word doc
mydoc = docx.Document()

def getInfo(URL, filepath):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Find article tag
    post = soup.find('article')

    # Text in article tag
    data = post.text
    
    # Add the text to word file and save
    mydoc.add_paragraph(data)
    mydoc.save(filepath)

# Driver Code
URL = input("Please enter the URL \n")
filepath = input("\nPlease enter the destination file path \n(Make sure to remove the quotation marks at the beginning and end)\n")
try:
    print("\nGetting page....")
    getInfo(URL, filepath)
except Exception as e:
    print(f"Got exception as {e}")
    exit()

print("Done! \nCheck your file in " + filepath)
