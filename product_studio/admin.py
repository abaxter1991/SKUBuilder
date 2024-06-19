from django.contrib import admin

from .models import Color, Size, ProductType, DesignPortfolio, Design, ProductPart, Product
# from .forms import ProductModelForm


# class ColorInline(admin.StackedInline):
#     model = Color


# class ProductPartAdmin(admin.ModelAdmin):
#     inlines = [
#         ColorInline
#     ]


# class DesignVersionInline(admin.StackedInline):
#     model = DesignVersion


# class DesignPortfolioAdmin(admin.ModelAdmin):
#     inlines = [
#         DesignVersionInline
#     ]

# class ProductAdmin(admin.ModelAdmin):
#     form_class = ProductModelForm

admin.site.register(Color)
admin.site.register(Size)
admin.site.register(ProductType)
admin.site.register(DesignPortfolio) # , DesignPortfolioAdmin)
admin.site.register(Design)
admin.site.register(ProductPart) # , ProductPartAdmin)
admin.site.register(Product) # , ProductAdmin)
