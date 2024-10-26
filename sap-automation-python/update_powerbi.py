import requests
import os

def update_powerbi_model():
    # Configure your Power BI credentials
    TENANT_ID = os.getenv('TENANT_ID')
    CLIENT_ID = os.getenv('CLIENT_ID')
    CLIENT_SECRET = os.getenv('CLIENT_SECRET')
    WORKSPACE_ID = os.getenv('WORKSPACE_ID')
    DATASET_ID = os.getenv('DATASET_ID')

    # URL to obtain the access token
    AUTH_URL = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"
    # URL to update the semantic model
    UPDATE_URL = f"https://api.powerbi.com/v1.0/myorg/groups/{WORKSPACE_ID}/datasets/{DATASET_ID}/refreshes"

    # Obtain the access token
    auth_data = {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'scope': 'https://analysis.windows.net/powerbi/api/.default'
    }

    response = requests.post(AUTH_URL, data=auth_data)

    if response.status_code != 200:
        raise Exception(f"Error obtaining token: {response.text}")

    access_token = response.json().get('access_token')

    # Start the dataset refresh
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    refresh_response = requests.post(UPDATE_URL, headers=headers)

    if refresh_response.status_code == 202:
        print("The semantic model refresh has started successfully.")
    else:
        raise Exception(f"Error starting refresh: {refresh_response.text}")

if __name__ == "__main__":
    update_powerbi_model()

