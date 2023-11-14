# 6.
import os

values = {
    "num_users": 100
}

paths = {
    "read_path": "https://randomuser.me/api/?results=",
    "write_path": os.path.dirname(os.path.realpath(__file__)) + "/processed_data"
}