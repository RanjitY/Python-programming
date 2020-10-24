from bs4 import BeautifulSoup
import requests

url="https://getpython.wordpress.com/"

source=requests.get(url)

soup=BeautifulSoup(source.text,'html')

title=soup.find('title') # place your html tagg in parentheses that you want to find from html.
print("this is with html tags :",title)

qwery=soup.find('h1') # here i find first h1 tagg in my website using find operation.

print("this is without html tags:",qwery.text) 


links=soup.find('a') #i extarcted link using "a" tag
print(links)

print(links['href']) 

print(links['class'])

many_link=soup.find_all('a') # here i extracted all the anchor tags of my website
total_links=len(many_link) # len function is use to calculate length of your array
print("total links in my website :",total_links)
print()
for i in many_link[:6]: # here i use slicing to fetch only first 6 links from rest of them.
    print(i)

second_link=many_link[1] #here i fetch second link which place on 1 index number in many_links.
print(second_link)
print()
print("href is :",second_link['href']) #only href link is extracted from ancor tag

nested_div=second_link.find('div')

print(nested_div)
print()

z=(nested_div['class'])
print(z)
print(type(z))
print()

print("class name of div is :"," ".join(nested_div['class'])) 

wiki=requests.get("https://en.wikipedia.org/wiki/World_War_II")
soup=BeautifulSoup(wiki.text,'html')
print(soup.find('title'))


ww2_contents=soup.find_all("div",class_='toc')
for i in ww2_contents:
    print(i.text)


overview=soup.find_all('table',class_='infobox vevent')
for z in overview:
    print(z.text)
