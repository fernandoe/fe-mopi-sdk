import os
from unittest import TestCase

from fe_mopi_sdk.client import MopiSDK
import uuid

FE_MOIP_API_TOKEN = os.environ.get('FE_MOIP_API_TOKEN', 'AFNN7P387XXPVSLV8Q1OXSSQH1LK1A76')
FE_MOIP_API_KEY = os.environ.get('FE_MOIP_API_KEY', 'BGBI32WLXG1FM8AQE3TAPYFLBXRHSXYRWCCBOQHL')


class TestMopiSDK(TestCase):

    def test_contructor(self):
        sdk = MopiSDK(FE_MOIP_API_TOKEN, FE_MOIP_API_KEY)
        assert sdk is not None

    def test_criar_pedido(self):
        sdk = MopiSDK(FE_MOIP_API_TOKEN, FE_MOIP_API_KEY)

        own_id = str(uuid.uuid4())
        product = 'Nome do Peoduto'
        quantity = 1
        price = 20000
        customer_id = str(uuid.uuid4())

        sdk.criar_pedido(
            own_id,
            product,
            quantity,
            price,
            customer_id
        )
