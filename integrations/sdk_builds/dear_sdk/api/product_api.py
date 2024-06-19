import requests


class ProductAPI:
    def __init__(self, config):
        self.config = config

    def find(self, id=None, name=None, sku=None, modified_since=None, include_deprecated=False,
             include_bom=False, include_suppliers=False, include_movements=False, include_attachments=False,
             include_reorder_levels=False, page=1, limit=100, auto_paginate=False):
        id = f'&ID={id}' if id else ''
        name = f'&Name={name}' if name else ''
        sku = f'&SKU={sku}' if sku else ''
        modified_since = f'&ModifiedSince={modified_since}' if modified_since else ''
        include_deprecated = f'&IncludeDeprecated={include_deprecated}' if include_deprecated else ''
        include_bom = f'&IncludeBOM={include_bom}' if include_bom else ''
        include_suppliers = f'&IncludeSuppliers={include_suppliers}' if include_suppliers else ''
        include_movements = f'&IncludeMovements={include_movements}' if include_movements else ''
        include_attachments = f'&IncludeAttachments={include_attachments}' if include_attachments else ''
        include_reorder_levels = f'&IncludeReorderLevels={include_reorder_levels}' if include_reorder_levels else ''
        page = f'?Page={page}'
        limit = f'&Limit={limit}'

        url_path = (f'/Product{page}{limit}{id}{name}{sku}{modified_since}{include_deprecated}{include_bom}'
                    f'{include_suppliers}{include_movements}{include_attachments}{include_reorder_levels}')

        url = self.config.get_url(url_path)
        headers = self.config.headers
        response = requests.get(url=url, headers=headers)

        return response

    def create(self, body):
        url_path = '/Product'
        url = self.config.get_url(url_path)
        headers = self.config.headers
        response = requests.post(url=url, headers=headers, data=body)

        return response

    def update(self, body):

        def _update(data):
            url_path = '/Product'
            url = self.config.get_url(url_path)
            headers = self.config.headers

            return requests.put(url=url, headers=headers, data=data)

        try:
            id = body['ID']
        except KeyError as e:
            id = None
            print(e)

        try:
            sku = body['SKU']
        except KeyError as e:
            sku = None
            print(e)

        if id:
            response = _update(body)

        elif sku:
            # TODO: Test if self.find(sku=sku) returns all products that contains the SKU or if it only returns
            #       an exact match.
            product = self.find(sku=sku).json()
            id = product['Products'][0]['ID']
            body['ID'] = id
            response = _update(body)

        else:
            print('To update a product, this endpoint requires the ID or SKU for the product you wish to update.')

        return response
