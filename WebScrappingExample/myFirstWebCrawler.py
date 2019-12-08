from bs4 import BeautifulSoup
import requests

myPythonQBank = {}
myUrl = "http://codingbat.com/java"
myWebPage = requests.get(myUrl)
mySoup = BeautifulSoup(myWebPage.text, 'html.parser')
mainPageitems = mySoup.find_all(class_="summ")

for topic in mainPageitems:
    myPythonQBank[topic.a.text] = {}

for key in myPythonQBank.keys():
    myJavaURL = myUrl + "/" + key
    myJavaWebPage = requests.get(myJavaURL)
    myJavaSoup = BeautifulSoup(myJavaWebPage.text, 'html.parser')
    table = myJavaSoup.find(width="200").find_parent("table")
    #  print(table)
    for row in table.find_all("tr")[1:]:
        for cell in row.find_all("td"):
            # print(cell.get_text(strip=True))
            # print(cell.a["href"])
            myPythonQBank[key][cell.a["href"]] = {}


for mainkey in myPythonQBank.keys():
    # print("**************************************************************************************")
    # print(mainkey)
    for minorkey in myPythonQBank[mainkey].keys():
        # print(minorkey)
        mysubJavaURL = "http://codingbat.com" + minorkey
        # print(mysubJavaURL)
        mysubJavaPage = requests.get(mysubJavaURL)
        mysubJavaSoup = BeautifulSoup(mysubJavaPage.text, 'html.parser')
        mytag = mysubJavaSoup.find(class_="max2")
        myPythonQBank[mainkey][minorkey] = mytag.text

print(myPythonQBank)