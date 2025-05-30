from fastapi import FastAPI
from hashlib import sha256

# from models.helpers import hash_and_encode

app = FastAPI()


# @app.get("/")
# def read_root():
#     # hash_and_encode("Testing out this string")
#     return hash_and_encode("Testing out this string")

def hash_and_encode(input: str, isCustom = False):
    hashed = sha256(input.encode('utf-8')).hexdigest()
    encoded = int(hashed, 16)

    if 

# class User

def main():
    hexed = hash_and_encode("hi im paul")
    print(hexed)
    print(int(hexed, 16))
    

if __name__ == "__main__":
    main()

"""

1. Make hashing function return a hashed string MD5 or SHA-256
    then make it encoded base =62
2. Store in an object
3. Make User class


"""
