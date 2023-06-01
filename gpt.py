import openai
from prompt_toolkit import prompt
import requests

# Отправьте GET-запрос на сервер, чтобы получить API-ключ
response = requests.get("https://192.168.31.121:5000/api_key", verify=False)
api_key = response.text

# Используйте полученный API-ключ в вашем коде
openai.api_key = api_key

# Продолжайте работать с OpenAI API, используя ключ


print(''' 
  /$$$$$$  /$$                   /$$      /$$$$$$  /$$$$$$$  /$$$$$$$$
 /$$__  $$| $$                  | $$     /$$__  $$| $$__  $$|__  $$__/
| $$  \__/| $$$$$$$   /$$$$$$  /$$$$$$  | $$  \__/| $$  \ $$   | $$   
| $$      | $$__  $$ |____  $$|_  $$_/  | $$ /$$$$| $$$$$$$/   | $$   
| $$      | $$  \ $$  /$$$$$$$  | $$    | $$|_  $$| $$____/    | $$   
| $$    $$| $$  | $$ /$$__  $$  | $$ /$$| $$  \ $$| $$         | $$   
|  $$$$$$/| $$  | $$|  $$$$$$$  |  $$$$/|  $$$$$$/| $$         | $$   
 \______/ |__/  |__/ \_______/   \___/   \______/ |__/         |__/   
                                                                      
                                                                      
                                                                      
''')
def chat_with_gpt(messages):
    response = openai.ChatCompletion.create(
        #model="gpt-3.5-turbo",
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response.choices[0].message['content']

messages = [
    {"role": "system", "content": "Вы: привет"},
    {"role": "system", "content": "ChatGPT: Привет, чем я могу помочь?"}
]

while True:
    user_input = prompt("Вы: ")

    if user_input.lower() == 'exit':
        break

    messages.append({"role": "user", "content": user_input})
    response = chat_with_gpt(messages)
    messages.append({"role": "system", "content": response})
    print("ChatGPT:", response)
