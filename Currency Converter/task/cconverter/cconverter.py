import json
import requests


def get_rate(currency_code):
    return json.loads(requests.get(f"http://www.floatrates.com/daily/{currency_code}.json").text)


rate_cache = dict()

requested_currency = input()
parsed = get_rate(requested_currency)
if requested_currency.upper() != "USD":
    rate_cache["USD"] = parsed["usd"]["rate"]

if requested_currency.upper() != "EUR":
    rate_cache["EUR"] = parsed["eur"]["rate"]


while True:
    exchange_currency = input()
    if len(exchange_currency) == 0:
        break

    amount_to_exchange = input()
    if len(amount_to_exchange) == 0:
        break

    amount_to_exchange = float(amount_to_exchange)
    rate_search = 0.0

    print("Checking the cache...")
    if exchange_currency.upper() not in rate_cache:
        print("Sorry, but it is not in the cache!")
        rate_search = get_rate(requested_currency)[exchange_currency.lower()]["rate"]
        rate_cache[exchange_currency.upper()] = rate_search
    else:
        print("Oh! It is in the cache!")
        rate_search = rate_cache[exchange_currency.upper()]

    print(f"You received {round(rate_search * float(amount_to_exchange),2)} {exchange_currency.upper()}.")


