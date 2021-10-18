import requests

url = "http://localhost:3000/objects"

payload = """{"id": 5,"item": "The Fiancés","artist": "Pierre Auguste Renoir","collection": "Wallraf–Richartz Museum, Cologne, Germany","date": "1868"}"""
headers = {
  'content-type': 'application/json; charset=utf-8'
}


response = requests.request("POST", url, headers=headers, data = payload.encode("utf-8"))

print(response.text.encode('utf8'))