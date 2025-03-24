from flask import Flask, render_template, request, jsonify
import pandas as pd
from src.predictor import predict_cost_price
import os

app = Flask(_name_)

# ✅ Load dataset for state & crop options
df = pd.read_excel(os.path.join("data", "cleaned_dataset.xlsx"))
states = df["state"].unique().tolist()
crops = df["crop"].unique().tolist()

@app.route("/")
def index():
    return render_template("index.html", states=states, crops=crops)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        state = request.form["state"]
        crop = request.form["crop"]

        cost, price = predict_cost_price(state, crop)

        return jsonify({
            "estimated_cost": cost,
            "expected_earnings": price
        })
    except Exception as e:
        return jsonify({"error": str(e)})

if _name_ == "_main_":
    app.run(debug=True)