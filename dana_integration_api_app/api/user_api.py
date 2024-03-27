from ..controller.user_controller import User_Controller
from ..utils import construct_response, hash_password
from http import HTTPStatus
import json


def users(req):
    if req.method == "GET":
        try:
            users = User_Controller.get_all_user()
            # print(users)
            return construct_response(list(users))
        except Exception as err:
            print(err)
            return construct_response(
                [],
                code=HTTPStatus.INTERNAL_SERVER_ERROR,
                msg="something wrong!" + str(err),
            )

    return construct_response(
        None, code=HTTPStatus.NOT_FOUND, msg="Unknown path!" + str(err)
    )


def user_id(req, user_id):
    if req.method == "POST":
        try:
            # print(req.body)
            new_user = dict(req.POST.items())
            # json.loads(req.body.decode("utf-8"))
            print(new_user)
            obj = {}

            cols = [
                "full_name",
                "email",
                "password",
                "phone",
                "is_admin",
                "gender",
                "email",
            ]
            for val in cols:
                if new_user.get(val):
                    if val == "is_admin":
                        obj[val] = True if new_user[val] == "true" else False
                    else:
                        obj[val] = new_user[val]
            resp, err = User_Controller.update_user(user_id, **obj)
            if err != None:
                return construct_response(
                    None,
                    code=HTTPStatus.BAD_REQUEST,
                    msg="update user failed" + str(err),
                )
            return construct_response(msg="update user success")
        except Exception as err:
            print(err)
            return construct_response(
                None,
                code=HTTPStatus.INTERNAL_SERVER_ERROR,
                msg="something wrong!" + str(err),
            )


def user(req):
    if req.method == "POST":
        try:
            new_user = dict(req.POST.items())
            print(new_user)
            resp, err = User_Controller.add_user(
                full_name=new_user["full_name"],
                email=new_user["email"],
                password=hash_password(new_user["password"]),
                phone=new_user["phone"],
                is_admin=True if new_user["is_admin"] == "true" else False,
                gender=new_user["gender"],
                address=new_user["address"],
            )
            if err != None:
                return construct_response(
                    None,
                    code=HTTPStatus.BAD_REQUEST,
                    msg="create user failed" + str(err),
                )
            return construct_response(msg="create user success")
        except Exception as err:
            print(err)
            return construct_response(
                None,
                code=HTTPStatus.INTERNAL_SERVER_ERROR,
                msg="something wrong!" + str(err),
            )

    return construct_response(
        None, code=HTTPStatus.NOT_FOUND, msg="Unknown path!" + str(err)
    )
