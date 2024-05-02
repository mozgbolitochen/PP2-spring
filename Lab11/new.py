import psycopg2
import os
import math


def ussr(username, phone):
    try:
        conn = psycopg2.connect(
            host="localhost",
            dbname="phones",
            user="postgres",
            password='808',
            port=5432
        )
        cur = conn.cursor()

        cur.execute("SELECT * FROM contacts WHERE username = %s", (username,))
        user = cur.fetchone()

        if user:
            cur.execute("UPDATE contacts SET phone = %s WHERE username = %s", (phone, username))
            conn.commit()
            print(f"{username}'s phone updated to:{phone}")
        else:
            cur.execute("INSERT INTO contacts (username, phone) VALUES (%s, %s)", (username, phone))
            conn.commit()
            print(f"{username} added with phone {phone}")

        conn.close()
    except Exception as e:
        print("SOS 404 ...---... ERROR:", e)


username = input("Name: ")
new_phone = input("Phone: ")

ussr(username, new_phone)