import requests
import urllib
import secrets
import json

# Function to generate authorization URL
def generate_auth_url(app_id, redirect_uri, authorize_url):
    # type: (str, str, str) -> str
    """
    Generate authorization URL
    :param app_id: app_id in TikTok
    :param redirect_uri: url that is redirected from URL
    :param authorize_url: authorize URL in TikTok Business
    :return: Response in str format
    """
    csrf_state = secrets.token_hex(16)

    params = {
        "app_id": app_id,
        "response_type": "code",
        "redirect_uri": redirect_uri,
        "state": csrf_state,
    }

    url = authorize_url + "?" + urllib.parse.urlencode(params)

    return url, csrf_state


# Function to get the access token


def get_auth_code(app_id, redirect_uri, authorize_url):
    # type: (str, str, str) -> str
    """
    Get auth code from app_id
    :param app_id: app_id in TikTok
    :param redirect_uri: url that is redirected from URL
    :param authorize_url: authorize URL in TikTok Business
    :return: Response in str format
    """
    # Generate authorization URL
    print("Generating authorization URL...")
    url, state = generate_auth_url(app_id, redirect_uri, authorize_url)
    print("URL:", url)
    print("State:", state)
    print("Paste the URL you were redirected to")
    # Prompt user for the redirect URL
    input_ = input("Paste the URL you were redirected to: ")

    # Extract authorization code from redirect URL
    auth_code = input_.split("code=")[1].split("&")[0]
    return auth_code


# Function to get the access token
def get_access_token(json_str, url):
    # type: (str, str) -> dict
    """
    Send POST request to get access token
    :param json_str: Args in JSON format
    :param url: URL to get access token
    :return: Response in JSON format
    """
    # url = build_url(path)
    args = json.loads(json_str)
    headers = {
        "Content-Type": "application/json",
    }
    rsp = requests.post(url, headers=headers, json=args)
    return rsp.json()
