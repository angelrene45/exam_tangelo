import hashlib

def encrypt_word(word: str) -> str:
    """
        Method that encrypt the word into sha1
    """
    try:
        # convert string to bytes 
        languages_string_bytes = bytes(word, 'utf-8')
        # convert bytes to sha1
        hash_object = hashlib.sha1(languages_string_bytes)
        # return hexadecimal
        return hash_object.hexdigest()
    except Exception as e:
        msg = f"Error when try to encrypt word \n" \
              f"Word: {word}\n" \
              f"Traceback: {e}"
        print(msg)
        return ''