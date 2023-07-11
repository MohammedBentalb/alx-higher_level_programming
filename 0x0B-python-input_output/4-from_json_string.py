#!/usr/bin/python3
"""display a json"""
import json


def from_json_string(my_str):
    """return the json as obj"""
    return json.loads(my_str)
