from django.db import models


class SalesOrder(models.Model):
    id = models.CharField(primary_key=True, max_length=100, verbose_name='ID')
    sales_channel = models.CharField(max_length=50, verbose_name='Sales Channel')
    display_id = models.CharField(unique=True, max_length=100, verbose_name='Display ID')
    status = models.CharField(max_length=100, verbose_name='Status')
    source = models.CharField(max_length=100, verbose_name='Source')
    customer = models.CharField(max_length=100, verbose_name='Customer')
    brand_discounts = models.CharField(max_length=100, null=True, blank=True, verbose_name='Brand Discounts')
    original_order_id = models.CharField(max_length=100, null=True, blank=True, verbose_name='Original Order ID')
    created_at = models.DateTimeField(null=True, blank=True, verbose_name='Created At')
    updated_at = models.DateTimeField(null=True, blank=True, verbose_name='Updated At')
    payment_initiated_at = models.DateTimeField(null=True, blank=True, verbose_name='Payment Initiated At')
    processing_at = models.DateTimeField(null=True, blank=True, verbose_name='Processing At')
    expected_ship_date = models.DateField(null=True, blank=True, verbose_name='Expected Ship Date')
    requested_ship_date = models.DateField(null=True, blank=True, verbose_name='Requested_Ship_Date')
    ship_after = models.DateField(null=True, blank=True, verbose_name='Ship After')
    item_subtotal = models.IntegerField(null=True, blank=True, verbose_name='Item Subtotal')
    payout_fee_percentage = models.IntegerField(null=True, blank=True, verbose_name='Payout Fee Percentage')
    payout_fee_cost = models.IntegerField(null=True, blank=True, verbose_name='Payout Fee Cost')
    commission_percentage = models.IntegerField(null=True, blank=True, verbose_name='Commission Percentage')
    commission_cost = models.IntegerField(null=True, blank=True, verbose_name='Commission Cost')
    total_payout = models.IntegerField(null=True, blank=True, verbose_name='Total Payout')

    class Meta:
        verbose_name = 'Sales Order'
        verbose_name_plural = 'Sales Orders'

    def __str__(self):
        return f'{self.display_id} (Total Payout: {self.total_payout})'
