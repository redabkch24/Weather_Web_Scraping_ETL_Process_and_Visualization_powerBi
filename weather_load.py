import pandas as pd
import psycopg2


def load_function(df):
    #
    host = 'localhost'
    user = 'postgres'
    password = '0000'  
    port = '5432'
    db_name = 'db_weather'
    
    # Add a index column
    df.index = range(1, len(df) + 1)

    conn = None
    cursor = None

    try:
        # Connexion
        conn = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            port=port,
            database=db_name
        )
        cursor = conn.cursor()

        # removing table if exists and create another one
        cursor.execute("DROP TABLE IF EXISTS weather_data")
        cursor.execute("""CREATE TABLE weather_data (
            Id SERIAL PRIMARY KEY,
            Date DATE,
            High_temp FLOAT,
            Low_temp FLOAT,
            Precip FLOAT
        )""")
        
        # Insertion into postgresDB
        for i, row in df.iterrows():
            cursor.execute("""
                INSERT INTO weather_data (Date, High_temp, Low_temp, Precip)
                VALUES (%s, %s, %s, %s)
            """, (row['Date'], row['High temp'], row['Low temp'], row['Precip']))

        # Validation
        conn.commit()
        print("Données chargées avec succès.")

    except Exception as e:
        print("Erreur lors du chargement des données :", e)

    finally:
        # close cursor and connexion if there are open
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    pass