import requests
from requests_ntlm import HttpNtlmAuth


class HttpFormDigestAuthException(Exception):
    pass


class HttpFormDigestAuth(HttpNtlmAuth):
    """HTTP Form Digest Authentication for SharePoint"""

    def __init__(self, username, password, base_url):
        """
        :param username: Username in format 'Domain\\username'
        :param password: Password
        :param base_url: Base URL to authenticate
        """
        super().__init__(username, password)
        if base_url.endswith('/'):
            base_url = base_url[:-1]
        self.endpoint_url = base_url + '/_api/contextinfo'

    def __call__(self, r):
        headers = {'Content-Type': 'application/json;odata=verbose',
                   'Accept': 'application/json;odata=verbose'}
        response = requests.post(url=self.endpoint_url,
                                 headers=headers,
                                 auth=HttpNtlmAuth(self.username, self.password))
        response.raise_for_status()
        try:
            digest = response.json()['d']['GetContextWebInformation']['FormDigestValue']
            r.headers['x-RequestDigest'] = digest
        except KeyError:
            raise HttpFormDigestAuthException()
        return super().__call__(r)
