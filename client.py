import json
import os

from cryptography.fernet import Fernet
from dotenv import load_dotenv
from websocket import create_connection


def main():
    """
    this will connect to server and send data and encrypt the result fetch the result
    """
    ws = create_connection("ws://localhost:8000/ws/sort")
    load_dotenv()
    cipher_suite = Fernet(str.encode(os.getenv('API_KEY')))
    print("enter string number like this example 1,23,4 ->")
    print("please input :")
    string_data = input(">")
    list_data = string_data.split(",")
    list_data = [int(x) for x in list_data]
    data_dict = {
        "array": list_data
    }
    encoded_text = cipher_suite.encrypt(str.encode(json.dumps(data_dict))).decode("utf-8")
    ws.send(encoded_text)
    result = ws.recv()
    decoded_text = json.loads(cipher_suite.decrypt(str.encode(result)).decode("utf-8"))
    print(decoded_text)


if __name__ == '__main__':
    main()
