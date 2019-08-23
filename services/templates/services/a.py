import requests

response = requests.get('http://artii.herokuapp.com/make?text=TAEWOO&FONT-ACROBATIC)
print(response.text)