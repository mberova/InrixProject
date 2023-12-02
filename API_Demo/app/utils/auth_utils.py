import requests

HASH_TOKEN = 'ZWI5ZWFiamI5aHxkUDZyMG5lazJEOFNOOWhkNFpvTVg0Z0cxall3aEUyOThhVVp5ekNK'
APP_ID = 'eb9eabjb9h'
TOKEN_URL = 'https://api.iq.inrix.com/auth/v1/appToken'

def get_token():
    #Pass in the app_id and hash_token as query parameters
    params = {
        'appId': APP_ID,
        'hashToken': HASH_TOKEN
    }
    # Make the request to the INRIX token endpoint
    try:
        response = requests.get(TOKEN_URL, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses

        data = response.json()
        # Extract the token from the response
        # For more info on how to parse the response, see the json_parser_example.py file
        token = data['result']['token']
        return token, response.status_code

    except requests.exceptions.RequestException as e:
        return f'Request failed with error: {e}', None
    except (KeyError, ValueError) as e:
        return f'Error parsing JSON: {e}', None