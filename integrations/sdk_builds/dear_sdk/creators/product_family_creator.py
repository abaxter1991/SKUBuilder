from .. import constants


class ProductFamilyCreator:
    def __init__(self, product_type, design_portfolio, design_version,
                 colors, sizes, retail_price, wholesale_price, custom_price):
        self.product_type = product_type
        self.design_portfolio = design_portfolio
        self.design_version = design_version
        self.colors = colors
        self.sizes = sizes
        self.retail_price = retail_price
        self.wholesale_price = wholesale_price
        self.custom_price = custom_price

    def build(self):
        return {
            'Products': self._product_variants(),
            'SKU': self._product_family_sku(),
            'Name': self._product_family_name(),
            'Category': self.product_type,
            'DefaultLocation': 'Main Warehouse',
            'Brand': 'Stryder',
            'CostingMethod': 'FIFO',
            'UOM': 'Item',
            'MinimumBeforeReorder': 0,
            'ReorderQuantity': 0,
            'PriceTier1': self.retail_price,
            'PriceTier2': self.wholesale_price,
            'PriceTier3': self.custom_price,
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
            'COGSAccount': '_35_: Cost of Goods Sold',
            'RevenueAccount': '_1_: Sales',
            'InventoryAccount': '_36_: Inventory Asset',
            'PurchaseTaxRule': 'No Tax',
            'SaleTaxRule': 'No Tax',
            'DropShipMode': 'No Drop Ship',
            'Option1Name': 'Color',
            'Option2Name': 'Size',
            'Option3Name': ''
        }

    def _product_variants(self):
        product_variants = []

        for color in self.colors:
            for size in self.sizes:
                product_variants.append([
                    {
                        # 'ID': '',
                        'SKU': self._product_sku(color, size),
                        'Name': self._product_name(color, size),
                        'Option1': '3',
                        'Option2': '4',
                        'Option3': '5'
                    }
                ])

        return product_variants

    def _product_family_sku(self):
        pass

    def _product_family_name(self):
        pass

    def _product_sku(self, color, size):
        pass

    def _product_name(self, color, size):
        pass
