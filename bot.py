def run():
   # Import the requests module for send a PUT request
import requests
# Import the base64 module for encoding a file to base64
import base64

githubAPIURL = "https://api.github.com/repos/daniyc4/test/contents/test.txt"
# Replace "bracketcounters" with your username, replace "test-repo" with your repository name and replace "new-image.png" with the filename you want to upload from local to GitHub.

# Paste your API token here
githubToken = "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"


with open("test.txt", "rb") as f:
    # Encoding "my-local-image.jpg" to base64 format
    encodedData = base64.b64encode(f.read())

    headers = {
        "Authorization": f'''Bearer {githubToken}''',
        "Content-type": "application/vnd.github+json"
    }
    data = {
        "message": "My commit message", # Put your commit message here.
        "content": encodedData.decode("utf-8")
    }

    r = requests.put(githubAPIURL, headers=headers, json=data)
    print(r.text) # Printing the response
