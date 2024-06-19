import requests


class ProductsAPI:
    def __init__(self, config):
        self.config = config

    def get_all_products(self):
        url_path = '/products'
        url = self.config.get_url(url_path)
        headers = self.config.headers
        response = requests.get(url=url, headers=headers)

        return response

    def get_a_product_by_id(self, id):
        url_path = f'/products/{id}'
        url = self.config.get_url(url_path)
        headers = self.config.headers
        response = requests.get(url=url, headers=headers)

        return response

    def create_product(self, body):
        url_path = '/products'
        url = self.config.get_url(url_path)
        headers = self.config.headers
        response = requests.post(url=url, headers=headers, data=body)

        return response

    def update_a_product(self, id, body):
        url_path = f'/products/{id}'
        url = self.config.get_url(url_path)
        headers = self.config.headers
        response = requests.patch(url=url, headers=headers, data=body)

        return response

    def delete_a_product(self, id):
        url_path = f'/products/{id}'
        url = self.config.get_url(url_path)
        headers = self.config.headers
        response = requests.delete(url=url, headers=headers)

        return response

    def update_products_variation_option_sets(self, id, body):
        url_path = f'/products/{id}/variant-option-sets'
        url = self.config.get_url(url_path)
        headers = self.config.headers
        response = requests.patch(url=url, headers=headers, data=body)

        return response

    def get_all_taxonomy_types(self):
        url_path = '/products/types'
        url = self.config.get_url(url_path)
        headers = self.config.headers
        response = requests.get(url=url, headers=headers)

        return response
