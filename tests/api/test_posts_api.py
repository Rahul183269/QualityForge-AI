import requests


def test_get_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    response = requests.get(url, timeout=10)

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["userId"] == 1
    assert isinstance(data["title"], str)
    assert data["title"] != ""
    assert isinstance(data["body"], str)
    assert isinstance(data, dict)

def test_get_nonexistent_post():
    url = "https://jsonplaceholder.typicode.com/posts/999999"

    response = requests.get(url, timeout=10)

    assert response.status_code == 404