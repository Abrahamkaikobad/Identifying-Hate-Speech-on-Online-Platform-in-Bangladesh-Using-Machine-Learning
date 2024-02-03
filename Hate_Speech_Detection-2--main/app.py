from flask import Flask, render_template, request, jsonify
from src.main import Prediction

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

@app.route('/predict', methods=["POST"])
def predict():
    prediction_obj = Prediction()

    # Get the user input from the form
    user_input_bangla = request.form['text_bangla']
    user_input_banglish = request.form['text_banglish']

    # Call the get_prediction method
    result = prediction_obj.get_prediction(user_input_bangla, user_input_banglish)

    # Render the result page with the prediction result
    return render_template('result.html', prediction_result=result)

@app.route('/result')
def result():
    # You can include additional logic here if needed
    return render_template('result.html')

if __name__ == "__main__":
    app.run(debug=True)
