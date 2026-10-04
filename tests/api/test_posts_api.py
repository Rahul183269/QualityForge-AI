import requests
import pytest


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


@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_posts_by_user_id(user_id):
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts",
        params={"userId": user_id},
        timeout=10
    )

    assert response.status_code == 200

    posts = response.json()

    assert isinstance(posts, list)
    assert len(posts) > 0

    for post in posts:
        assert post["userId"] == user_id