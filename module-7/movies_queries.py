import mysql.connector
from mysql.connector import Error

# Database configuration
config = {
    'user': 'root',  # Replace with your MySQL username
    'password': 'SugHei297A!',  # Replace with your MySQL password
    'host': '127.0.0.1',  # Replace with your MySQL host
    'database': 'movies',  # Replace with your database name
    "raise_on_warnings": True
}

try:
    # Connect to the database
    connection = mysql.connector.connect(**config)
    if connection.is_connected():
        print("Connected to the database")
        cursor = connection.cursor()

        # Query 1: Select all fields from the studio table
        cursor.execute("SELECT * FROM studio")
        studios = cursor.fetchall()
        print("\n-- DISPLAYING Studio RECORDS --")
        for row in studios:
            print(f"\nStudio ID: {row[0]}")
            print(f"Studio Name: {row[1]}")

        # Query 2: Select all fields from the genre table
        cursor.execute("SELECT * FROM genre")
        genres = cursor.fetchall()
        print("\n-- DISPLAYING Genre RECORDS --")
        for row in genres:
            print(f"\nGenre ID: {row[0]}")
            print(f"Genre Name: {row[1]}")

        # Query 3: Select film names with film runtime less than 2 hours
        cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
        short_films = cursor.fetchall()
        print("\n-- DISPLAYING Short Film RECORDS --")
        for film in short_films:
            print(f"\nFilm Name: {film[0]}")
            print(f"Runtime: {film[1]}")

        # Query 4: List film names and film directors grouped by film director
        cursor.execute("""
            SELECT film_name, film_director
            FROM film
            ORDER BY film_director, film_name
        """)
        director_records = cursor.fetchall()
        print("\n-- DISPLAYING Director RECORDS in Order --")
        for record in director_records:
            print(f"\nFilm Name: {record[0]}")
            print(f"Director: {record[1]}")

except Error as e:
    print(f"Error: {e}")
finally:
    # Close the cursor and connection
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection closed")
