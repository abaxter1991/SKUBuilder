from django import forms

from .models import SalesOrder


class SalesOrderForm(forms.ModelForm):
    class Meta:
        model = SalesOrder
        fields = (
            'sales_channel',
            'id',
            'display_id',
            'status',
            'source',
            'brand_discounts',
            'original_order_id',
            'created_at',
            'updated_at',
            'payment_initiated_at',
            'processing_at',
            'expected_ship_date',
            'requested_ship_date',
            'ship_after',
            'item_subtotal',
            'payout_fee_percentage',
            'payout_fee_cost',
            'commission_percentage',
            'commission_cost',
            'total_payout',
        )
