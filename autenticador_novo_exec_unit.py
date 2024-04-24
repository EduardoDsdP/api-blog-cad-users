from requests.auth import HTTPBasicAuth
import requests

resultado = requests.get('http://localhost:8000/login',auth=('Eduardo', '123456'))

print(resultado.json())