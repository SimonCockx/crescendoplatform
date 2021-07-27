import os
from django.core.exceptions import ImproperlyConfigured

deployment = os.environ['DEPLOYMENT']
if deployment == "development":
    from .development import *
elif deployment == "test":
    from .test import *
elif deployment == "production":
    from .production import *
else:
    raise ImproperlyConfigured(
        "The environment variable DEPLOYMENT should be one of 'development', 'test' or 'production'.")
