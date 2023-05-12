from flask import Flask, render_template, request
import numpy as np
import pickle
import os
from email.message import EmailMessage 
import ssl
import smtplib

app = Flask(__name__, template_folder='templates')
model = pickle.load(open('model.pkl', 'rb'))

email_sender = "prasath201907@gmail.com"
email_pass = "zbnspzgnkigryqjv"
email_recv = "ywaran152@gmail.com"
subject = "Chronic kidney disease prediction System"
body = """ Kidney specialist hospitals \n Bhairav Kidney Hospital : https://bmct.in/ \n Ponni hospital : http://www.ponnihospitalpalladam.com/ \n Revathi medical center : https://www.revathimedicalcenter.com/ \n  """


@app.route('/', methods=['GET', 'POST'])
def Home():
    return render_template('home.html')
    
    
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        age = float(request.form['age'])
        bp = float(request.form['bp'])
        sg = float(request.form['sg'])
        al = float(request.form['al'])
        su = float(request.form['sg'])
        rbc = float(request.form['rbc'])
        pc = float(request.form['pc'])
        pcc = float(request.form['pcc'])
        ba = float(request.form['ba']) 
        bgr = float(request.form['bgr'])
        bu = float(request.form['bu'])
        sc = float(request.form['sc'])
        sod = float(request.form['sod'])
        pot = float(request.form['pot'])
        hemo = float(request.form['hemo'])
        pcv = float(request.form['pcv'])
        wc = float(request.form['wc'])
        rc = float(request.form['rc'])
        htn = float(request.form['htn'])
        dm = float(request.form['dm'])
        ca = float(request.form['ca'])
        appet = float(request.form['appet'])
        pe = float(request.form['pe'])
        ane = float(request.form['ane'])

        values = np.array([[age, bp, sg, al, su, rbc, pc, pcc, ba, bgr, bu, sc, sod, pot, hemo, pcv, wc, rc, htn, dm, ca, appet, pe, ane]])

    prediction = model.predict(values)

    return render_template('result.html', prediction=prediction)

@app.route("/send", methods=['POST'])
def send():
    if request.method == 'POST':
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_recv
        em['Subject'] = subject
        em.set_content(body)
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_pass)
            smtp.sendmail(email_sender, email_recv, em.as_string())
        value = True
    return render_template('result.html', value=value)


if __name__ == "__main__":
    app.run(debug=True)


