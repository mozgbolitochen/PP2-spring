import psycopg2
import os
import math
def delete(name=None, phone=None):
    try:
        conn = psycopg2.connect(
            host="localhost",
            dbname="PhoneBook", 
            user="postgres",
            password='808',
            port=5432
        )
        cur = conn.cursor()
        
        if name:
            cur.execute("DELETE FROM contacts WHERE first_name ILIKE %s", (name,))
        elif phone:
            cur.execute("DELETE FROM contacts WHERE phone = %s", (phone,))
        
        conn.commit()
        cur.close()
        conn.close()
        
        print(f"{name} have been wiped off the world")
        print(f"{phone}'s owner have been vanished")
    except Exception as e:
        print("SOS 404 ...---... ERROR:", e)

#delete(name="John")

#delete(phone="1234567890")