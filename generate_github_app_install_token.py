import jwt
import time
import requests
import os

# GitHub App settings
app_id = os.environ['APP_ID'] # Github App ID
private_key_path = os.environ['PRIVATE_KEY_PATH'] # PRIVATE_KEY_PATH = 'path_to_your_app_private_key.pem', generated in the app dashboard

# Load the private key
with open(private_key_path, 'r') as file:
    private_key = file.read()

# Generate a JWT
expiration_time = int(time.time()) + (10 * 60)  # Token valid for 10 minutes
payload = {
    'iat': int(time.time()),
    'exp': expiration_time,
    'iss': app_id
}
jwt_token = jwt.encode(payload, private_key, algorithm='RS256')

# GitHub API URL to list installations
url = 'https://api.github.com/app/installations'
# Headers
headers = {
    'Authorization': f'Bearer {jwt_token}',
    'Accept': 'application/vnd.github.v3+json'
}
# Make the request to get a list of installations
response = requests.get(url, headers=headers)
installations = response.json()

installation_id = ''
for installation in installations:
    print(f"Installation ID: {installation['id']} - Account login: {installation['account']['login']}") # Print each installation and its ID
    installation_id = installation['id'] #get last installationId

# GitHub API URL to obtain an installation access token
url = f'https://api.github.com/app/installations/{installation_id}/access_tokens'
headers = {
    'Authorization': f'Bearer {jwt_token}',
    'Accept': 'application/vnd.github.v3+json'
}
# Make the request to get the installation access token
response = requests.post(url, headers=headers)
installation_access_token = response.json()

