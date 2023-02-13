def run():
   import requests
   import base64
   githubAPIURL = "https://api.github.com/repos/daniyc4/test/contents"
   githubToken = "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"
   with open("test.txt", "rb") as f:
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
