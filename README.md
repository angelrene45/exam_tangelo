# Tangelo Technical Test

Instructions:

- Make API request and get json (restcountries)
- Process Json into DataFrame
- Show time statistics
- Create sqlite database from DataFrame
- Create json from DataFrame

## Setup
Install the librarys that exam needs
```
    pip install -r requirements.txt
```

## Execute Script
You can execute the script directly by main.py
```
    python main.py
```

## Notebook
Or you can use the notebook called main.ipynb
```
    [Notebook](https://github.com/angelrene45/exam_tangelo/blob/'main'/main.ipynb)
```

## Unittest
You can execute all unittest with following command
```
    python -m unittest
```
You can execute every single unittest separately
```
    python -m unittest modules.test.test_functions.TestFunctionsExam.test_restcountries
    python -m unittest modules.test.test_functions.TestFunctionsExam.test_word_encrypt
    python -m unittest modules.test.test_functions.TestFunctionsExam.test_json_to_df
    python -m unittest modules.test.test_functions.TestFunctionsExam.test_df_to_sqllite
```
