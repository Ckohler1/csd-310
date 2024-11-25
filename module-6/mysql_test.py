import mysql.connector
from mysql.connector import Error

# Database configuration
config = {
    'user': 'root',
    'password': 'SugHei297A!',
    'host': '127.0.0.1',
    'database': 'movies', 
    "raise_on_warnings": True
}

try:
    # Attempt to connect to the MySQL server
    db = mysql.connector.connect(**config)
    
    # If the connection is successful
    print("\nDatabase user {} connected to MySQL on host {} with database {}"
          .format(config["user"], config["host"], config["database"]))

    input("\n\nPress any key to continue...")

except mysql.connector.Error as err:
    # Handle specific MySQL errors
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)

finally:
    # Close the connection if it was successfully made
    if 'db' in locals() and db.is_connected():
        db.close()
        print("\nMySQL connection is closed")
