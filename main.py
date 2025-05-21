import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

#Делаем проверку
if not API_KEY:
    print("Error: check your API-KEY")
    exit()
else:
    print("API-KEY successfully loaded")
    
#Запрос данных от пользователя для конвертации
base_currency = input("Write your base currency: ").upper()
target_currency = input("Write your target currency: ").upper()
amount = float(input("Write sum for conversion: "))


#Формируем URL 
url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base_currency}"

#Запрос к API
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
#Проверяем успешен ли ответ
    if data["result"] == "success":
        print("API-KEY WORK!")
        
        #Проверяем, есть ли нужная валюта в списке
        if target_currency in data["conversion_rates"]:
            rate = data["conversion_rates"][target_currency]
            converted_amount = amount * rate
            print(f"{amount}{base_currency} = {converted_amount:.2f} {target_currency}")
        else:
             print("Error! Currency not in base API") 
    else:
        print("Error! API not the request")
else:
    print(f"Error: API dont peply. Code status {response.status_code}")
    print(f"Message from server: {response.text}")
    

    
 
      