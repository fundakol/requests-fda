# requests-fda

This package allows for HTTP Form Digest Authentication along with NTLM authentication for SharePoint site using the requests library.

## Usage

```python
import requests
from requests_fda import HttpFormDigestAuth

auth = HttpFormDigestAuth('domain\\username','password', 'http://sharepoint-site.com')
requests.get('http://sharepoint-site.com/home.aspx', auth=auth)
```

## Installation
```
python setup.py install
```
