import sys
from configs.config import config_dict


def redirect_output():
    if 'use_output_file' in config_dict:
        output_file = open(f"{config_dict['use_output_file']}.txt", 'w')
    else:
        output_file = sys.stdout

    return output_file
