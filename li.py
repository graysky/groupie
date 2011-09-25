"""Wrapper for calling LinkedIn methods"""
import os
import sys

# Add locally modified linked in to path
try:
    current_dir = os.path.abspath(os.path.dirname(__file__))
except NameError:
    current_dir = os.getcwd() # repl

sys.path.append(os.path.join(current_dir, 'python_linkedin/linkedin'))

from linkedin import LinkedIn

# hs_hackday info
KEY = 'nowsh2sf2a4n' 
SECRET = 'vNLLDpdhAyovJrX6' 
RETURN_URL = "http://dev.graysky.org"

def mgc_handle():
    """Get API handle for Mike's account using hs_hackday app"""
    api = LinkedIn(KEY, SECRET, RETURN_URL)
    api._access_token = '4a1db6ff-999d-483c-8b20-779bed512d0f'
    api._access_token_secret = '6729077d-6861-456a-9782-5b5e46ce7733'
    return api

def request_auth():
    """TODO Make real request """
    api = LinkedIn(KEY, SECRET, RETURN_URL)
    api.request_token()
    print api._request_token

    print api._request_token_secret
    url = api.get_authorize_url()
    print url

    #oauth_token = bf688755-dd92-4792-ab8f-ffd7085c7e40
    # oauth_verifier=27219

    # Flow to get approved:
    # api = linkedin.LinkedIn(KEY, SECRET, RETURN_URL)
    # api.requestToken()
    # api.request_token
    # > '829861f4-2723-4fe4-9e36-c77564ec0a93'
    # api.request_token_secret
    # > 'b8b5aa3b-731b-43dd-ab44-3cffc857ad1f'
    # api.getAuthorizeURL()
    # > https://api.linkedin.com/uas/oauth/authorize?oauth_token=829861f4-2723-4fe4-9e36-c77564ec0a93
    # <paste in browser will return link like: http://localhost/?oauth_token=829861f4-2723-4fe4-9e36-c77564ec0a93&oauth_verifier=48662
    # 
    # api.accessToken(verifier = '48662')
    # > True (hopefully!)
    #  api.access_token
    # '4a1db6ff-999d-483c-8b20-779bed512d0f'