import requests
from requests.auth import HTTPBasicAuth

ORDERS_API = 'https://sandbox.moip.com.br/v2/orders'

HEADERS = {'Content-Type': 'application/json'}


class MopiSDK(object):

    def __init__(self, token, key):
        self.auth = HTTPBasicAuth(token, key)

    def criar_pedido(self, own_id, product, quantity, price, customer_id):
        payload = self.payload(own_id, product, quantity, price, customer_id)

        print('=' * 100)
        print(payload)
        print('=' * 100)

        response = requests.post(ORDERS_API, json=payload, auth=self.auth, headers=HEADERS)
        print(response.status_code)
        print(response.text)

    def payload(self, own_id, product, quantity, price, customer_id):
        return {
            'ownId': own_id,
            'amount': {
                'currency': 'BRL',
                'subtotals': {
                    'shipping': 0,
                }
            },
            'items': [{
                'product': product,
                'quantity': quantity,
                'price': price
            }],
            'customer': {
                'ownId': 'cliente_xyz ',
                'fullname': 'João Silva',
                'email': 'joaosilva@email.com'
            }
        }
