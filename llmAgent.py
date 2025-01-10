import requests

def getLLMResponse(text, prompt):
    url = "http://172.245.107.85:5432/api/chat"
    # Prepare the payload
    payload = {
        "text": text,
        "prompt": prompt,
        "auth": "F27SyqNLXOWkh0nK"
    }

    try:
        # Make a POST request to the API
        response = requests.post(url, json=payload)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse and print the response
            data = response.json()
            # print("Response from LLM:", data.get("response"))
            return data.get("response")
        else:
            print(f"Error: {response.status_code}, Message: {response.text}")
    except Exception as e:
        print("An error occurred:", str(e))