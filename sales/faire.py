import json
import requests
from datetime import datetime

from .models import SalesOrder

"""
The code in this file looks like crap, and you might be wondering why I wrote functions instead of class methods. When
I was writing this code, I was in the middle of testing the functionality of these external API's and found it easier
to test with functions first. The plan was to move these functions into the classes as class methods, however, we
decided to rebuild the SKUBuilder project as an API only application and then build a new front end with Next.JS.
Doing this allowed us to build a more robust frontend with realtime updates in the browser.

I will look into the other project that was built in place of this and get the completed version of this file.
"""


class Faire_API:
    """
    Call Limit: 20 calls per second
    Cost: $0
    API Documentation: https://faire.github.io/external-api-docs/#introduction
    """
    TOKEN = 'API token from Faire'


class MyFaireStore:
    def __init__(self, api_token):
        self.api_token = api_token

    def manage(self, endpoint):
        method = endpoint[0].lower()
        url = endpoint[1]

        headers = {'X-FAIRE-ACCESS-TOKEN': self.api_token}
        auto_request = getattr(requests, method)

        return auto_request(url, headers=headers)


def my_faire_store():
    my_faire_store = MyFaireStore(Faire_API.TOKEN)
    my_faire_orders = my_faire_store.manage(Orders.GET_ALL_ORDERS)
    data = json.dumps(my_faire_orders.json(), indent=4)

    return json.loads(data)


def _get_a_single_order_by_id(id):
    return ('GET', f'https://www.faire.com/api/v1/orders/{id}')


def convert_dt(dt):
    dt, _ = dt.split('.')

    # Format for Faire API V2: '%Y-%m-%dT%H:%M:%S.%f'
    return datetime.strptime(dt, '%Y%m%dT%H%M%S')


def total_cost_products(products):
    cost = 0

    for product in products:
        cost += product['price_cents'] * product['quantity']

    return cost


def total_payout_amount(item_subtotal, fees, discounts):
    if item_subtotal == 0:
        return item_subtotal
    else:
        discount_amount_cents = 0
        discount_percentage = 0

        if discounts:
            discount_amount_cents = discounts[0]['discount_amount_cents']
            discount_percentage = discounts[0]['discount_percentage']

        if discount_amount_cents != 0:
            discount_amount_cents = item_subtotal - discount_amount_cents

        if discount_percentage != 0:
            discount_percentage = item_subtotal * discount_percentage

        return item_subtotal - (fees['payout_fee_cents'] + fees['commission_cents']) - discount_amount_cents - discount_percentage


def sync_faire_orders():
    my_faire_orders = my_faire_store()

    for order in my_faire_orders['orders']:
        try:
            fees = order['payout_costs']
            discounts = order['brand_discounts']
            item_subtotal = total_cost_products(order['items'])
            total_payout = total_payout_amount(item_subtotal, fees, discounts)

            sales_order = SalesOrder.objects.create(
                sales_channel='Faire',
                id=order['id'],
                display_id=f"#{order['display_id']}",
                status=order['state'],
                source=order['source'],
                customer=order['address']['company_name'],
                brand_discounts=order['brand_discounts'],
                created_at=convert_dt(order['created_at']),
                updated_at=convert_dt(order['updated_at']),
                payment_initiated_at=convert_dt(order['payment_initiated_at']),
                processing_at=convert_dt(order['processing_at']),
                item_subtotal=int(item_subtotal),
                payout_fee_percentage=int(fees['payout_fee_bps']),
                payout_fee_cost=int(fees['payout_fee_cents']),
                commission_percentage=int(fees['commission_bps']),
                commission_cost=int(fees['commission_cents']),
                total_payout=int(total_payout),
            )
        except Exception as error:
            print(error)


class Orders:
    GET_ALL_ORDERS = ('GET', 'https://www.faire.com/api/v1/orders')
    GET_A_SINGLE_ORDER_BY_ID = _get_a_single_order_by_id


class Products:
    pass


class ProductOptions:
    pass


class ProductStateManagement:
    pass


class OrderItems:
    pass


class Shipments:
    pass


class Brands:
    pass


class Retailers:
    pass


class Addresses:
    pass


class PayoutCosts:
    pass
