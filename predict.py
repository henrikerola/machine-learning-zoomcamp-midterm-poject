from flask import Flask, jsonify, request
import pickle
import pandas as pd

with open('model.bin','rb') as f_in:
    dv,model=pickle.load(f_in)

app = Flask(__name__)


@app.route('/', methods=['POST'])
def endpoint():
    input_data = request.json

    input_df = pd.DataFrame([input_data])
    input_dict = input_df.to_dict(orient='records')
    input_vector = dv.transform(input_dict)

    result = {'prediction': bool(model.predict(input_vector)[0])}
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)