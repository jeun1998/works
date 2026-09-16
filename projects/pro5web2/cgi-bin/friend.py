# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

import os
import urllib.parse

# get / post 요청 구분
method = os.environ.get("REQUEST_METHOD", "GET")

if method == "POST":
    length = int(os.environ.get("CONTENT_LENGTH", 0))
    body = sys.stdin.read(length)
else:
    body = os.environ.get("QUERY_STRING", "")

params = urllib.parse.parse_qs(body)

irum = params.get("name", [""])[0]
junhwa = params.get("phone", [""])[0]
gen = params.get("get", [""])[0]

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>my</title>
</head>
<body>
    <b>my 페이지</b>
    <br/>
    일반 사용자가 전송한 값 : 이름은{0}, 전화는{1} 성별은{2}
    <br/>
    <a href="../index.html">메인으로</a>
</body>
</html>
""".format(irum, junhwa, gen))