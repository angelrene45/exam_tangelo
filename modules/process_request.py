import time
from pandas import DataFrame
from requests.models import Response

from .encrypt_sha1 import encrypt_word
from .convert_time import convert_seconds_into_legible_time

def process_countries(response: Response, encrypt_language: bool=True, delay: int=0) -> DataFrame:
    """
        Method that process reponse json 
        and get the info for every country

        @param response: Instance of Response from requests library
        @param encrypt_language: The column language is encrypted in SHA1 if the flag is True
        @param delay: The method process fast but if you want delay the process you need tu put the seconds

    """
    df = DataFrame([], columns=['Region', 'City Name', 'Language', 'Time'])

    for num, country in enumerate(response.json(), start=0):
        start_time = time.time()
        # get name country
        name = country.get('name', {}).get('common', 'Not available')
        # get region name 
        region = country.get('region', 'Not available')
        # get dictionary from languages
        languages = country.get('languages', {})
        # convert values to string (every language separate by -)
        languages_string = '-'.join(languages.values())
        # encrypt languages
        languages_string_sha1 = encrypt_word(languages_string) if encrypt_language else languages_string
        # simulate take more time for every row
        if delay > 0: time.sleep(delay)
        # get total time processed
        time_process = time.time() - start_time
        # convert time to legible string
        time_legible = convert_seconds_into_legible_time(time_process)
        # create dictionary with new row
        new_row = {
            'Region': region,
            'City Name': name,
            'Language': languages_string_sha1,
            'Time': time_legible
        }
        # append new row into dataframe
        df = df.append(new_row, ignore_index=True)
    return df

def show_statistics(df: DataFrame):
    """
        Show info from dataframe
    """
    # Use str.replace and pass a regex pattern to remove the characters and avoid 'ms' word
    df_time = df['Time'].str.replace(r'[^\d.]','', regex=True).astype(float)
    # show statistics from time in dataframe 
    total_time = df_time.sum()
    mean = df_time.mean()
    min_time = df_time.min()
    max_time = df_time.max()

    msg = f"total time: {total_time} ms \n" \
          f"mean: {mean} ms \n" \
          f"min_time: {min_time} ms \n" \
          f"max_time: {max_time} ms \n"
    print(msg)