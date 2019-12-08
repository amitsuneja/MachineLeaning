import requests
from bs4 import BeautifulSoup
import csv


# Collect first page of artists’ list
page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')
print(page.text)

print("*"*50)

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')
print(soup.text)

# Remove bottom links
last_links = soup.find(class_='AlphaNav')
last_links.decompose()

# Create a file to write to, add headers row
myFile = csv.writer(open('z-artist-names.csv', 'w'))
myFile.writerow(['Name', 'Link'])

print("*"*50)

# Pull all text from the BodyText div
artist_name_list = soup.find(class_='BodyText')
print(artist_name_list)

print("*"*50)
print("*"*50)
print("*"*50)

# Pull text from all instances of <a> tag within BodyText div
artist_name_list_items = artist_name_list.find_all('a')
print(artist_name_list_items)
print("*"*50)
print("*"*50)
print("*"*50)
# Create for loop to print out all artists' names
for artist_name in artist_name_list_items:
    print(artist_name.prettify())

print("*"*50)
print("*"*50)
print("*"*50)
# Use .contents to pull out the <a> tag’s children
for artist_name in artist_name_list_items:
    names = artist_name.contents[0]
    print(names)
print("*"*50)
print("*"*50)
print("*"*50)
for artist_name in artist_name_list_items:
    names = artist_name.contents[0]
    links = 'https://web.archive.org' + artist_name.get('href')
    print(names)
    print(links)

for artist_name in artist_name_list_items:
    names = artist_name.contents[0]
    links = 'https://web.archive.org' + artist_name.get('href')
    # Add each artist’s name and associated link to a row
    myFile.writerow([names, links])