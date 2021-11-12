from django.db import connection


def raw(username, password):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT username FROM users WHERE username = '" + username + "' AND password = '" + password + "'")
        row = cursor.fetchone()

    return row
