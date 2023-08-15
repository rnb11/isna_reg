import psycopg2
from psycopg2.extras import RealDictCursor

def execute_sql(config, query):
    connection = None
    try:
        connection = psycopg2.connect(**config)
        print("Connected to the database")

        # Create a cursor
        cursor = connection.cursor(cursor_factory=RealDictCursor)

        # Execute SQL queries
        cursor.execute(query)
        rows = cursor.fetchall()

        # Commit changes and close cursor
        connection.commit()
        cursor.close()

        return rows

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL:", error)
    finally:
        # Close the connection
        if connection:
            connection.close()
            print("Database connection closed")