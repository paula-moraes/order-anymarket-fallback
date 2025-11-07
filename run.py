import json
import os
import sys

import requests
from dotenv import load_dotenv

load_dotenv()

CALLBACK_URL = os.getenv('CALLBACK_URL')
API_KEY = os.getenv('API_KEY')
GUMGA_TOKEN = os.getenv('GUMGA_TOKEN')

if not all([CALLBACK_URL, API_KEY, GUMGA_TOKEN]):
    print('Erro: Variáveis de ambiente CALLBACK_URL, API_KEY ou GUMGA_TOKEN não foram definidas')
    sys.exit(1)


def main():
    headers = {
        'apiKey': API_KEY,
        'Content-Type': 'application/json',
        'gumgaToken': GUMGA_TOKEN
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
        requests.request('POST', CALLBACK_URL, headers=headers, data=payload)
        print('Requisição enviada com sucesso')
    except requests.exceptions.RequestException as e:
        print(f'Erro na requisição: {e}')


if __name__ == '__main__':
    main()
