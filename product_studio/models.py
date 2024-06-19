from django.db import models

from .managers import ColorManager, ProductManager


class Color(models.Model):
    color = models.CharField(max_length=50)
    sku = models.CharField(max_length=10)

    objects = ColorManager()

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'

    def __str__(self):
        return self.color

    def get_name(self):
        return f'{self.color}'

    def get_sku(self):
        return f'{self.sku}'


class Size(models.Model):
    size = models.CharField(max_length=50)
    sku = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Size'
        verbose_name_plural = 'Sizes'

    def __str__(self):
        return f'{self.size}'

    def get_name(self):
        return f'{self.size}'

    def get_sku(self):
        return f'{self.sku}'


class ProductType(models.Model):
    product_type = models.CharField(max_length=50)
    sku = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Product Type'
        verbose_name_plural = 'Product Types'

    def __str__(self):
        return f'{self.product_type}'

    def get_name(self):
        return f'{self.product_type}'

    def get_sku(self):
        return f'{self.sku}'


class ProductPart(models.Model):
    product_part = models.CharField(max_length=50)
    sku = models.CharField(max_length=10)
    product_type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True, blank=True)
    colors = models.ManyToManyField(Color)
    sizes = models.ManyToManyField(Size)

    class Meta:
        verbose_name = 'Product Part'
        verbose_name_plural = 'Product Parts'

    def __str__(self):
        return f'{self.product_part}'

    def get_name(self):
        return f'{self.product_part}'

    def get_sku(self):
        return f'{self.sku}'


class Design(models.Model):
    design = models.CharField(max_length=250)
    design_version = models.CharField(max_length=50)
    sku = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Design'
        verbose_name_plural = 'Design'

    def __str__(self):
        return f'{self.design} ({self.sku})'
        # return f'{self.design_name} ({self.design_portfolio} {self.design_version})'

    def get_name(self):
        return f'{self.design}'

    def get_sku(self):
        return f'{self.sku}'


class DesignPortfolio(models.Model):
    design_portfolio = models.CharField(max_length=50)
    designs = models.ManyToManyField(Design)
    sku = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Design Portfolio'
        verbose_name_plural = 'Design Portfolios'

    def __str__(self):
        return f'{self.design_portfolio}'

    def get_name(self):
        return f'{self.design_portfolio}'

    def get_sku(self):
        return f'{self.sku}'


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_sku = models.CharField(max_length=100)
    product_type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True, blank=True)
    product_part = models.ForeignKey(ProductPart, on_delete=models.SET_NULL, null=True, blank=True)
    design_portfolio = models.ForeignKey(DesignPortfolio, on_delete=models.SET_NULL, null=True, blank=True)
    design = models.ForeignKey(Design, on_delete=models.SET_NULL, null=True, blank=True)
    color = models.ManyToManyField(Color)
    size = models.ManyToManyField(Size)

    objects = ProductManager()

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.get_product_sku()

    def get_product_name(self):
        product_type = self.product_type.get_name()
        design = self.design.get_name()
        product_part = self.product_part.get_sku()
        color = self.color.get_name()
        size = self.size.get_sku()

        self.product_name = f'{design} on {product_part} {color} {size} {product_type}'

        return self.product_name

    def get_product_sku(self):
        product_type = self.product_type.get_sku()
        design_portfolio = self.design_portfolio.get_sku()
        design = self.design.get_sku()
        product_part = self.product_part.get_sku()
        color = self.color.get_sku()
        size = self.size.get_sku()

        self.product_sku = f'{product_type}-{design_portfolio}{design}-{product_part}-{color}-{size}'

        return self.product_sku
