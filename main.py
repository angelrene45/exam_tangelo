import sys
import os 
import time

from modules import make_request, process_countries, create_sqllite_from_dataframe, show_statistics

if __name__ == '__main__':
    # get start time
    start_time = time.time()

    # get all countries json
    response, status_request = make_request('https://restcountries.com/v3.1/all')
    if not status_request: sys.exit(0)

    # process json and get DataFrame
    df = process_countries(response)
    if df.empty: sys.exit(0)

    # print the time statistics
    show_statistics(df)

    # create sqllite from dataframe
    path_sqlite = "output/countries.sqlite"
    name_table = "countries"
    is_created = create_sqllite_from_dataframe(path_sqlite, name_table, df)
    if not is_created: sys.exit(0)

    # create json and store from dataframe
    path_json = "output/countries.json"
    df.to_json(path_json)
    if not os.path.isfile(path_json): sys.exit(0)

    # calculate time_elapsed
    time_elapsed =  time.time() - start_time
    msg = f"Script executed success \n"\
          f"Time elapsed: {time_elapsed}"
    print(msg)