import requests

def simple_http_client(url):
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Print the response content
            print("Response from", url)
            print(response.json())
        else:
            print("Request failed with status code:", response.status_code)
            print("JSON:", response.json())

    except requests.exceptions.RequestException as e:
        # Handle any request exceptions (e.g., connection error)
        print("Request error:", e)

if __name__ == "__main__":
    url =  "http://127.0.0.1:5000?string=WUaKFvAVjD"
    simple_http_client(url)
