def build_query(args):
    base_query = """
    SELECT
        CVE.CVE_ID,
        CVE.CVE_NAME,
        CVE.DESCRIPTION,
        CVE.CPES_RELATIONS,
        CVE.ASSIGNER,
        CVE.PUBLISH_DATE,
        CVSSV2.BASE_SCORE AS CVSSV2_BASE_SCORE,
        CVSSV2.VECTOR_STRING AS CVSSV2_VECTOR_STRING,
        CVSSV2.ACCESS_VECTOR AS CVSSV2_ACCESS_VECTOR,
        CVSSV2.ACCESS_COMPLEXITY AS CVSSV2_ACCESS_COMPLEXITY,
        CVSSV2.AUTHENTIFICATION AS CVSSV2_AUTHENTIFICATION,
        CVSSV2.CONFIDENTIALITY_IMPACT AS CVSSV2_CONFIDENTIALITY_IMPACT,
        CVSSV2.INTEGRITY_IMPACT AS CVSSV2_INTEGRITY_IMPACT,
        CVSSV2.AVAILABILITY_IMPACT AS CVSSV2_AVAILABILITY_IMPACT,
        CVSSV2.SEVERITY AS CVSSV2_SEVERITY,
        CVSSV2.EXPLOITABILITY_SCORE AS CVSSV2_EXPLOITABILITY_SCORE,
        CVSSV2.IMPACT_SCORE AS CVSSV2_IMPACT_SCORE,
        CVSSV2.OBTAIN_ALL_PRIVILEGE AS CVSSV2_OBTAIN_ALL_PRIVILEGE,
        CVSSV2.OBTAIN_USER_PRIVILEGE AS CVSSV2_OBTAIN_USER_PRIVILEGE,
        CVSSV2.OBTAIN_OTHER_PRIVILEGE AS CVSSV2_OBTAIN_OTHER_PRIVILEGE,
        CVSSV2.USER_INTERACTION_REQUIRED AS CVSSV2_USER_INTERACTION_REQUIRED,
        CVSSV3.VECTOR_STRING AS CVSSV3_VECTOR_STRING,
        CVSSV3.ATTACK_VECTOR AS CVSSV3_ATTACK_VECTOR,
        CVSSV3.ATTACK_COMPLEXITY AS CVSSV3_ATTACK_COMPLEXITY,
        CVSSV3.PRIVILEGES_REQUIRED AS CVSSV3_PRIVILEGES_REQUIRED,
        CVSSV3.USER_INTERACTION AS CVSSV3_USER_INTERACTION,
        CVSSV3.SCOPE AS CVSSV3_SCOPE,
        CVSSV3.CONFIDENTIALITY_IMPACT AS CVSSV3_CONFIDENTIALITY_IMPACT,
        CVSSV3.INTEGRITY_IMPACT AS CVSSV3_INTEGRITY_IMPACT,
        CVSSV3.AVAILABILITY_IMPACT AS CVSSV3_AVAILABILITY_IMPACT,
        CVSSV3.BASE_SCORE AS CVSSV3_BASE_SCORE,
        CVSSV3.BASE_SEVERITY AS CVSSV3_BASE_SEVERITY,
        CVSSV3.IMPACT_SCORE AS CVSSV3_IMPACT_SCORE,
        CVSSV3.EXPLOITABILITY_SCORE AS CVSSV3_EXPLOITABILITY_SCORE,
        REFERENCE.URL AS REFERENCE_URL,
        REFERENCE.NAME AS REFERENCE_NAME,
        CPE.CPE_URI AS CPE_URI,
        CPE.CPE_VERSION AS CPE_VERSION,
        CPE.CPE_PART AS CPE_PART,
        CPE.CPE_VENDOR AS CPE_VENDOR,
        CPE.CPE_PRODUCT AS CPE_PRODUCT,
        CPE.CPE_PRODUCT_VERSION AS CPE_PRODUCT_VERSION,
        CPE.CPE_PRODUCT_UPDATE AS CPE_PRODUCT_UPDATE,
        CPE.CPE_PRODUCT_EDITION AS CPE_PRODUCT_EDITION,
        CPE.CPE_PRODUCT_LANGUAGE AS CPE_PRODUCT_LANGUAGE,
        CPE.CPE_PRODUCT_PLATFORM AS CPE_PRODUCT_PLATFORM,
        CPE.CPE_PRODUCT_RUNTIME AS CPE_PRODUCT_RUNTIME,
        CPE.CPE_PRODUCT_OTHER AS CPE_PRODUCT_OTHER,
        CWE.CWE_NAME AS CWE_NAME,
        CWE.DESCRIPTION AS CWE_DESCRIPTION,
        CAPEC.CAPEC_NAME AS CAPEC_NAME,
        CAPEC.ABSTRACTION AS CAPEC_ABSTRACTION,
        CAPEC.STATUS AS CAPEC_STATUS,
        CAPEC.DECRIPTION AS CAPEC_DESCRIPTION,
        CAPEC.LIKELIHOOD AS CAPEC_LIKELIHOOD,
        CAPEC.RELATED_ATTACK_PATTERN AS CAPEC_RELATED_ATTACK_PATTERN,
        CAPEC.EXECUTION_FLOW AS CAPEC_EXECUTION_FLOW,
        CAPEC.PREREQUISITES AS CAPEC_PREREQUISITES,
        CAPEC.SKILL AS CAPEC_SKILL,
        CAPEC.RESOURCE_REQUIRED AS CAPEC_RESOURCE_REQUIRED,
        CAPEC.CONSEQUENCES AS CAPEC_CONSEQUENCES,
        CAPEC.MITIGATIONS AS CAPEC_MITIGATIONS,
        CAPEC.EXAMPLE_INSTANCES AS CAPEC_EXAMPLE_INSTANCES
    FROM
        CVE
        LEFT JOIN CVSSV2 ON CVE.CVSSV2_ID = CVSSV2.CVSSV2_ID
        LEFT JOIN CVSSV3 ON CVE.CVSSV3_ID = CVSSV3.CVSSV3_ID
        LEFT JOIN CVE_has_REFERENCE ON CVE.CVE_ID = CVE_has_REFERENCE.CVE_ID
        LEFT JOIN REFERENCE ON CVE_has_REFERENCE.REFERENCE_ID = REFERENCE.REFERENCE_ID
        LEFT JOIN CVE_has_CPE_GROUP ON CVE.CVE_ID = CVE_has_CPE_GROUP.CVE_ID
        LEFT JOIN CPE_GROUP_has_CPE ON CVE_has_CPE_GROUP.CPE_GROUP_ID = CPE_GROUP_has_CPE.CPE_GROUP_ID
        LEFT JOIN CPE ON CPE_GROUP_has_CPE.CPE_ID = CPE.CPE_ID
        LEFT JOIN CVE_has_CWE ON CVE.CVE_ID = CVE_has_CWE.CVE_ID
        LEFT JOIN CWE ON CVE_has_CWE.CWE_ID = CWE.CWE_ID
        LEFT JOIN CAPEC_has_CWE ON CWE.CWE_ID = CAPEC_has_CWE.CWE_ID
        LEFT JOIN CAPEC ON CAPEC_has_CWE.CAPEC_ID = CAPEC.CAPEC_ID
    WHERE
    """

    conditions = []
    parameters = []

    if args.cve_name:
        conditions.append("CVE.CVE_NAME = ?")
        parameters.append(args.cve_name)
    if args.cve_assigner:
        conditions.append("CVE.ASSIGNER = ?")
        parameters.append(args.cve_assigner)
    if args.cve_publish_date:
        conditions.append("CVE.PUBLISH_DATE = ?")
        parameters.append(args.cve_publish_date)
    if args.cve_publish_date_year:
        conditions.append("strftime('%Y', CVE.PUBLISH_DATE) = ?")
        parameters.append(args.cve_publish_date_year)
    if args.cve_publish_date_month:
        conditions.append("strftime('%m', CVE.PUBLISH_DATE) = ?")
        parameters.append(args.cve_publish_date_month)
    if args.cve_publish_date_day:
        conditions.append("strftime('%d', CVE.PUBLISH_DATE) = ?")
        parameters.append(args.cve_publish_date_day)
    if args.cpe_uri:
        conditions.append("CPE.CPE_URI = ?")
        parameters.append(args.cpe_uri)
    if args.cpe_version:
        conditions.append("CPE.CPE_VERSION = ?")
        parameters.append(args.cpe_version)
    if args.cpe_part:
        conditions.append("CPE.CPE_PART = ?")
        parameters.append(args.cpe_part)
    if args.cpe_vendor:
        conditions.append("CPE.CPE_VENDOR = ?")
        parameters.append(args.cpe_vendor)
    if args.cpe_product:
        conditions.append("CPE.CPE_PRODUCT = ?")
        parameters.append(args.cpe_product)
    if args.cpe_product_version:
        conditions.append("CPE.CPE_PRODUCT_VERSION = ?")
        parameters.append(args.cpe_product_version)
    if args.cpe_product_update:
        conditions.append("CPE.CPE_PRODUCT_UPDATE = ?")
        parameters.append(args.cpe_product_update)
    if args.cpe_product_edition:
        conditions.append("CPE.CPE_PRODUCT_EDITION = ?")
        parameters.append(args.cpe_product_edition)
    if args.cpe_product_language:
        conditions.append("CPE.CPE_PRODUCT_LANGUAGE = ?")
        parameters.append(args.cpe_product_language)
    if args.cpe_product_platform:
        conditions.append("CPE.CPE_PRODUCT_PLATFORM = ?")
        parameters.append(args.cpe_product_platform)
    if args.cpe_product_runtime:
        conditions.append("CPE.CPE_PRODUCT_RUNTIME = ?")
        parameters.append(args.cpe_product_runtime)
    if args.cpe_product_other:
        conditions.append("CPE.CPE_PRODUCT_OTHER = ?")
        parameters.append(args.cpe_product_other)
    if args.cwe_name:
        conditions.append("CWE.CWE_NAME = ?")
        parameters.append(args.cwe_name)
    if args.cvssv2_score:
        conditions.append("CVSSV2.BASE_SCORE = ?")
        parameters.append(args.cvssv2_score)
    if args.cvssv3_score:
        conditions.append("CVSSV3.BASE_SCORE = ?")
        parameters.append(args.cvssv3_score)

    if not conditions:
        raise ValueError("Необходимо указать хотя бы один параметр для поиска.")

    query = base_query + " AND ".join(conditions)
    return query, parameters
