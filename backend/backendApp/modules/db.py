import datetime

import psycopg2

# Update connection string information

host = "localhost"
dbname = "postgres"
user = "postgres"
password = "qwerty"


def set_con():
    conn_string = "host={0} user={1} dbname={2} password={3}".format(host, user, dbname, password)
    conn = psycopg2.connect(conn_string)
    print("Connection established")
    return conn


def init_db():
    return


def get_users():
    conn = set_con()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM ilstudio.users;")
    data = cursor.fetchall()

    cursor.close()
    conn.close()
    return data


def get_user_by_login(username):
    username = str(username)
    conn = set_con()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM ilstudio.users WHERE username = %s;", (username,))
    data = cursor.fetchall()

    cursor.close()
    conn.close()
    return data


def get_rooms():
    conn = set_con()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM ilstudio.rooms;")
    data = cursor.fetchall()

    cursor.close()
    conn.close()
    return data


def get_messages(room_id):
    conn = set_con()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM ilstudio.messages WHERE room_id = %s;", (str(room_id),))
    data = cursor.fetchall()

    cursor.close()
    conn.close()
    return data


def get_cookie(user_id):
    conn = set_con()
    cursor = conn.cursor()

    cursor.execute("SELECT token, kill_time, user_id FROM ilstudio.cookie WHERE user_id = %s;", (str(user_id),))
    data = cursor.fetchall()

    cursor.close()
    conn.close()
    return data


def get_cookie_by_token(token):
    conn = set_con()
    cursor = conn.cursor()

    cursor.execute("SELECT token, kill_time, user_id FROM ilstudio.cookie WHERE token = %s;", (str(token),))
    data = cursor.fetchall()

    cursor.close()
    conn.close()
    return data


def isTokenExist(token):
    conn = set_con()
    cursor = conn.cursor()

    try:
        # cursor.execute("SELECT EXISTS(SELECT 1 FROM ilstudio.cookie where token = %s AND kill_time > now()::timestamp);", (str(token),))
        cursor.execute("SELECT EXISTS(SELECT 1 FROM ilstudio.cookie where token = %s);", (str(token),))
        data = cursor.fetchall()
    except Exception as e:
        print(e)
        raise Exception("token is not uuid")
    finally:
        cursor.close()
        conn.close()

    return data


def remove_cookie(user_id):
    conn = set_con()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM ilstudio.cookie WHERE user_id = %s;", (str(user_id),))

    conn.commit()
    cursor.close()
    conn.close()
    return True


def set_cookie(user_id):
    conn = set_con()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO ilstudio.cookie (user_id, kill_time) VALUES(%s, %s)",
                   (str(user_id), datetime.datetime.now() + datetime.timedelta(days=10)))
    conn.commit()
    cursor.close()
    conn.close()


def send_message(msg, user_id, room_id):
    conn = set_con()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO ilstudio.messages (room_id, user_id, msg, date) VALUES(%s, %s, %s, %s)",
                   (str(room_id), str(user_id), str(msg), datetime.datetime.now()))
    conn.commit()
    cursor.close()
    conn.close()


def create_room(room_name):
    conn = set_con()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO ilstudio.rooms (name) VALUES (%s)", (str(room_name),))

    conn.commit()
    cursor.close()
    conn.close()