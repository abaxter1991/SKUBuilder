import requests


class ProductFamilyAPI:
    def __init__(self, config):
        self.config = config

    def find(self, id=None, name=None, sku=None, modified_since=None, page=1, limit=100, auto_paginate=False):
        id = f'&ID={id}' if id else ''
        name = f'&Name={name}' if name else ''
        sku = f'&SKU={sku}' if sku else ''
        modified_since = f'&ModifiedSince={modified_since}' if modified_since else ''
        page = f'?Page={page}'
        limit = f'&Limit={limit}'

        url_path = f'/ProductFamily{page}{limit}{id}{name}{sku}{modified_since}'

        url = self.config.get_url(url_path)
        headers = self.config.headers
        response = requests.get(url=url, headers=headers)

        return response

    def create(self, body):
        url_path = '/ProductFamily'
        url = self.config.get_url(url_path)
        headers = self.config.headers
        response = requests.post(url=url, headers=headers, data=body)

        return response

    def update(self):
        pass


product_family = {
    'Products': [
        {
            'ID': 'ce9a6504-4207-4001-b430-749bf11fdc4f',
            'SKU': 'GB1-White',
            'Name': 'Golf balls - white single',
            'Option1': '3',
            'Option2': '4',
            'Option3': '5'
        }
    ],
    'SKU': 'Test',
    'Name': 'Test',
    'Category': 'Other',
    'DefaultLocation': 'Main Warehouse',
    'Brand': None,
    'CostingMethod': 'FIFO',
    'UOM': 'Item',
    'MinimumBeforeReorder': 0,
    'ReorderQuantity': 0,
    'PriceTier1': 0,
    'PriceTier2': 0,
    'PriceTier3': 0,
    'PriceTier4': 0,
    'PriceTier5': 0,
    'PriceTier6': 0,
    'PriceTier7': 0,
    'PriceTier8': 0,
    'PriceTier9': 0,
    'PriceTier10': 0,
    'ShortDescription': '',
    'Description': '',
    'AttributeSet': None,
    'DiscountRule': None,
    'Tags': '',
    'COGSAccount': None,
    'RevenueAccount': None,
    'InventoryAccount': None,
    'PurchaseTaxRule': None,
    'SaleTaxRule': None,
    'DropShipMode': 'No Drop Ship',
    'Option1Name': 'Test 1',
    'Option2Name': '',
    'Option3Name': '',
}
