__author__ = 'ntrepid8'
from functools import wraps
allowed_headers = [
    'X-Custom-Header',
    'X-Requested-With',
    'origin',
    'content-type',
    'X-MaaSive-Token',
    'X-Auth-Token',
    'Cache-Control',
    'X-Smart-Cache'
]


def cors_support(method):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        origin = self.request.headers.get('origin')
        if not origin:
            return method(self, *args, **kwargs)
        self.set_header('Access-Control-Allow-Origin', origin)
        self.set_header('Access-Control-Allow-Credentials', 'true')
        self.set_header('Access-Control-Allow-Methods', 'OPTIONS, GET, POST')
        self.set_header("Access-Control-Allow-Headers", ', '.join(allowed_headers))
        return method(self, *args, **kwargs)
    return wrapper
