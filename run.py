import json
import os
import sys

import requests
from dotenv import load_dotenv

load_dotenv()

CALLBACK_URL = os.getenv('CALLBACK_URL')
API_KEY = os.getenv('API_KEY')

if not all([CALLBACK_URL, API_KEY]):
    print('Erro: Variáveis de ambiente CALLBACK_URL ou API_KEY não foram definidas')
    sys.exit(1)


def main():
    headers = {
        'apiKey': API_KEY,
        'Content-Type': 'application/json'
    }

    payload = json.dumps({
        'type': 'SYNC',
        'event': 'PENDING',
        'content': {
            'id': 999999,
            'oi': '999999.',
            'metadata': ''
        }
    })

    print(payload)

    try:
        r = requests.request('POST', CALLBACK_URL, headers=headers, data=payload)
        if r.status_code == 200:
            print(f'Requisição enviada com sucesso: {r}')
        else:
            print(f'Falha na requisição. Status code: {r.status_code}, Resposta: {r.text}')
    except requests.exceptions.RequestException as e:
        print(f'Erro na requisição: {e}')


if __name__ == '__main__':
    main()
