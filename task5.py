import requests
class Converter:
    @staticmethod
    def get_exchange_rate():
        url = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
        response = requests.get(url)
        data = response.json()
        for item in data:
            if item['Ccy'] == 'USD':
                return float(item['Rate'])
        raise ValueError

    @staticmethod
    def usd_to_uzs(usd_amount):
        usd_to_uzs_rate = Converter.get_exchange_rate()
        return usd_amount * usd_to_uzs_rate

    @staticmethod
    def uzs_to_usd(uzs_amount):
        usd_to_uzs_rate = Converter.get_exchange_rate()
        return uzs_amount / usd_to_uzs_rate

usd_amount = 10000
uzs_amount = 100000000

try:
    print(f"{usd_amount} USD = {Converter.usd_to_uzs(usd_amount):.2f} UZS")
    print(f"{uzs_amount} UZS = {Converter.uzs_to_usd(uzs_amount):.2f} USD")
except ValueError as e:
    print(e)
