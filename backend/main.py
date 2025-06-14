from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from db.service import DB
from models import ShortURL, User

# from models import ShortURL, URLEncoder, User

# from models.helpers import hash_and_encode
app = FastAPI()


class AppRoutes:
    POST = {
        "CREATE_NEW_USER": "create-new-user",
        "CREATE_SHORT_URL": "create-short-url",
    }
    DELETE = {
        "DELETE_USER": "delete-user",
    }
    BASE = "rmpl/"

    def go(self, endpoint):
        return f"{self.BASE}{endpoint}"


r = AppRoutes()
POST, DELETE = vars(AppRoutes()).values()


@app.post(r.go(POST['CREATE_NEW_USER']))
def create_new_user(new_user: User):
    try:
        with DB() as db:
            db.create_new_user(new_user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {"message": "User created", "status": 200, "res": new_user}

@app.post(r.go(POST["create-short-url"]))
def create_short_url(user_id: int, original_url: str ):
    pass

def main():
    temp: User = {
        "first_name": "str",
        "last_name": "str",
        "username": "str2",
        "email": "EmailStr@abcgfd.com",
        "date_of_birth": "2025-06-12",
        "password_hash": "SecretBytes",
    }
    # ------------------POST (Creating a new url)-----------------
    print(create_new_user(temp))


# If we are in the main file, then execute
if __name__ == "__main__":
    main()
