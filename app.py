from flask import Flask, render_template, request
from forex_python.converter import CurrencyRates

app = Flask(__name__)
c = CurrencyRates()

# Список поддерживаемых валют
supported_currencies = ['USD', 'EUR', 'GBP', 'JPY', 'CAD']

@app.route('/')
def index():
    return render_template('index.html', currencies=supported_currencies)

@app.route('/convert', methods=['POST'])
def convert():
    from_currency = request.form['from_currency']
    to_currency = request.form['to_currency']
    amount = float(request.form['amount'])

    # Конвертируем валюту
    converted_amount = c.convert(from_currency, to_currency, amount)

    return f'{amount} {from_currency} равно {converted_amount:.2f} {to_currency}'

if __name__ == '__main__':
    app.run(debug=True)
