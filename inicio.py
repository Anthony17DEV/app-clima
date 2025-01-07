import requests
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="Previsão_Agora")

print("Seja bem vindo a previsão do tempo")
localizacao = input("Insira seu endereço (ex:Rua do Tubarão 80, Tibau - RN ):")

location = geolocator.geocode(localizacao)
if location:
    print("Endereço localizado:", location.address)
    print("Coordenadas:", (location.latitude, location.longitude))
else:
    print("Localização não encontrada. Verifique se o endereço está correto!")
    exit()

api_key = "54a12b195967f8987756cfa52ee1e3c6"
url= f"https://api.openweathermap.org/data/2.5/onecall"
params = {
    "lat": location.latitude,
    "lon": location.longitude,
    "lang": "pt_br",
    "units": "metric",
    "appid": api_key
}

response = requests.get(url,params=params)
if response.status_code == 200:
    data = response.json()
    clima_atual = data["current"]
    print("\nPrevisão do tempo atual:")
    print(f"Temperatura atual: {clima_atual["temp"]}°C")
    print(f"Descrição: {clima_atual['weather'][0]['description'].capitalize()}")
    print(f"Umidade: {clima_atual['humidity']}%")
    print(f"Vento: {clima_atual['wind_speed']} m/s")
else:
    print("Erro ao acessar a API. Verifique sua chave ou conexão com a internet.")