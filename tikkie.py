from time import time
import jwt
import requests

with open('private_rsa.pem', 'r') as file:
    private_key = file.read()

with open('key-secret', 'r') as file:
    key = file.readline()
    secret = file.readline()
    key, secret = key[:-1], secret[:-1]

url = "https://api-sandbox.abnamro.com/v1/oauth/token"

exp = int(time() + 15 * 60)
nbf = int(time())
iss = "Wouter Kayser (ETV)"
aud = "https://auth-sandbox.abnamro.com/oauth/token"
payload = {"exp": exp, "nbf": nbf, "iss": iss, "sub": key, "aud": aud}
headers = {"API-Key": key}
signature = jwt.encode(payload, private_key, algorithm="RS256")

p = requests.post(url, data=payload, headers=headers)
print(p.text)
