# BeautifulSoup 객체로 XML 문서 처리
from bs4 import BeautifulSoup

with open("pandas7.xml", mode="r", encoding="utf-8") as f:
    xmlfile = f.read()
    print(xmlfile, type(xmlfile))

soup = BeautifulSoup(xmlfile, 'lxml')
print(type(soup))

itemTag = soup.find_all("item")
print(itemTag[1])
print()
nameTag = soup.find_all("name")
print(nameTag[1])
print(nameTag[1]["id"])

print('-----------------------')
for i in itemTag:
    nametag = i.find_all("name")
    for j in nametag:
        print("id : " + j["id"] + " name : " + j.string)
        tel = i.find("tel")
        print("tel : " + tel.string)

    for j in i.find_all("exam"):
        print("kor : " + j["kor"] + ", eng:" + j["eng"])
    print()

print("\n\n서울시 제공 도서관 XML anstj 정보 읽기")
import urllib.request as req
import pandas as pd
url = "http://openapi.seoul.go.kr:8088/sample/xml/SeoulLibraryTimeInfo/1/5/"
plainText = req.urlopen(url).read()
# print(plainText)
xm10bj = BeautifulSoup(plainText, 'lxml-xml')
libData = xm10bj.select("row")
rows = []
for data in libData:
    name = data.find("LBRRY_NAME").string
    addr = data.find("ADRES").string
    print("도서관명: " + name)
    print("주소: " + addr)
    print()
    rows.append({"도서관명":name, "주소":addr})

df = pd.DataFrame(rows)
print(df)
print("건수 : ", len(df))
