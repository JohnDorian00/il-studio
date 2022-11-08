import datetime

from django.http import HttpResponseForbidden, HttpResponseBadRequest, HttpResponse, HttpResponseServerError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from backendApp.modules import db
import json


def is_request_from_user(request):
    try:
        token = request.headers["Token"]
    except Exception as e:
        print("Токен отсутствует в заголовке")
        return False

    try:
        if db.isTokenExist(token)[0][0]:
            return True
    except Exception as e:
        return False

    return False


@api_view(['GET'])
def get_users(request):
    if not is_request_from_user(request):
        return HttpResponseForbidden()

    if request.method == 'GET':
        return Response(db.get_users())


@api_view(['GET'])
def get_rooms(request):
    if not is_request_from_user(request):
        return HttpResponseForbidden()

    if request.method == 'GET':
        return Response(json.dumps(db.get_rooms()))


@api_view(['GET'])
def get_messages(request, room_id):
    if not is_request_from_user(request):
        return HttpResponseForbidden()

    if request.method == 'GET':
        return Response(db.get_messages(room_id))


# curl -X POST -v localhost:8000/send_message/ -d "{\"room_id\": \"1\", \"user_id\": \"1\", \"msg\": \"test_message\"}" --header "Token: b454a363-a801-4bf0-9ac6-8d8f5af862d8"
@api_view(['POST'])
def send_message(request):
    if not is_request_from_user(request):
        return HttpResponseForbidden()

    if request.method == 'POST':
        body = json.loads(request.body)
        try:
            msg, user_id, room_id = body["msg"], body["user_id"], body["room_id"]
        except Exception as e:
            print("Не хватает данных", e)
            return HttpResponseBadRequest()

        if msg and user_id and room_id:
            db.send_message(msg, room_id, user_id)
            return HttpResponse()

        return HttpResponseServerError()


@api_view(['GET'])
def get_cookie(request, user_id):
    if not is_request_from_user(request):
        return HttpResponseForbidden()

    if request.method == 'GET':
        return Response(db.get_cookie(user_id))


# curl -X POST -v localhost:8000/auth/ -d "{\"login\": \"user\", \"pass\": \"1234\"}" --header "Token: b454a363-a801-4bf0-9ac6-8d8f5af862d8"
@api_view(['POST'])
def auth(request):
    if request.method == 'POST':
        # Проверка токена в хэдере
        if request and request.headers and "Token" in request.headers and is_request_from_user(request):
            json_cookie = json.dumps((request.headers['Token'], None))
            return Response(json_cookie)

        body = json.loads(request.body)
        try:
            login, password = body["login"], body["pass"]
        except Exception as e:
            print("Не хватает данных", e)
            return HttpResponseBadRequest()

        if login and password:
            user = db.get_user_by_login(login)
            print(len(user))
            if user and len(user) > 0 and user[0] and user[0][0]:
                # Если хэш не совпал - ошибка
                if password != user[0][2]:
                    return HttpResponseForbidden()
                user_id = user[0][0]
                cookie = db.get_cookie(user_id)
                # Если куки уже есть в бд и время не вышло -
                # юзер уже автризован, отдать куки и время окончания
                if cookie and cookie[0] and cookie[0][3] > datetime.datetime.now():
                    json_cookie = json.dumps((cookie[0][2], str(cookie[0][3])))
                    return Response(json_cookie)
                # Если куки уже есть в бд и время вышло - удалить куки из бд
                elif cookie and cookie[0] and cookie[0][3] < datetime.datetime.now():
                    db.remove_cookie(user_id)

                # Если куки нет в бд -
                db.set_cookie(user_id)
                cookie = db.get_cookie(user_id)
                json_cookie = json.dumps((cookie[0][2], str(cookie[0][3])))
                return Response(json_cookie)

        return HttpResponseForbidden()


@api_view(['POST'])
def create_room(request):
    if not is_request_from_user(request):
        return HttpResponseForbidden()

    if request.method == 'POST':
        body = json.loads(request.body)
        try:
            room_name = body["room_name"]
        except Exception as e:
            print("Не хватает данных", e)
            return HttpResponseBadRequest()

        if room_name:
            db.create_room(room_name)
            return HttpResponse()

        return HttpResponseServerError()
