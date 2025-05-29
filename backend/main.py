from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "It works!"}

'''

1. Make hashing funcition return a hashed string
2. Store in an object
3. Make User class
    

'''
