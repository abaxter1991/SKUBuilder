import requests


class SaleAPI:
    def __init__(self, config):
        self.config = config

    def sale_list(self, search=None, created_since=None, updated_since=None, ship_by=None, quote_status=None,
                  order_status=None, combined_pick_status=None, combined_pack_status=None,
                  combined_shipping_status=None, combined_invoice_status=None, credit_note_status=None,
                  external_id=None, status=None, ready_for_shipping=None, order_location_id=None,
                  page=1, limit=100, auto_paginate=False):
        search = f'&Search={search}' if search else ''
        created_since = f'&CreatedSince={created_since}' if created_since else ''
        updated_since = f'&UpdatedSince={updated_since}' if updated_since else ''
        ship_by = f'&ShipBy={ship_by}' if ship_by else ''
        quote_status = f'&QuoteStatus={quote_status}' if quote_status else ''
        order_status = f'&OrderStatus={order_status}' if order_status else ''
        combined_pick_status = f'&CombinedPickStatus={combined_pick_status}' if combined_pick_status else ''
        combined_pack_status = f'&CombinedPackStatus={combined_pack_status}' if combined_pack_status else ''
        combined_shipping_status = f'&CombinedShippingStatus={combined_shipping_status}' if combined_shipping_status else ''
        combined_invoice_status = f'&CombinedInvoiceStatus={combined_invoice_status}' if combined_invoice_status else ''
        credit_note_status = f'&CreditNoteStatus={credit_note_status}' if credit_note_status else ''
        external_id = f'&ExternalID={external_id}' if external_id else ''
        status = f'&Status={status}' if status else ''
        ready_for_shipping = f'&ReadyForShipping={ready_for_shipping}' if ready_for_shipping else ''
        order_location_id = f'&OrderLocationID={order_location_id}' if order_location_id else ''
        page = f'?Page={page}'
        limit = f'&Limit={limit}'

        url_path = (f'/SaleList{page}{limit}{search}{created_since}{updated_since}{ship_by}{quote_status}{order_status}'
                    f'{combined_pick_status}{combined_pack_status}{combined_shipping_status}{combined_invoice_status}'
                    f'{credit_note_status}{external_id}{status}{ready_for_shipping}{order_location_id}')

        url = self.config.get_url(url_path)
        headers = self.config.headers

        return requests.get(url=url, headers=headers)
