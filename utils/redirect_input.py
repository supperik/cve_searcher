from configs.config import config_dict, query_dict
import json
from utils.fill_query_dict import fill_query_dict


def redirect_input():
    if 'use_input_file' in config_dict:

        if config_dict['use_input_file'].split('.')[1] == 'json':
            with open(config_dict['use_input_file'], 'r') as input_file:
                read_input_json_file(input_file)
        else:
            print('Входной файл с данными должен иметь только формат Json')


def read_input_json_file(file):
    input_dict = json.load(file)

    fill_query_dict(input_dict)
