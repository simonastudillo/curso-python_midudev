# Como hacer peticiones a APIs con Python
# con y sin dependencias

# 1. Sin dependencias
import urllib.request
import json

api_posts = "https://jsonplaceholder.typicode.com/posts"
try:
  response = urllib.request.urlopen(api_posts)
  data = response.read();
  json_data = json.loads(data.decode('utf-8'))
  print(json_data)
  response.close();
except urllib.error.URLError as e:
  print(f"Error al hacer la petición: {e} ")

# 2. Con dependencias
# pip install requests
import requests

print("\nGET");
api_posts = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(api_posts)
print(response.json())
json = response.json()
print(json[0])

# 3. POST

print("\nPOST");
api_posts = "https://jsonplaceholder.typicode.com/posts"
data = {"title": "foo", "body": "bar", "userId": 1}
response = requests.post(api_posts, json=data)
print(response.json())
print(response.status_code)

# 4. PUT

print("\nPOST");
api_posts = "https://jsonplaceholder.typicode.com/posts/1"
data = {"title": "foo", "body": "bar", "userId": 1}
response = requests.put(api_posts, json=data)
print(response.json())
print(response.status_code)

# Usar la API de gpt-4 con OpenAI
api = "https://api.openai.com/v1/chat/completions"
key = "SK-XXXXXXXXX"
headers = {
  "Content-Type": "application/json",
  "Authorization" : f"Bearer {key}"
}
data = {
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "user",
      "content": "What is the meaning of life?"
    }
  ]  
}

response = requests.post(api, json=data, headers=headers)
print(response.json())
# Usar la API de gpt-4 con OpenAI
api = "https://api.deepseek.com/v1/chat/completions"
key = "SK-XXXXXXXXX"
headers = {
  "Content-Type": "application/json",
  "Authorization" : f"Bearer {key}"
}
data = {
  "model": "deepseek-chat",
  "messages": [
    {
      "role": "user",
      "content": "What is the meaning of life?"
    }
  ]  
}

response = requests.post(api, json=data, headers=headers)
print(response.json())