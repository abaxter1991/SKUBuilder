from .configuration import Configuration
from .decorators import auto_instantiate
from .api.product_api import ProductAPI
from .api.product_family_api import ProductFamilyAPI
from .api.sale_api import SaleAPI


class Client:
    def __init__(self, account_id, api_key):
        self.account_id = account_id
        self.api_key = api_key
        self.config = Configuration(self.account_id, self.api_key)

    @auto_instantiate
    def product(self):
        return ProductAPI(self.config)

    @auto_instantiate
    def product_family(self):
        return ProductFamilyAPI(self.config)

    @auto_instantiate
    def sale(self):
        return SaleAPI(self.config)
