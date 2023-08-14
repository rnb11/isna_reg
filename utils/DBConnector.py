import psycopg2

def execute_sql(self, config, sql_script):
    connection = None
    try:
        connection = psycopg2.connect(**config)
        print("Connected to the database")

        # Create a cursor
        cursor = connection.cursor()

        # Execute SQL queries
        cursor.execute(sql_script)
        rows = cursor.fetchall()

        for row in rows:
            print(row)

        # Commit changes and close cursor
        connection.commit()
        cursor.close()

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL:", error)
    finally:
        # Close the connection
        if connection:
            connection.close()
            print("Database connection closed")