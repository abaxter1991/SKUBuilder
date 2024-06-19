


class Configuration:
    def __init__(self, account_id, api_key):
        self.account_id = account_id
        self.api_key = api_key

        self.headers = {
            'Content-Type': 'application/json',
            'api-auth-accountid': self.account_id,
            'api-auth-applicationkey': self.api_key
        }

    def get_url(self, url_path):
        return f'https://inventory.dearsystems.com/ExternalApi/v2/{url_path}'
