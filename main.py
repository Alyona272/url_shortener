from fastapi import FastAPI, HTTPException

import uuid
import hashlib
from model.url import RequestPostUrl
from utils.shortener.shortener import short
from utils.validators.validator import *


from storage.model import InputCreateUser
from storage.pg.pg_storage import PgStorage


app = FastAPI()
storage = PgStorage()


@app.post("/user/", status_code=201)
async def create_user(request_body: InputCreateUser):
    if not validate_email(request_body.email):
        raise HTTPException(status_code=400, detail="Incorrect email")
    if not validate_login(request_body.login):
        raise HTTPException(status_code=400, detail="Incorrect login")
    if not validate_phone_number(request_body.phone_number):
        raise HTTPException(status_code=400, detail="Incorrect phone number")

    try:
        user_id = str(uuid.uuid4())
        storage.save_user(request_body, user_id)
        return {'id': user_id}
    except:
        raise HTTPException(status_code=500, detail="User cannot create")


@app.post("/url/", status_code=201)
async def create_short_url(request_body: RequestPostUrl):
    origin_url = request_body.url
    if not validate_url(origin_url):
        raise HTTPException(status_code=400, detail="Incorrect url")
    short_url = short(origin_url)
    try:
        #short_url = short(origin_url)
        storage.save_short_url(origin_url, short_url)
        return {'short': short_url}
    except:
        raise HTTPException(
            status_code=500, detail="Short url cannot be saved")
