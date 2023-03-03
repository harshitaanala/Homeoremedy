import pandas as pd
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
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

if __name__ == '__main__':
    app.run(debug=True)
