import os
import time

from .utils import make_request, process_countries, create_sqllite_from_dataframe, show_statistics

class TangeloExam:
    """
        Class that run all tasks from exam:
            - Make API request and get json (restcountries)
            - Process Json into DataFrame
            - Show time statistics
            - Create sqlite database from DataFrame
            - Create json from DataFrame
    """
    def start(self) -> bool:
        # get start time
        start_time = time.time()

        # get all countries json
        response, status_request = make_request('https://restcountries.com/v3.1/all')
        if not status_request: return False

        # process json and get DataFrame
        df = process_countries(response)
        if df.empty: return False
        print(df)

        # print the time statistics
        show_statistics(df)

        # create sqllite from dataframe
        path_sqlite = "output/countries.sqlite"
        name_table = "countries"
        is_created = create_sqllite_from_dataframe(path_sqlite, name_table, df)
        if not is_created: return False

        # create json and store from dataframe
        path_json = "output/countries.json"
        df.to_json(path_json)
        if not os.path.isfile(path_json): return False

        # calculate time_elapsed
        time_elapsed =  time.time() - start_time
        msg = f"Script executed success \n"\
            f"Time elapsed: {time_elapsed}"
        print(msg)

        return True

