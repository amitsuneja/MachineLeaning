from bs4 import BeautifulSoup
import requests

myUrl = "https://www.consumerreports.org/cro/a-to-z-index/products/index.htm"
myWebPage = requests.get(myUrl)
mySoup = BeautifulSoup(myWebPage.text, 'html.parser')


bottomLinkList = mySoup.find_all(id = "global-footer")
for element in bottomLinkList:
    element.decompose()

myTopSideList = mySoup.find_all(class_="crux-body-copy crux-body-copy--small products-a-z__categories__label")
for element in myTopSideList:
    element.decompose()

myTopBoldElementList = mySoup.find_all(class_="crux-body-copy crux-body-copy--bold products-a-z__categories__legend")
for element in myTopBoldElementList:
    element.decompose()

myListOfProduucts = mySoup.find_all(class_ = "crux-body-copy")
for product in myListOfProduucts:

    print(product.text.strip() + "," + product.a['href'])