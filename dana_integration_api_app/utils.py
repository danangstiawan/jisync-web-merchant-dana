from django.http import JsonResponse
from http import HTTPStatus
import bcrypt
import jwt


def construct_response(data=None, status=HTTPStatus.OK, msg="Success", code=None):
    return JsonResponse(
        {
            "status": status,
            "msg": msg,
            "data": data,
            "code": code,
        },
        status=status,
    )


salt = "$2b$12$MmB14Yiy2iC7RLxQrHujhe".encode("utf-8")
# print(salt)


def gen_salt():
    return bcrypt.gensalt()


def hash_password(password):
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed_password.decode("utf-8")


def verify_password(password, hashed_password):
    return password == hashed_password


secret_key = "SECREEE"


def encode_token(payload):
    return jwt.encode(payload, secret_key, algorithm="HS256")


def decode_token(token):
    return jwt.decode(token, secret_key, algorithms=["HS256"])
