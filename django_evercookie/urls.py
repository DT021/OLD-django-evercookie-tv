try:
    from django.conf.urls import url
except ImportError:
    from django.conf.urls.defaults import url

from django_evercookie.views import (
    evercookie_cache,
    evercookie_png,
    evercookie_etag,
    evercookie_core,
    evercookie_auth,
)
"""URLs differ from standart evercookie_<storage_method> to dodge easyprivacy blocking rules"""


urlpatterns = [
    url(r'^ec/cache', evercookie_cache, name='ecache'),
    url(r'^ec/png', evercookie_png, name='epng'),
    url(r'^ec/etag', evercookie_etag, name='ecetag'),
    url(r'^ec/cookie', evercookie_core, name='ecookie'),
    url(r'^ec/auth', evercookie_auth, name='ecauth'), 
]
