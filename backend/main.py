from fastapi import FastAPI, HTTPException

from db.service import DB
from models import ShortURL, User

# from models import ShortURL, URLEncoder, User

# from models.helpers import hash_and_encode

# Enum-like dictionary
APP_ROUTES = {
    "post": {
        "get_with_id": "get_with_id",
        "create_new_user": "create_new_user",
    },
}

app = FastAPI()


# @app.post(f"/rmpl/{APP_ROUTES.post}")
def create_new_user(new_user: User):
    try:
        with DB() as db:
            db.create_new_user(new_user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {"message": "User created", "status": 200, "res": new_user}


def main():
    temp: User = {
        "id": "str",
        "first_name": "str",
        "last_name": "str",
        "username": "str",
        "email": "EmailStr",
        "date_of_birth": "date",
        "password_hash": "SecretBytes",
    }
    # ------------------POST (Creating a new url)-----------------
    print(create_new_user(temp))
    # new_url: str
    # while True:
    #     get_input = input("Give me a URL")
    #     if not get_input or not get_input.strip():
    #         print("try again")
    #     else:
    #         new_url = get_input
    #         break

    # # Init new short url
    # new_short_url = ShortURL(new_url)


# If we are in the main file, then execute
if __name__ == "__main__":
    main()
