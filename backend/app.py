from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Load spreadsheet data
def load_data():
    df = pd.read_excel("construction_material_costs.csv")  # Replace with your file
    return df.to_dict(orient="material")  # Convert to list of dictionaries

@app.route('/data', methods=['GET'])
def get_data():
    data = load_data()
    return jsonify(data)

@app.route('/')
def login():
    return render_template("index.html")

@app.route('/home')
def home():
    return "This is home"


if __name__ == '__main__':
    app.run(debug=True)
