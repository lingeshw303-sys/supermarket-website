from flask import Flask, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Products
products = [
    {"id": 1, "name": "Apple", "price": 80, "image": "https://cdn-icons-png.flaticon.com/512/415/415733.png"},
    {"id": 2, "name": "Orange", "price": 50, "image": "https://cdn-icons-png.flaticon.com/512/415/415734.png"},
    {"id": 3, "name": "Watermelon", "price": 40, "image": "https://cdn-icons-png.flaticon.com/512/415/415731.png"},
    {"id": 4, "name": "Milk", "price": 60, "image": "https://cdn-icons-png.flaticon.com/512/415/415732.png"},
    {"id": 5, "name": "Burger", "price": 70, "image": "https://cdn-icons-png.flaticon.com/512/1046/1046784.png"},
    {"id": 6, "name": "Mango", "price": 45, "image": "https://cdn-icons-png.flaticon.com/512/415/415735.png"},
]

@app.route("/")
def home():
    return render_template("index.html", products=products)

@app.route("/add/<int:product_id>")
def add_to_cart(product_id):
    if "cart" not in session:
        session["cart"] = []
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        session["cart"].append(product)
        session.modified = True
    return redirect(url_for("cart"))

@app.route("/cart")
def cart():
    cart_items = session.get("cart", [])
    total = sum(item["price"] for item in cart_items)
    return render_template("cart.html", cart_items=cart_items, total=total)

@app.route("/checkout")
def checkout():
    total = sum(item["price"] for item in session.get("cart", []))
    session.pop("cart", None)  # clear cart after checkout
    return render_template("checkout.html", total=total)

if __name__ == "__main__":
    app.run(debug=True)
