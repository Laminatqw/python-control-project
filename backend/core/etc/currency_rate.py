import requests

from apps.currency.models import CurrencyRate


def get_currency_rates():
    response = requests.get("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5")
    data = response.json()

    rates = {}
    for entry in data:
        if entry['ccy'] in ['USD', 'EUR']:
            rates[entry['ccy']] = float(entry['sale'])

    rates['UAH'] = 1
    return rates

def update_currency_rates():
    rates = get_currency_rates()
    for currency, rate in rates.items():
        CurrencyRate.objects.update_or_create(currency=currency, defaults={'rate_to_uah': rate})