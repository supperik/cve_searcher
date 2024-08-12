import os
import inspect

from configs.config import config_dict, database_name


def get_db_path(execution_file):
    db_file_path = f'{get_execution_file_dir(execution_file)}\\\\{database_name}'

    if 'db_path' in config_dict:
        db_file_path = config_dict['db_path']

    return db_file_path


def get_execution_file_dir(file):
    return os.path.dirname(file)



