from flask import Flask, render_template
app = Flask(__name__);


@app.route("/")
def index():
    return render_template("index.html");

@app.route("/loop")
def loop():
    users = ["전재현","강동엽","이정인"]
    return render_template("loop.html", users=users);

@app.route("/condition")
def condition():
    score = 75;
    return render_template("condition.html", score=score);

@app.route("/filter")
def filter():
    message = "hello false jinja2";
    price = 12345;
    return render_template("filter.html", message=message, price=price);

@app.template_filter('format')
def format_number(value):
    return format(value, ",") # 숫자 세자리 마다, 출력

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000);