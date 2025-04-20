import requests

# Set your OpenAI API key here
api_key = "sk-proj-1H1RKYIUNKLmxb2VhELADbJBHKeDrUaPvnDsRgMISn-HO7pvgvOpFtccbzINxVZEZfwW_TC_gpT3B|bkFJg6_uQY6abhK7qhOHcqPObHHObYpUq_nGB7|t9f7d_wPhaiBN7_zza9l_2p8Jzqele8ur0eeTgA"

# Define the URL for the API endpoint
url = "https://api.openai.com/v1/models"

# Make the request to the API
response = requests.get(
    url,
    headers={
        "Authorization": f"Bearer {api_key}"
    }
)

# Check the response
if response.status_code == 200:
    print("API Key is valid!")
    print("Response:", response.json())
else:
    print("Invalid API Key!")
    print("Error:", response.json())
