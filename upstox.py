from upstox_api.api import *

s = Session ('your_api_key')
s.set_redirect_uri ('your_redirect_uri')
s.set_api_secret ('your_api_secret')

print (s.get_login_url())