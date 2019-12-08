html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""


from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify())
# print("*"*50)
print(type(soup))                     # <class 'bs4.BeautifulSoup'>
print(soup.title)                     # <title>The Dormouse's story</title>
print(type(soup.title))               # <class 'bs4.element.Tag'>
print(soup.title.name)                # title
print(type(soup.title.name))          # <class 'str'>
print(soup.title.string)              # The Dormouse's story
print(type(soup.title.parent.name))   # <class 'str'>
print(soup.title.parent.name)         # head
print("*"*50)
print(soup.p)                         # <p class="title"><b>The Dormouse's story</b></p>
print(soup.p['class'])                # ['title']
print("*"*50)

print(soup.a)                         # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
print(soup.a['class'])                # ['sister']
print(soup.a['id'])                   # link1
print(soup.a['href'])                 # http://example.com/elsie
print("*"*50)
print(soup.find_all('a'))             # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
                                      #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
                                      #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a> ]
print(soup.find_all(id='link3'))      # [<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
print("*"*50)

for link in soup.find_all('a'):
    print(link)                       # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
    print(type(link))                 # <class 'bs4.element.Tag'>
    print(link.get('href'))           # http://example.com/tillie
print("*"*50)
print(soup.get_text())
print("*"*50)

soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
print(type(soup))  # <class 'bs4.BeautifulSoup'>
tag = soup.b
print(type(tag))   # <class 'bs4.element.Tag'>
print(tag)         # <b class="boldest">Extremely bold</b>
print(tag.get_text())  # Extremely bold
print(tag['class'])    # ['boldest']
print(soup.get_text())  # Extremely bold
print(tag.name)    # b
tag.name = "amit"
print(tag)         # <amit class="boldest">Extremely bold</amit>
print(tag.attrs)   # {'class': ['boldest']}
tag['id'] = 'verybold'
print(tag)         # <amit class="boldest" id="verybold">Extremely bold</amit>
del tag['id']
print(tag)         # <amit class="boldest">Extremely bold</amit>
print("*"*50)






soup = BeautifulSoup(html_doc, 'html5lib')
print(type(soup))
print(soup.name)    # [document]
print(soup.title)   # <title>The Dormouse's story</title>
print(soup.title.name)  # title
print(soup.title.string)  # The Dormouse's story
print(soup.title.attrs)  # {}
print("*********************************")
myTag = soup.p
print(myTag)        # <p class="title"><b>The Dormouse's story</b></p>
print(type(myTag))  # <class 'bs4.element.Tag'>
print(myTag.attrs)  # {'class': ['title']}
print(myTag['class'])  # ['title']
print(myTag.name)   # p


print("*********************************")

#  HTML 4 defines a few attributes that can have multiple values. HTML 5 removes a couple of them,
# but defines a few more. The most common multi-valued attribute is class (that is,
# a tag can have more than one CSS class). Others include rel, rev, accept-charset, headers, and accesskey.
# Beautiful Soup presents the value(s) of a multi-valued attribute as a list:

css_soup = BeautifulSoup('<p class="body"></p>')
print(css_soup.p['class'])    # ["body"]


css_soup = BeautifulSoup('<p class="body strikeout amitcss"></p>')
print(css_soup.p['class'])     # ["body", "strikeout", "amitcss"]

print("*********************************")

#  If an attribute looks like it has more than one value, but it’s not a multi-valued attribute as defined by any
# version of the HTML standard, Beautiful Soup will leave the attribute alone:

id_soup = BeautifulSoup('<p id="my id"></p>')
print(id_soup.p['id'])       # "my id"