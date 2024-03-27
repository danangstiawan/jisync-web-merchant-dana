from ..models.User import User
from ..utils import construct_response, hash_password, verify_password
from http import HTTPStatus
from django.forms.models import model_to_dict
from django.core.exceptions import ObjectDoesNotExist


class User_Controller:

    @staticmethod
    def login(req, email, password):
        try:
            user = User.objects.get(email=email)

            if not user.is_active:
                return construct_response(
                    msg="User not active",
                    status=HTTPStatus.FORBIDDEN,
                )
            hashed_pass = hash_password(password)
            if verify_password(user.password, hashed_pass):
                req.session["user_id"] = user.id
                return construct_response(data="Success")
            else:
                return construct_response(
                    status=HTTPStatus.UNAUTHORIZED, msg="Wrong password!"
                )

        except ObjectDoesNotExist:
            return construct_response(
                code="user/not-exist",
                status=HTTPStatus.NOT_FOUND,
                msg="Email not found!",
            )
        except Exception as err:
            return construct_response(
                msg=str(err),
                status=HTTPStatus.BAD_REQUEST,
            )

    @staticmethod
    def register(user_data):
        try:
            print(user_data)
            new_user = User(
                full_name=user_data["full_name"],
                email=user_data["email"],
                password=hash_password(user_data["password"]),
                phone=user_data["phone"],
                is_admin=False,
                gender="U",
                created_by=0,
                updated_by=0,
            )
            new_user.save()
            print(new_user)
            return construct_response(data=model_to_dict(new_user))

        except Exception as err:
            return construct_response(
                msg=str(err),
                status=HTTPStatus.BAD_REQUEST,
            )

    def add_user(**user_data):
        try:
            # print(user_data)
            new_user = User(
                **user_data,
                created_by=0,
                updated_by=0,
            )
            new_user.save()
            # print(new_user)
            return model_to_dict(new_user), None

        except Exception as err:
            print(err)
            return None, err

    def update_user(user_id, **user_data):
        try:
            # print(user_data)
            user = User.objects.get(id=user_id)
            for key, value in user_data.items():
                if hasattr(user, key):
                    if key == "password":
                        setattr(user, key, hash_password(value))
                    else:
                        setattr(user, key, (value))
            user.save()
            # print(new_user)
            return model_to_dict(user), None

        except Exception as err:
            print(err)
            return None, err

    def get_all_user():

        # print(user_data)
        forbidden_fields = ["password"]
        fields = [
            field.name
            for field in User._meta.get_fields()
            if field.name not in forbidden_fields
        ]

        new_user = User.objects.all().values(*fields)

        # print(new_user)
        return new_user
