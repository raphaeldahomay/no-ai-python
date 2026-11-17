import requests

def get_user(user_id: int) -> dict:
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}", timeout=10)

    if response.status_code == 404:
        return None

    content = response.json()

    return {
        'name': content['name']
        , "email": content['email']
        , "city": content['address']['city']
    }
