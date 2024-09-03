from flask import Flask, render_template, request, jsonify
import requests
from config import API_KEY
import currencyapicom
import argparse

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    ilk_doviz = request.form['ilk_doviz'].upper()
    cevrilen_doviz = request.form['cevrilen_doviz'].upper()
    miktar = float(request.form['miktar'])
    url = f"http://data.fixer.io/api/latest?access_key={API_KEY}"
    yanit = requests.get(url)
    data = yanit.json()
    rates = data.get("rates", {})
    oran = rates.get(ilk_doviz, 1)
    miktar_in_EUR = miktar / oran
    miktar = miktar_in_EUR * rates.get(cevrilen_doviz, 1)
    miktar = round(miktar, 5)

    return render_template('index.html', miktar=miktar, cevrilen_doviz=cevrilen_doviz)
@app.route('/convert', methods=['GET'])
def convert_currency():
    ilk_doviz = request.args.get('ilk')
    cevrilen_doviz = request.args.get('son')
    miktar = request.args.get('miktar', '1')
    try:
        miktar = float(miktar)
    except ValueError:
        return jsonify({'error': 'Geçersiz miktar'}), 400

    response = requests.get(f'http://data.fixer.io/api/latest?access_key={API_KEY}')
    data = response.json()
    rates = data.get('rates', {})
    if ilk_doviz not in rates or cevrilen_doviz not in rates:
        return jsonify({'Hata': 'Geçersiz döviz birimi'}), 400

    from_rate = rates[ilk_doviz]
    to_rate = rates[cevrilen_doviz]
    sonuc = (miktar / from_rate) * to_rate

    return jsonify({
        'Ana para birimi': ilk_doviz,
        'Cevrilen para birimi': cevrilen_doviz,
        'Miktar': miktar,
        'Sonuc': sonuc
    })

@app.route('/about')
def about():
     return render_template('about.html')
@app.route('/nolist')
def nolist():
     return render_template('nolist.html')
if __name__ == '__main__':
    app.run(debug=True)
