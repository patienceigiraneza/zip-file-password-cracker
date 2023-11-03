import itertools
import string
import zipfile

def guess_password(zip_file_path):
    chars = string.ascii_letters + string.digits + string.punctuation
    print(chars)

    attempts = 0
    with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
        for password_length in range(1, 24):
            for guess in itertools.product(chars, repeat=password_length):
                attempts += 1
                password = ''.join(guess)
                try:
                    zip_file.extractall(pwd=password.encode('utf-8'))
                    print(f"Successfully extracted {zip_file_path} for the {attempts}'s attempt, password is: {password}")
                    return  True
                except Exception as e:
                    pass

    print(f"Fialed at {attempts}'s attempt.")


zip_file_path = '_path_to_your_zip_file_/file.zip'

guess_password(zip_file_path)
