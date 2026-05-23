from flask import Flask, render_template, request
import pickle
import json
import numpy as np

app = Flask(__name__)

# Load model
with open('house_price_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load columns
with open('columns.json', 'r') as f:
    data_columns = json.load(f)['data_columns']

# Location list
locations = data_columns[3:]


def predict_price(location, total_sqft, bath, bhk):

    loc_index = -1

    if location.lower() in data_columns:
        loc_index = data_columns.index(location.lower())

    x = np.zeros(len(data_columns))

    x[0] = total_sqft
    x[1] = bath
    x[2] = bhk

    if loc_index >= 0:
        x[loc_index] = 1

    return round(model.predict([x])[0],2)


@app.route('/')
def home():
    return render_template(
        'index.html',
        locations=locations
    )


@app.route('/predict', methods=['POST'])
def predict():

    location = request.form['location']
    sqft = float(request.form['sqft'])
    bath = float(request.form['bath'])
    bhk = int(request.form['bhk'])

    prediction = predict_price(
        location,
        sqft,
        bath,
        bhk
    )

    return render_template(
        'index.html',
        prediction_text=f"Estimated Price: ₹ {prediction} Lakhs",
        locations=locations
    )


if __name__=="__main__":
    app.run()