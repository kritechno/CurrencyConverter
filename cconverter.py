import requests

our_money = str(input()).lower()

r = requests.get(f"http://www.floatrates.com/daily/{our_money}.json")
data = r.json()
if our_money == 'usd':
    cache = {'eur': data['eur']['rate']}
elif our_money == 'eur':
    cache = {'usd': data['usd']['rate']}
else:
    cache = {
        'usd': data['usd']['rate'],
        'eur': data['eur']['rate']
    }
while True:
    wanted = str(input()).lower()
    if not wanted:
        break
    amount = float(input())
    print("Checking the cache...")
    if wanted in cache:
        print("Oh! It is in the cache!")
    else:
        cache[f'{wanted}'] = data[wanted]['rate']
        print("Sorry, but it is not in the cache!")
    print(f"You received {round(amount * data[wanted]['rate'], 2)} {wanted.upper()}.")

