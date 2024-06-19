from django.db.models import Manager


class ColorManager(Manager):
    def create_color(self, color, sku, **extra_fields):
        color = self.model(
            color=color,
            sku=sku,
            **extra_fields)

        color.save()

        return color


class ProductManager(Manager):
    def create_product(self, product_type, design_portfolio, design, product_part, color, size, **extra_fields):
        product_type_name = product_type.get_name()
        design_portfolio_name = design_portfolio.get_name()
        design_name = design.get_name()
        product_part_name = product_part.get_name()
        color_name = color.get_name()
        size_name = size.get_name()

        product_type_sku = product_type.get_sku()
        design_portfolio_sku = design_portfolio.get_sku()
        design_sku = design.get_sku()
        product_part_sku = product_part.get_sku()
        color_sku = color.get_sku()
        size_sku = size.get_sku()

        product_name = f'{design_name} on {product_part_sku} {color_name} {size_sku} {product_type_name}'
        product_sku = f'{product_type_sku}-{design_portfolio_sku}{design_sku}-{product_part_sku}-{color_sku}-{size_sku}'

        print(product_name)
        print(product_sku)

        product = self.model(
            product_name=product_type,
            product_sku=product_type,
            product_type=product_type,
            design_portfolio=design_portfolio,
            design=design,
            product_part=product_part,
            color=color,
            size=size,
            **extra_fields
        )

        product.save()

        return product
