import requests
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="Previsão_Agora")

print("Seja bem vindo a previsão do tempo")
localizacao = input("Insira seu endereço (EX: Rua do Tubarão 80, Tibau - RN ):")

location = geolocator.geocode(localizacao)
if location:
    print("Endereço localizado:", location.address)
    print("Coordenadas:", (location.latitude, location.longitude))
else:
    print("Localização não encontrada. Verifique se o endereço está correto!")
    exit()

api_key = "54a12b195967f8987756cfa52ee1e3c6"
url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "lat": location.latitude,
    "lon": location.longitude,
    "lang": "pt_br",
    "units": "metric",
    "appid": api_key
}

response = requests.get(url,params=params)
print(response.json())
if response.status_code == 200:
    data = response.json()
    print("\nPrevisão do tempo atual:")
    print(f"Temperatura atual: {data['main']['temp']}°C")
    print(f"Descrição: {data['weather'][0]['description'].capitalize()}")
    print(f"Umidade: {data['main']['humidity']}%")
    print(f"Vento: {data['wind']['speed']} m/s")
else:
    print("Erro ao acessar a API. Verifique sua chave ou conexão com a internet.")