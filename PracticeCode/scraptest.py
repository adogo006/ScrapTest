from urllib.request import urlopen
from urllib.request import HTTPError
from urllib.request import URLError
import re

from bs4 import BeautifulSoup

def scraping():
    try:
        html = urlopen('http://www.pythonscraping.com/pages/error.html')
        #bs = BeautifulSoup(html.read(), 'html.parser')
    except HTTPError as e:
        print("The server returned HTTP error")
    except URLError as e:
        print("The server could not be found!")            
    else:
        print(html.read())
        #print(bs.h1)
        
def bsEH():
    try:
        html = urlopen('https://pythonscraping.com/pages/page1.html')
        bs = BeautifulSoup(html.read(), 'html.parser')
        badContent = bs.nonExistingTag.anotherTag
    except AttributeError as e:
        print("Tag was not found!")

    else:
        if badContent == None:
                print("Tag was not found!")
        else:
            print(badContent)

def getTitle(url):
    try: 
        html = urlopen(url)
    except HTTPError as e:
        #print("Server returned HTTP error!")
        return None
    except URLError as e:
        #print("Server was not found!")
        return None
    try:
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    
    return title    

def colorParser():
    html = urlopen('https://pythonscraping.com/pages/warandpeace.html')
    bs = BeautifulSoup(html.read(), 'html.parser')
    #find_all(tagName, tagAttributes) 
    nameList = bs.find_all('span', {'class': 'green'})
    for name in nameList:
        # get_text() 함수는 모든 태그를 제거하고 유니코드 텍스트 반환
        print(name.get_text())  

def childFind():
    html = urlopen('https://pythonscraping.com/pages/page3.html')
    bs = BeautifulSoup(html.read(),'html.parser')
    for child in bs.find('table', {'id': 'giftList'}).children:
        print(child)

def nextSib():
    html = urlopen('https://pythonscraping.com/pages/page3.html')
    bs = BeautifulSoup(html, 'html.parser')

    for sibling in bs.find('table' , {'id': 'giftList'}).tr.next_siblings:
        print(sibling)

def findParent():
    html = urlopen('https://pythonscraping.com/pages/page3.html')
    bs = BeautifulSoup(html, 'html.parser')
    print(bs.find('img', {'src': '../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())

def filteringImg():
    html = urlopen('https://pythonscraping.com/pages/page3.html')
    bs = BeautifulSoup(html, 'html.parser')
    images = bs.find_all('img', {'src': re.compile('../img/gifts/img.*.jpg')})
    for image in images:
        print(image['src'])
#re.compile('') 정규표현식을 사용하여 문자열을 필터링 할 수 있다.
#myTag.attrs['src'] 처럼 태그에서 속성이 가진 내용으로 접근할 수 있다.
#bs.find_all(lambda tag: len(tag.attrs) == 2) 을 사용하면 속성을 2개 가진 태그에 접근할 수 있다.   

def main():
    filteringImg()


if __name__ == "__main__":
    main()


