import requests
import json

# Your GitHub token
token = 'YOUR_GITHUB_TOKEN'

# Read the public key from file
with open('~/.ssh/id_rsa.pub', 'r') as file:
    public_key = file.read().strip()

# The headers for the API request
headers = {
    'Authorization': 'token {}'.format(token),
    'Accept': 'application/vnd.github.v3+json'
}

# The data for the new SSH key
data = {
    'title': 'new SSH key',
    'key': public_key
}

# Make the API request
response = requests.post(
    'https://api.github.com/user/keys',
    headers=headers,
    data=json.dumps(data)
)

# Check the response
if response.status_code == 201:
    print('SSH key added successfully.')
else:
    print('Failed to add SSH key. Response:', response.content)
