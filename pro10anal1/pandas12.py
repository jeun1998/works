# json 자료 처리 : xml에 비해 경량이므로 빠른 처리 가능. 배열 개념만 있으면 됨

import json
dict = {"name":"tom","age":23,"score":["90","80","70"]}
print(dict, type(dict))

print("json 인코딩 : dict -> str로 변환")
str_val = json.dumps(dict)
# str_val = json.dumps(dict, indent=4)  # 보기 좋게 들여쓰기
print(str_val, type(str_val))
print(str_val[0:20])

print("\n\njson 디코딩 : str -> dict로 변환")
json_val = json.loads(str_val)
print(json_val, type(json_val))
print(json_val["name"])

print()
for k in json_val.keys():
    print(k)
print()
for v in json_val.values():
    print(v)

print("\n\n서울시 제공 도서관 json 샘플 문서 정보 읽기")
import urllib.request as req
import pandas as pd
url = "http://openapi.seoul.go.kr:8088/sample/json/SeoulLibraryTimeInfo/1/5/"
plainText = req.urlopen(url).read().decode("utf-8")

jsonData = json.loads(plainText)
print(type(jsonData))
print(jsonData["SeoulLibraryTimeInfo"].get("row"))

print('-----------------------------------------')

libData = jsonData.get("SeoulLibraryTimeInfo").get("row")
# print(libData)
name = libData[0].get("LBRRY_NAME")
print(name)

print()
datas = []
for ele in libData:
    name = ele.get("LBRRY_NAME")
    tel = ele.get("TEL_NO")
    addr = ele.get("ADRES")
    print(name, " ", tel, " ", addr)
    datas.append([name, tel, addr])

df = pd.DataFrame(datas, columns=["도서관명", "전화", "주소"])
print(df)