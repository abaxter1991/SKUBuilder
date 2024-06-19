import logging
from datetime import datetime

from django.shortcuts import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from .models import (
    Product,
    DesignPortfolio,
    Design,
    ProductType,
    ProductPart,
    Color,
    Size,
)
from .forms import (
    ProductCreateModelForm,
    DesignPortfolioModelForm,
    DesignVersionModelForm,
    ProductTypeModelForm,
    ProductPartModelForm,
    ColorModelForm,
    SizeModelForm,
)

from integrations.sdk_builds.dear_sdk.client import Client as DearClient

logger = logging.getLogger(__name__)


class ProductPartSmartReorder(generic.ListView):
    template_name = 'product_studio/smart_reorder/product_part_smart_reorder.html'
    context_object_name = 'orders'

    def get_reorder_list(self):
        dear = DearClient(account_id='10bbe300-9dd1-46f1-ad19-fa9ada88cdab',
                          api_key='8ffc6d82-700c-e68c-22cc-d585deb2e46d')

        all_sales = dear.sales.sale_list(status='Backordered').json()
        
        for order in all_sales['SaleList']:
            order['OrderDate'] = datetime.strptime(order['OrderDate'], '%Y-%m-%dT%H:%M:%SZ')

        sale_list = all_sales['SaleList']
        
        # # TODO: Get list of all products needed to order and start for loop to do the following calculation.
        # total_on_pending_order =            int('Total number of the product on all pending sales orders.')
        # part_sku =                          'Get SKU for the main part for the product.'
        # part_name =                         'Get Name for the main part for the product.'
        # total_in_inventory =                int('Total number of the part_name/part_sku in current inventory *after allocation.')
        # total_of_part_to_order =            int('total_on_pending_order - total_in_inventory')
        # possible_vendors =                  'Get list of all possible vendors for the product.'

        # part_order = {
        #     'Name': part_name,
        #     'SKU': 'HATPRT-RCH168-BLK',
        #     'TotalToOrder': total_of_part_to_order,
        #     'AllVendors': [
        #         possible_vendors
        #     ]
        # }

        return sale_list

    def get_queryset(self):
        # TODO: Use get_reorder_list function to create a queryset.
        queryset = self.get_reorder_list()

        return queryset


############################################################ PRODUCTS ############################################################


class ProductListView(generic.ListView):
    template_name = 'product_studio/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        user = self.request.user
        queryset = Product.objects.all()

        return queryset

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        user = self.request.user
        queryset = Product.objects.all()

        context.update({
            'products': queryset
        })

        return context


class ProductCreateView(LoginRequiredMixin, generic.CreateView, generic.ListView):
    template_name = 'product_studio/product_list.html'
    form_class = ProductCreateModelForm
    context_object_name = 'products'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('product_studio:product_studio')

    def get_queryset(self):
        queryset = Product.objects.all()

        return queryset

    def get_context_data(self, **kwargs):
        context = super(ProductCreateView, self).get_context_data(**kwargs)
        queryset = Product.objects.all()

        context.update({
            'products': queryset
        })

        for item in queryset:
            print(item.color.all())

        return context


# class ProductDetailView(LoginRequiredMixin, generic.DetailView):
#     template_name = 'product_studio/products/product_detail.html'
#     context_object_name = 'product'

#     def get_queryset(self):
#         user = self.request.user
#         queryset = Product.objects.all()

#         return queryset


# class ProductUpdateView(LoginRequiredMixin, generic.UpdateView):
#     template_name = 'product_studio/products/product_update.html'
#     form_class = ProductModelForm

#     def get_queryset(self):
#         user = self.request.user
#         return Product.objects.all()

#     def get_success_url(self):
#         return reverse('product_studio:product_list')

#     def form_valid(self, form):
#         form.save()
#         messages.info(self.request, 'You have successfully updated this product')
#         return super(ProductUpdateView, self).form_valid(form)


# class ProductDeleteView(LoginRequiredMixin, generic.DeleteView):
#     template_name = 'product_studio/products/product_delete.html'

#     def get_success_url(self):
#         return reverse('product_studio:product_list')

#     def get_queryset(self):
#         user = self.request.user
#         return Product.objects.all()


# ############################################################ DESIGN PORTFOLIOS ############################################################


# class DesignPortfolioListView(LoginRequiredMixin, generic.ListView):
#     template_name = 'product_studio/design_portfolios/design_portfolio.html'
#     context_object_name = 'design_portfolio'

#     def get_queryset(self):
#         user = self.request.user
#         queryset = DesignPortfolio.objects.all()

#         return queryset

#     def get_context_data(self, **kwargs):
#         context = super(DesignPortfolioListView, self).get_context_data(**kwargs)
#         user = self.request.user
#         queryset = DesignPortfolio.objects.all()

#         context.update({
#             'design_portfolio': queryset
#         })

#         return context


# class DesignPortfolioCreateView(LoginRequiredMixin, generic.CreateView):
#     template_name = 'product_studio/design_portfolios/design_portfolio_create.html'
#     form_class = DesignPortfolioModelForm
#     def get_success_url(self):
#         return reverse('product_studio:design_portfolio_list')

#     def form_valid(self, form):
#         design_portfolio = form.save(commit=False)
#         design_portfolio.save()
#         send_mail(
#             subject='A design portfolio has been created',
#             message='Go to the site to see the new design portfolio',
#             from_email='test@test.com',
#             recipient_list=['test2@test.com']
#         )
#         messages.success(self.request, 'You have successfully created a design portfolio')
#         return super(DesignPortfolioCreateView, self).form_valid(form)


# class DesignPortfolioDetailView(LoginRequiredMixin, generic.DetailView):
#     template_name = 'product_studio/design_portfolios/design_portfolio_detail.html'
#     context_object_name = 'design_portfolio'

#     def get_queryset(self):
#         user = self.request.user
#         queryset = DesignPortfolio.objects.all()

#         return queryset


# class DesignPortfolioUpdateView(LoginRequiredMixin, generic.UpdateView):
#     template_name = 'product_studio/design_portfolios/design_portfolio_update.html'
#     form_class = DesignPortfolioModelForm

#     def get_queryset(self):
#         user = self.request.user
#         return DesignPortfolio.objects.all()

#     def get_success_url(self):
#         return reverse('product_studio:design_portfolio_list')

#     def form_valid(self, form):
#         form.save()
#         messages.info(self.request, 'You have successfully updated this design portfolio')
#         return super(DesignPortfolioUpdateView, self).form_valid(form)


# class DesignPortfolioDeleteView(LoginRequiredMixin, generic.DeleteView):
#     template_name = 'product_studio/design_portfolios/design_portfolio_delete.html'

#     def get_success_url(self):
#         return reverse('product_studio:design_portfolio_list')

#     def get_queryset(self):
#         user = self.request.user
#         return DesignPortfolio.objects.all()


############################################################ DESIGN VERSIONS ############################################################




############################################################ PRODUCT TYPES ############################################################




############################################################ PRODUCT PARTS ############################################################




############################################################ COLORS ############################################################




############################################################ SIZES ############################################################



