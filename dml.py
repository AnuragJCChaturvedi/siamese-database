import psycopg2
import uuid
import json
import os
import io
from PIL import Image

from creds import host, port, dbname, user, password

# Function to load data from a JSON file
def load_data_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Load the data
data = load_data_from_json('data.json')

# Function to connect to the database
def connect_to_database():
    conn = psycopg2.connect(
       dbname=dbname, user=user, password=password, host=host, port=port
    )
    return conn

def convert_image_to_blob(image_path):
    with Image.open(image_path) as image:
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='JPEG')  # Adjust format as needed
        img_byte_arr = img_byte_arr.getvalue()
    return img_byte_arr

# Function to insert user and images data into the database
def update_database(data):
    conn = connect_to_database()
    cur = conn.cursor()

    for item in data:
        user_info = item['users']
        images = item['images']

        # Generate a new UUID for the user
        user_id = str(uuid.uuid1())

        # Insert user data into the users table
        cur.execute("""
            INSERT INTO users (id, firstName, lastName, amount) VALUES (%s, %s, %s, %s)
            """, (user_id, user_info['firstName'], user_info['lastName'], user_info['amount']))

        # Insert image data into the images table
        for image in images:
            image_blob = convert_image_to_blob(os.path.abspath(f"images/{image}"))
            cur.execute("""
                INSERT INTO images (id, userId, rawImage) VALUES (%s, %s, %s)
                """, (str(uuid.uuid1()), user_id, image_blob))  # Assuming rawImage can store image path as text for simplicity

    # Commit the transaction
    conn.commit()
    cur.close()
    conn.close()

# Main function to run the updates
if __name__ == "__main__":
    update_database(data)
