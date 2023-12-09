from sqlalchemy import create_engine, exc, text

DATABASE_NAME = 'Chess_championship'
USERNAME = 'postgres'
PASSWORD = '12312345'
HOST = 'localhost'
PORT = '5432'
DATABASE_URI = f'postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE_NAME}'

def create_database():
    try:
        engine = create_engine(f'postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/postgres', isolation_level="AUTOCOMMIT")
        connection = engine.connect()
        
        connection.execute(text(f"CREATE DATABASE {DATABASE_NAME}"))

        connection.close()

        print(f"Database '{DATABASE_NAME}' was created successfully.")

        engine = create_engine(DATABASE_URI)

    except exc.SQLAlchemyError as err:
        print(f"Error: {err}")

# Avoid unintended execution
if __name__ == "__main__":
    create_database()
