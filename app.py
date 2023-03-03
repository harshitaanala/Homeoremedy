import datetime
import pandas as pd
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app, support_credentials=True)
medicines_df = pd.read_csv("Datasets/homeo.csv")

def suggest_medicines(symptoms):
    matching_medicines = medicines_df[medicines_df['English'].apply(lambda x: all([symptom in x.split(", ") for symptom in symptoms]))]
    matching_medicines['English'] = matching_medicines['English'].apply(lambda x: len(set(symptoms) & set(x.split(", "))))
    matching_medicines = matching_medicines.sort_values(by='English', ascending=False)
    return matching_medicines.head(5)['Remedy_1'].tolist() if not matching_medicines.empty else []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_message/<symptoms>', methods=['GET', 'POST'])
def send_message(symptoms):
    symptoms = symptoms.upper().split(", ")
    medicines = suggest_medicines(symptoms)
    message = "Based on your symptoms, I suggest the following medicines: " + ", ".join(medicines)
    res = jsonify({'response': message})
    res.headers.add('Access-Control-Allow-Origin', '*')
    return res

@app.route('/generate_report', methods=['POST'])
def generate_report():
    name = request.form['name']
    age = request.form['age']
    gender = request.form['gender']
    symptoms = request.form['symptoms']
    days = request.form['days']

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report_html = open('report.html', 'w')
    report_title = 'Medical Report of - {}'.format(name)
    report_html.write('<html><head><title>{}</title></head><body>'.format(report_title))
    report_html.write('<h1>{}</h1>'.format(report_title))
    report_html.write('<p><strong>Report Generated on:</strong> {}</p>'.format(current_time))
    report_html.write('<p><strong>Name:</strong> {}</p>'.format(name))
    report_html.write('<p><strong>Age:</strong> {}</p>'.format(age))
    report_html.write('<p><strong>Gender:</strong> {}</p>'.format(gender))
    report_html.write('<p><strong>Symptoms:</strong> {}</p>'.format(symptoms))
    report_html.write('<p><strong>Number of Days you have been facing the issue:</strong> {}</p>'.format(days))
    report_html.write('</body></html>')
    report_html.close()

    return 'Report generated successfully'


if __name__ == '__main__':
    app.run(debug=True)
