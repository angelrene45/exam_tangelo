import os
import unittest
import pandas as pd

from ..utils import make_request, process_countries, create_sqllite_from_dataframe, encrypt_word

class TestFunctionsExam(unittest.TestCase):
    """
        Unittest for restcountries api 
    """
    def test_restcountries(self) -> None:
        api = 'https://restcountries.com/v3.1/all'
        response, status_request = make_request(api)
        # check status request
        self.assertTrue(status_request, f"Cant make request with return code: {response.status_code} and api: {api}")
        # check json response 
        json_api = response.json()
        self.assertEqual(type(json_api), list)
        # check json has the keys (name, region and languages)
        country_sample = json_api[0]
        json_keys = set(country_sample.keys())
        mandatory_keys = {'name', 'region', 'languages'}
        # get differences between sets 
        diff = mandatory_keys.difference(json_keys)
        self.assertFalse(diff, f"The following keys are not present in json: {diff}")

    def test_word_encrypt(self) -> None:
        words = ["spanish", "english", "chinese"]
        words_encrypted = ['e3d92827c04e8bd003692ed8189f8467b9e58178', '1b669334dae8ebafa433f0175b5fd418a7bc0975', 'd1a76f90103d1a81842cc458ab2ea94930ee8e53']
        test_encrypted = [encrypt_word(word) for word in words]
        self.assertEqual(words_encrypted, test_encrypted)

    def test_json_to_df(self) -> None:
        api = 'https://restcountries.com/v3.1/all'
        response, _ = make_request(api)

        df = process_countries(response)
        self.assertFalse(df.empty, "The dataframe is empty")

        total_countries = len(response.json())
        total_df = len(df)
        self.assertEqual(total_df, total_countries, f"The total countries '{total_countries}' are not in dataframe '{total_df}' ")

    def test_df_to_sqllite(self) -> None:
        # create dataframe 
        data = [['tom', 10], ['nick', 15], ['juli', 14]]
        df = pd.DataFrame(data, columns=['Name', 'Age'])
        # create sqllite from dataframe
        path_sqlite = "output/test.sqlite"
        name_table = "test"
        is_created = create_sqllite_from_dataframe(path_sqlite, name_table, df)
        self.assertTrue(is_created)
        os.remove(path_sqlite)