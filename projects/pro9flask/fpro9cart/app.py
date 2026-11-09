from flask import Flask, render_template, request, session, redirect, url_for
from datetime import timedelta

app = Flask(__name__);

app.secret_key = "abcd1234"
app.permanent_session_lifetime = timedelta(minutes=5)  # 세션 만료 시간 5분

products = [
    {"id":1,"name":"노트북","price":3500000},
    {"id":2,"name":"물티슈","price":3500},
    {"id":3,"name":"종이컵","price":350},
    {"id":4,"name":"볼펜","price":1500},
]

@app.route("/")
def product_list():
    return render_template("products.html", products=products)

@app.route("/cart")
def show_cart():
    cart = session.get("cart", {})
    total = sum(info["price"] * info["qty"] for info in cart.values())
    return render_template("cart.html", cart=cart, total=total)

@app.route("/add/<int:product_id>")
def add_to_cart(product_id):

    cart = session.get("cart", {})
    product = next((p for p in products if p["id"] == product_id), None)

    if product is None:
        return "주문 상품을 찾츨 수 없어요", 404

    item_name = product["name"]

    if item_name in cart:
        cart[item_name]["qty"] += 1  # 카트에 동일 상품이 있는 경우는 수량만 증가
    else:
        cart[item_name] = {"price":product["price"], "qty":1}

    session["cart"] = cart
    session.permanent = True

    return redirect(url_for("show_cart"))

@app.route("/remove/<item_name>")
def remove_to_cart(item_name):
    cart = session.get("cart")

    if item_name in cart:
        del cart[item_name]

    session["cart"] = cart
    return redirect(url_for("show_cart"))

@app.route("/clear")
def clear_cart():
    session.pop("cart", None)
    return redirect(url_for("show_cart"))




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000);