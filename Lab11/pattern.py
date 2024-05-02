import psycopg2
import os
import math
def search_records(pattern):
    try:
        conn = psycopg2.connect(
            host="localhost",
            dbname="PhoneBook",  
            user="postgres",
            password="808",
            port=5432
        )
        cur = conn.cursor()
        
        query = "SELECT * FROM contacts WHERE first_name ILIKE %s OR second_name ILIKE %s OR phone LIKE %s"
        cur.execute(query, ('%' + pattern + '%', '%' + pattern + '%', '%' + pattern + '%'))
        
        rows = cur.fetchall()
        
        cur.close()
        conn.close()
        
        return rows
    except Exception as e:
        print("SOS 404 ...---... ERROR:", e)

pattern = input("Pattern: ")
matching_records = search_records(pattern)
if matching_records:
    for record in matching_records:
        print(record)
else:
    print("I have sad news... there is no such records(((")