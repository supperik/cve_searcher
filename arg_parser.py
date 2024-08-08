import argparse
from configs import config as conf
from utils.redirect_input import redirect_input
from utils.fill_query_dict import fill_query_dict


def arg_parse():
    parser = argparse.ArgumentParser()

    parser.add_argument('--use-config')

    parser.add_argument('--use-output-file', type=str)
    parser.add_argument('--use-input-file', type=str)

    # Arguments for cve
    parser.add_argument('--cve-name', nargs='+', type=str)
    parser.add_argument('--cve-assigner', nargs='+', type=str)
    parser.add_argument('--cve-publish-date')

    # Arguments for cpe
    parser.add_argument('--cpe-uri', nargs='+', type=str)
    parser.add_argument('--cpe-version', nargs='+', type=str)
    parser.add_argument('--cpe-part', nargs='+', type=str)
    parser.add_argument('--cpe-vendor', nargs='+', type=str)
    parser.add_argument('--cpe-product', nargs='+', type=str)
    parser.add_argument('--cpe-product-version', nargs='+', type=str)
    parser.add_argument('--cpe-product-update', nargs='+', type=str)
    parser.add_argument('--cpe-product-edition', nargs='+', type=str)
    parser.add_argument('--cpe-product-language', nargs='+', type=str)
    parser.add_argument('--cpe-sw-edition', nargs='+', type=str)
    parser.add_argument('--cpe-target-sw', nargs='+', type=str)
    parser.add_argument('--cpe-target-hw', nargs='+', type=str)
    parser.add_argument('--cpe-product-other', nargs='+', type=str)

    # Arguments for cwe
    parser.add_argument('--cwe-name', nargs='+', type=str)

    # Arguments for cvss score
    parser.add_argument('--cvssv2-score', nargs='+', type=str)
    parser.add_argument('--cvssv3-score', nargs='+', type=str)

    # Parse arguments
    args = parser.parse_args()
    return args


def process_args(args):
    if args.use_input_file:
        conf.config_dict['use_input_file'] = args.use_input_file

    else:
        fill_query_dict(args.__dict__)
