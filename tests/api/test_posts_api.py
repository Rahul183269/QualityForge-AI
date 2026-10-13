import requests
import pytest
import json
from pathlib import Path
from jsonschema import validate
from src.api_client import APIClient


def test_get_post(api_session):
    url = "https://jsonplaceholder.typicode.com/posts/1"

    headers = {
        "Authorization": "Bearer fake-test-token",
        "Accept": "application/json"
    }

    response = api_session.get(
        url,
        headers=headers, 
        timeout=10
    )

    assert response.status_code == 200
    assert response.headers["Content-Type"].startswith("application/json")

    data = response.json()
    assert isinstance(data, dict), "Expected the response body to be a JSON object"

    assert data["id"] == 1
    assert data["userId"] == 1
    assert isinstance(data["title"], str)
    assert data["title"] != ""
    assert isinstance(data["body"], str)
    assert data["body"] != ""

def test_get_nonexistent_post(api_session):
    url = "https://jsonplaceholder.typicode.com/posts/999999"

    response = api_session.get(url, timeout=10)
    assert response.status_code == 404

    data = response.json()
    assert data== {}


VALID_USER_IDS = [
    pytest.param(1, id="first_user"),
    pytest.param(2, id="second_user"),
    pytest.param(3, id="third_user"),
]

@pytest.mark.parametrize("user_id", VALID_USER_IDS)
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
        assert isinstance(post, dict)
        assert "id" in post
        assert "title" in post
        assert "body" in post
        assert post["userId"] == user_id


def test_get_posts_invalid_user_id():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts",
        params={"userId": "abc"},
        timeout=10
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert data == []

def test_get_post_with_invalid_id():
    url = "https://jsonplaceholder.typicode.com/posts/abc"

    response = requests.get(url, timeout=10)

    assert response.status_code == 404

    data = response.json()

    assert data == {}



def test_api_client_get_post():
    client = APIClient("https://jsonplaceholder.typicode.com")

    try:
        response = client.get("/posts/1")

        assert response.status_code == 200
        assert response.json()["id"] == 1
    finally:
        client.session.close()



def test_post_has_expected_json_fields(api_session):
    response = api_session.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        timeout=10,
    )

    assert response.status_code == 200

    post = response.json()

    expected_fields = {"userId", "id", "title", "body"}

    assert expected_fields.issubset(post.keys())



def test_post_has_expected_field_types(api_session):
    response = api_session.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        timeout=10,
    )

    assert response.status_code == 200

    post = response.json()

    assert isinstance(post["userId"], int)
    assert isinstance(post["id"], int)
    assert isinstance(post["title"], str)
    assert isinstance(post["body"], str)



def test_post_has_valid_field_values(api_session):
    response = api_session.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        timeout=10,
    )

    assert response.status_code == 200

    post = response.json()

    assert post["id"] > 0
    assert post["userId"] > 0
    assert post["title"].strip() != ""
    assert post["body"].strip() != ""


def test_post_response_matches_schema(api_session):
    response = api_session.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        timeout=10,
    )

    assert response.status_code == 200

    post = response.json()

    schema_path = (
        Path(__file__).resolve().parents[2]
        / "test_data"
        / "schemas"
        / "post_schema.json"
    )

    with schema_path.open(encoding="utf-8") as schema_file:
        schema = json.load(schema_file)

    validate(instance=post, schema=schema)
