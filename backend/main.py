from fastapi import FastAPI

from models import ShortURL, User

# from models import ShortURL, URLEncoder, User

# from models.helpers import hash_and_encode

app = FastAPI()

# @app.get("/")
# def read_root():
#     # hash_and_encode("Testing out this string")
#     return hash_and_encode("Testing out this string")


def main():
    # ------------------POST (Creating a new url)-----------------
    new_url: str
    while True:
        get_input = input("Give me a URL")
        if not get_input or not get_input.strip():
            print("try again")
        else:
            new_url = get_input
            break

    # Init new short url
    new_short_url = ShortURL(new_url)


# If we are in the main file, then execute
if __name__ == "__main__":
    main()
