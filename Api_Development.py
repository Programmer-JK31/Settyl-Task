from flask import Flask, render_template, request
from Settyl_Task import predictFromInput

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_prediction', methods=['POST'])
def get_prediction():
    external_status = request.form['external_status']
    predicted_internal_status = predictFromInput(external_status)
    return predicted_internal_status

if __name__ == "__main__":
    app.run(debug=True)
