from flask import Flask, render_template, request
import requests
from config import APİ_KEY

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    ilk_doviz = request.form['ilk_doviz'].upper()
    cevrilen_doviz = request.form['cevrilen_doviz'].upper()
    miktar = float(request.form['miktar'])

    # API'den veri çekiliyor.
    url = f"http://data.fixer.io/api/latest?access_key={APİ_KEY}"
    yanit = requests.get(url)
    data = yanit.json()

    rates = data.get("rates", {})
    oran = rates.get(ilk_doviz, 1)
    miktar_in_EUR = miktar / oran
    miktar = miktar_in_EUR * rates.get(cevrilen_doviz, 1)
    miktar = round(miktar, 5)

    return render_template('index.html', miktar=miktar, cevrilen_doviz=cevrilen_doviz)
@app.route('/about')
def about():
     return render_template('about.html')
@app.route('/nolist')
def nolist():
     return render_template('nolist.html')
if __name__ == '__main__':
    app.run(debug=True)
