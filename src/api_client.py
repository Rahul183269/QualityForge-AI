
import requests


class APIClient:
    def __init__(self, base_url, timeout=10):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()

        self.session.headers.update({
            "Accept": "application/json"
        })


    

    def get(self, endpoint):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        try:
            return self.session.get(url, timeout=self.timeout)
        except requests.exceptions.Timeout:
            print(f"Request timed out: {url}")
            raise
        except requests.exceptions.ConnectionError:
            print(f"Could not connect to: {url}")
            raise
