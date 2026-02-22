import requests


def fetch_users():
    """
    Fetch users from RandomUser public API.
    Returns list of user records (JSON).
    """
    url = "https://randomuser.me/api/?results=50"

    response = requests.get(url, timeout=10)

    # Raise error if API fails
    response.raise_for_status()

    data = response.json()

    return data["results"]