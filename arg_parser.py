import argparse
import config as conf


def arg_parse():
    parser = argparse.ArgumentParser()

    parser.add_argument('--use-config')

    # Arguments for cve
    parser.add_argument('--cve-name')
    parser.add_argument('--cve-assigner')
    parser.add_argument('--cve-publish-date')
    parser.add_argument('--cve-publish-date-year')
    parser.add_argument('--cve-publish-date-month')
    parser.add_argument('--cve-publish-date-day')

    # Arguments for cpe
    parser.add_argument('--cpe-uri')
    parser.add_argument('--cpe-version')
    parser.add_argument('--cpe-part')
    parser.add_argument('--cpe-vendor')
    parser.add_argument('--cpe-product')
    parser.add_argument('--cpe-product-version')
    parser.add_argument('--cpe-product-update')
    parser.add_argument('--cpe-product-edition')
    parser.add_argument('--cpe-product-language')
    parser.add_argument('--cpe-product-platform')
    parser.add_argument('--cpe-product-runtime')
    parser.add_argument('--cpe-product-other')

    # Arguments for cwe
    parser.add_argument('--cwe-name')

    # Arguments for cvss score
    parser.add_argument('--cvssv2-score')
    parser.add_argument('--cvssv3-score')

    # Parse arguments
    args = parser.parse_args()

    return args
