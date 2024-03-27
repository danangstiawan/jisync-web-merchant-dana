from ..controller.user_controller import User_Controller
from ..utils import construct_response, hash_password
from http import HTTPStatus


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
                is_admin=False,
                gender=new_user["gender"],
                address=new_user["address"],
            )
            if err != None:
                return construct_response(
                    [],
                    code=HTTPStatus.BAD_REQUEST,
                    msg="create user failed" + str(err),
                )
            return construct_response(msg="create user success")
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
