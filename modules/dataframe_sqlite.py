import sqlite3
import os
from pandas import DataFrame

def create_sqllite_from_dataframe(path_store: str, name_table: str, df: DataFrame) -> bool:
    """
        Method that create a sqlite file from dataframe

        if already exists the table, replace the existing table
    """
    conn = None

    try:
        conn = sqlite3.connect(path_store)
        df.to_sql(name=name_table, con=conn, if_exists="replace")
        conn.close()
    except Exception as e:
        msg = f"Error when try to create a sqlite file\n"\
              f"Traceback: {e}"
        print(msg)
    finally:
        # close connection
        if conn: conn.close()

        # check if path exists
        if os.path.isfile(path_store):
            return True
        else:
            print("Error when try to create sqlite file")
            return False