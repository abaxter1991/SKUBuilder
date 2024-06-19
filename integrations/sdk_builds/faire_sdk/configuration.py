


class Configuration:
    def __init__(self, api_access_token):
        self.api_access_token = api_access_token

        self.headers = {
            'X-FAIRE-ACCESS-TOKEN': self.api_access_token
        }

    def get_url(self, url_path):
        return f'https://www.faire.com/external-api/v2{url_path}'
