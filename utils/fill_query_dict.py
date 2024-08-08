from configs.config import query_dict


def fill_query_dict(input_dict):
    print(input_dict)
    if 'cve_name' in input_dict and input_dict['cve_name'] is not None:
        query_dict[';'.join(input_dict['cve_name'])] = ["CVE.CVE_NAME", "CVE Name"]

    if 'cve_assigner' in input_dict and input_dict['cve_assigner'] is not None:
        print('123123')
        query_dict[';'.join(input_dict['cve_assigner'])] = ["CVE.ASSIGNER", "CVE Assigner"]

    if 'cve_publish_date' in input_dict and input_dict['cve_publish_date'] is not None:
        query_dict[';'.join(input_dict['cve_publish_date'])] = ["CVE.CVE_PUBLISH_DATE", "CVE Publish date"]

    if 'cpe_uri' in input_dict and input_dict['cpe_uri'] is not None:
        query_dict[';'.join(input_dict['cpe_uri'])] = ["CPE.CPE_URI", "CPE URI"]

    if 'cpe_part' in input_dict and input_dict['cpe_part'] is not None:
        query_dict[';'.join(input_dict['cpe_part'])] = ["CPE.CPE_PART", "CPE Part"]

    if 'cpe_version' in input_dict and input_dict['cpe_version'] is not None:
        query_dict[';'.join(input_dict['cpe_version'])] = ["CPE.CPE_VERSION", "CPE Version"]

    if 'cpe_vendor' in input_dict and input_dict['cpe_vendor'] is not None:
        query_dict[';'.join(input_dict['cpe_vendor'])] = ["CPE.CPE_VENDOR", "CPE Vendor"]

    if 'cpe_product' in input_dict and input_dict['cpe_product'] is not None:
        query_dict[';'.join(input_dict['cpe_product'])] = ["CPE.CPE_PRODUCT", "CPE Product"]

    if 'cpe_product_version' in input_dict and input_dict['cpe_product_version'] is not None:
        query_dict[';'.join(input_dict['cpe_product_version'])] = ["CPE.CPE_PRODUCT_VERSION", "CPE Product version"]

    if 'cpe_product_update' in input_dict and input_dict['cpe_product_update'] is not None:
        query_dict[';'.join(input_dict['cpe_product_update'])] = ["CVE.CPE_PRODUCT_UPDATE", "CPE Product update"]

    if 'cpe_product_edition' in input_dict and input_dict['cpe_product_edition'] is not None:
        query_dict[';'.join(input_dict['cpe_product_edition'])] = ["CPE.CPE_PRODUCT_EDITION", "CPE Product update"]

    if 'cpe_product_language' in input_dict and input_dict['cpe_product_language'] is not None:
        query_dict[';'.join(input_dict['cpe_product_language'])] = ["CPE.CPE_PRODUCT_LANGUAGE", "CPE Product update"]

    if 'cpe_sw_edition' in input_dict and input_dict['cpe_sw_edition'] is not None:
        query_dict[';'.join(input_dict['cpe_sw_edition'])] = ["CPE.CPE_PRODUCT_PLATFORM", "CPE Product update"]

    if 'cpe_target_sw' in input_dict and input_dict['cpe_target_sw'] is not None:
        query_dict[';'.join(input_dict['cpe_target_sw'])] = ["CPE.CPE_PRODUCT_RUNTIME", "CPE Product update"]

    if 'cpe_target_hw' in input_dict and input_dict['cpe_target_hw'] is not None:
        query_dict[';'.join(input_dict['cpe_target_hw'])] = ["CPE.CPE_PRODUCT_RUNTIME", "CPE Product update"]

    if 'cpe_product_other' in input_dict and input_dict['cpe_product_other'] is not None:
        query_dict[';'.join(input_dict['cpe_product_other'])] = ["CPE.CPE_PRODUCT_OTHER", "CPE Product update"]

    if 'cwe_name' in input_dict and input_dict['cwe_name'] is not None:
        query_dict[';'.join(input_dict['cwe_name'])] = ["CWE.CWE_NAME", "CPE Product update"]

    if 'cvssv3_score' in input_dict and input_dict['cvssv3_score'] is not None:
        query_dict[';'.join(input_dict['cvssv3_score'])] = ["CVSSV3.BASE_SCORE", "CPE Product update"]

    if 'cvssv2_score' in input_dict and input_dict['cvssv2_score'] is not None:
        query_dict[';'.join(input_dict['cvssv2_score'])] = ["CVSSV2.BASE_SCORE", "CPE Product update"]

    if 'use_output_file' in input_dict and input_dict['use_output_file'] is not None:
        config_dict['use_output_file'] = input_dict['use_output_file']
