import requests
import pywhatkit
import keyboard
import time
from datetime import datetime
import pyautogui


API_KEY = 'Coloque sua chave de API' # Coloque sua chave de API válida do CoinMarketCap (o meu caso é CoinMarketCap)
base_url = 'https://pro-api.coinmarketcap.com/v1/'  # URL base da API da coinmarketcap
endpoint = 'cryptocurrency/listings/latest'  # Endpoint para obter a lista de criptomoedas
params = {
    'start': '1',
    'limit': '100',  # Limitar de 100 criptomoedas, você pode ajustar conforme necessário. Lembresse que sua coin precisa estar dentro desse range ou vc pode descartar esse parametro
    'convert': 'USD'
}
headers = {
    'Accepts': 'application/json',                    #Cabeçalhos da solicitação
    'X-CMC_PRO_API_KEY': API_KEY
}
response = requests.get(base_url + endpoint, params=params, headers=headers)    # Fazendo a solicitação GET através da lib requests
if response.status_code == 200:  # Veja se a solicitação foi bem-sucedida
    data = response.json()    
    contatos = ['+11998765432', '+11912345678', '+11976543210']   #escreva os numeros de seus contatos sempre com o prefixo +DDD9(numero_do_contato)
    message = ''  # Variável para acumular as informações    
    for cryptocurrency in data['data']:        # Processar e exibir os dados da resposta
        symbol = cryptocurrency['symbol']
        if symbol in ['CAKE', 'BTC', 'BNB']:     #nesse caso, optei por CAKE, BTC e BNB
            name = cryptocurrency['name']
            price_usd = cryptocurrency['quote']['USD']['price']     #famoso dóla
            print(f'{name} ({symbol}): USD {price_usd:.2f}')    #print do valor 
            message += f'{name} ({symbol}): USD {price_usd:.2f}\n'  # variavel para salvar todos os "print". No caso, os valores de cada moeda consultada na linha 41
    if message:
        for contato in contatos:      #Aqui ele vai consultar os contatos da linha 36 
            pywhatkit.sendwhatmsg(contato, message, datetime.now().hour, datetime.now().minute + 2)
            time.sleep(20)
            keyboard.press_and_release('ctrl + w')
else:
    print('Falha na solicitação. Código de status:', response.status_code)
