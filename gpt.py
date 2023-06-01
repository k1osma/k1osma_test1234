import openai
from prompt_toolkit import prompt
import configparser

# Создайте объект ConfigParser и загрузите конфигурацию из файла
config = configparser.ConfigParser()
config.read('config.ini')

# Получите значение ключа из конфигурации
openai_key = config.get('API', 'openai_key')

openai.api_key = openai_key

print('''                                             
$$ |      $$$$ |                                             
$$ |  $$\ \_$$ |  $$$$$$\   $$$$$$$\ $$$$$$\$$$$\   $$$$$$\  
$$ | $$  |  $$ | $$  __$$\ $$  _____|$$  _$$  _$$\  \____$$\ 
$$$$$$  /   $$ | $$ /  $$ |\$$$$$$\  $$ / $$ / $$ | $$$$$$$ |
$$  _$$<    $$ | $$ |  $$ | \____$$\ $$ | $$ | $$ |$$  __$$ |
$$ | \$$\ $$$$$$\\$$$$$$  |$$$$$$$  |$$ | $$ | $$ |\$$$$$$$ |
\__|  \__|\______|\______/ \_______/ \__| \__| \__| \_______|

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
