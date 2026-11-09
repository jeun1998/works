from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 로그인 화면을 보여주는 라우터
@app.route('/')
def index():
    return render_template('aa.html')

# 로그인 데이터를 처리하는 라우터 (GET 방식)
@app.route('/login', methods=['GET'])
def login():
    # GET 요청으로 전달된 query parameter 추출
    user_id = request.args.get('userid')
    passwd = request.args.get('passwd')
    
    # 서버 콘솔 창에 출력
    print(f"Server Log - 아이디: {user_id}, 비밀번호: {passwd}")
    
    # 조건 체크
    if user_id == "tom" and passwd == "111":
        return jsonify({"status": "success", "message": "로그인 성공"})
    else:
        return jsonify({"status": "fail", "message": "로그인 실패"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000);
