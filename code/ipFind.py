import requests
import webbrowser

ip = "5.173.176.9"  # Adres IP do sprawdzenia
response = requests.get(f"http://ipinfo.io/{ip}/json")
data = response.json()

# Pobranie współrzędnych geograficznych (szerokość, długość)
if 'loc' in data:
    lat, lon = data['loc'].split(',')
    map_url = f"https://www.google.com/maps/search/?api=1&query={lat},{lon}"
    
    print(f"Kraj: {data.get('country')}")
    print(f"Region: {data.get('region')}")
    print(f"Miasto: {data.get('city')}")
    print(f"Kod pocztowy: {data.get('postal')}")
    print(f"Dostawca internetu: {data.get('org')}")
    print(f"Współrzędne: {lat}, {lon}")
    print(f"Otwieranie mapy: {map_url}")
    
    # Otwórz mapę w przeglądarce
    webbrowser.open(map_url)
else:
    print("Nie udało się pobrać lokalizacji IP.")
