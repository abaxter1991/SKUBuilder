from FaireSDK.configuration import Configuration
from FaireSDK.decorators import auto_instantiate
from FaireSDK.api.products_api import ProductsAPI


class Client:
    def __init__(self, api_access_token):
        self.api_access_token = api_access_token
        self.config = Configuration(self.api_access_token)

    @auto_instantiate
    def products(self):
        return ProductsAPI(self.config)
