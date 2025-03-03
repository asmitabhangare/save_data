from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/save_data', methods=['POST'])
def save_data():
    data = request.get_json()
    with open("sample.json", "w") as outfile:
        json.dump(data, outfile)
    return jsonify({"message": "Data saved successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)


# 402-5145907-7651545B00CGM89I0