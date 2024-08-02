import argparse
from configs import config as conf


def arg_parse():
    parser = argparse.ArgumentParser()

    parser.add_argument('--use-config')

    parser.add_argument('--use-output-file', type=str)

    # Arguments for cve
    parser.add_argument('--cve-name', nargs='+', type=str)
    parser.add_argument('--cve-assigner', nargs='+', type=str)
    parser.add_argument('--cve-publish-date')

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
    parser.add_argument('--cvssv2-score', nargs='+', type=str)
    parser.add_argument('--cvssv3-score')

    # Parse arguments
    args = parser.parse_args()

    if args.cve_name:
        conf.query_dict[';'.join(args.cve_name)] = ["CVE.CVE_NAME", "CVE Name"]

    if args.cve_assigner:
        conf.query_dict[';'.join(args.cve_assigner)] = ["CVE.ASSIGNER", "CVE Assigner"]

    if args.cve_publish_date:
        conf.query_dict[';'.join(args.cve_publish_date)] = ["CVE.CVE_PUBLISH_DATE", "CVE Publish date"]

    if args.cpe_uri:
        conf.query_dict[';'.join(args.cpe_uri)] = ["CPE.CPE_URI", "CPE URI"]

    if args.cpe_part:
        conf.query_dict[';'.join(args.cpe_part)] = ["CPE.CPE_PART", "CPE Part"]

    if args.cpe_version:
        conf.query_dict[';'.join(args.cpe_version)] = ["CPE.CPE_VERSION", "CPE Version"]

    if args.cpe_vendor:
        conf.query_dict[';'.join(args.cpe_vendor)] = ["CPE.CPE_VENDOR", "CPE Vendor"]

    if args.cpe_product:
        conf.query_dict[';'.join(args.cpe_product)] = ["CPE.CPE_PRODUCT", "CPE Product"]

    if args.cpe_product_version:
        conf.query_dict[';'.join(args.cpe_product_version)] = ["CPE.CPE_PRODUCT_VERSION", "CPE Product version"]

    if args.cpe_product_update:
        conf.query_dict[';'.join(args.cpe_product_update)] = ["CVE.CPE_PRODUCT_UPDATE", "CPE Product update"]

    if args.cpe_product_edition:
        conf.query_dict[';'.join(args.cpe_product_edition)] = ["CPE.CPE_PRODUCT_EDITION", "CPE Product update"]

    if args.cpe_product_language:
        conf.query_dict[';'.join(args.cpe_product_language)] = ["CPE.CPE_PRODUCT_LANGUAGE", "CPE Product update"]

    if args.cpe_product_platform:
        conf.query_dict[';'.join(args.cpe_product_platform)] = ["CPE.CPE_PRODUCT_PLATFORM", "CPE Product update"]

    if args.cpe_product_runtime:
        conf.query_dict[';'.join(args.cpe_product_runtime)] = ["CPE.CPE_PRODUCT_RUNTIME", "CPE Product update"]

    if args.cpe_product_other:
        conf.query_dict[';'.join(args.cpe_product_other)] = ["CPE.CPE_PRODUCT_OTHER", "CPE Product update"]

    if args.cwe_name:
        conf.query_dict[';'.join(args.cwe_name)] = ["CWE.CWE_NAME", "CPE Product update"]

    if args.cvssv3_score:
        conf.query_dict[';'.join(args.cvssv3_score)] = ["CVSSV3.BASE_SCORE", "CPE Product update"]

    if args.cvssv2_score:
        conf.query_dict[';'.join(args.cvssv2_score)] = ["CVSSV2.BASE_SCORE", "CPE Product update"]

    if args.use_output_file:
        conf.config_dict['use_output_file'] = args.use_output_file

    return args
