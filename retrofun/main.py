from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def main():
    return {'message': 'Welcome to my retrofun homepage!'}