import sys
sys.stdout.reconfigure(encoding='utf-8')  # 한글 깨짐 방지


v1 = '자료1'
v2 = '두번째 자료'




print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>메인</title>
</head>
<body>
    <h1>홈 페이지: http://127.0.0.1:9999 라고 해도 서비스 됨</h1>
    <a href="cgi-bin/hello.py">hello</a>
    <a href="cgi-bin/world.py">world</a>
    <a href="cgi-bin/my.py?name=tom&age=23">my(get 방식)</a>
    <a href="friend.html">friend</a>
    <a href="cgi-bin/sangpum.py">상품 자료(MariaDB)</a>
</body>
    <b>world 페이지</b>
    <br>
    자료 출력 : {0}, {1}
    <br/>
    <img src="../images/image.jpeg"
    <a href="../index.html">메인으로</a>
</html>
""".format(v1, v2))