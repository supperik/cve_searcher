use_config = ''

cve_name = ''
cve_assigner = ''
cve_publish_date = ''
cve_publish_date_year = ''
cve_publish_date_month = ''
cve_publish_date_day = ''

cpe_uri = ''
cpe_version = ''
cpe_part = ''
cpe_vendor = ''
cpe_product = ''
cpe_product_version = ''
cpe_product_update = ''
cpe_product_edition = ''
cpe_product_language = ''
cpe_product_platform = ''
cpe_product_runtime = ''
cpe_product_other = ''

cwe_name = ''

cvssv2_score = ''
cvssv3_score = ''

dict_config = dict()

# Чтобы добавлять в запрос все заголовки, которые не даны изначально
CVE_DB_TABLE_LABELS = ['CVE_NAME', 'DESCRIPTION', 'CPE_IDS', 'CPES_RELATIONS', 'REFERENCE_IDS', 'CWE_IDS', 'ASSIGNER',
                       'CVSSV2_IDS', 'CVSSV3_IDS', 'PUBLISH_DATE']

CPE_DB_TABLE_LABELS = ['CPE_URI', 'CPE_VERSION', 'CPE_PART', 'CPE_VENDOR', 'CPE_PRODUCT', 'CPE_PRODUCT_VERSION',
                       'CPE_PRODUCT_EDITION', 'CPE_PRODUCT_LANGUAGE', 'CPE_PRODUCT_PLATFORM', 'CPE_PRODUCT_RUNTIME',
                       'CPE_PRODUCT_OTHER']

CVE_REFERENCE_TABLE_DB_LABELS = ['URL', 'NAME']

CWE_DB_TABLE_LABELS = ['CWE_NAME', 'DESCRIPTION', 'CAPEC_IDS']

CVSSV2_DB_TABLE_LABELS = ['BASE_SCORE', 'VECTOR_STRING', 'ACCESS_VECTOR', 'ACCESS_COMPLEXITY', 'AUTHENTICATION',
                          'CONFIDENTIALITY_IMPACT', 'INTEGRITY_IMPACT', 'AVAILABILITY_IMPACT', 'SEVERITY',
                          'EXPLOITABILITY_SCORE', 'IMPACT_SCORE', 'OBTAIN_ALL_PRIVILEGE', 'OBTAIN_USER_PRIVILEGE',
                          'OBTAIN_OTHER_PRIVILEGE', 'USER_INTERACTION_REQUIRED']

CVSSV3_DB_TABLE_LABELS = ['VECTOR_STRING', 'ACCESS_VECTOR', 'ACCESS_COMPLEXITY', 'PRIVILEGE_REQUIRED',
                          'USER_INTERACTIONS', 'SCOPE', 'CONFIDENTIALITY_IMPACT', 'INTEGRITY_IMPACT',
                          'AVAILABILITY_IMPACT', 'BASE_SCORE', 'BASE_SEVERITY', 'IMPACT_SCORE', 'EXPLOITABILITY_SCORE']

CAPEC_DB_TABLE_LABELS = ['CAPEC_NAME', 'ABSTRACTION', 'STATUS', 'DESCRIPTION', 'LIKELIHOOD',
                         'RELATED_ATTACK_PATTERN_NATURE', 'RELATED_ATTACK_PATTERN_CAPEC_IDS',
                         'EXECUTION_FLOW_FOR_CAPEC', 'PREREQUISITES', 'SKILL_LEVEL', 'SKILL_TEXT', 'RESOURCE_REQUIRED',
                         'CONSEQUENCES', 'CONSEQUENCES_IMPACT', 'MITIGATIONS', 'EXAMPLE_INSTANCES']

EXECUTION_FLOW_DB_TABLE_LABELS = ['EXECUTION_FLOW_ID_FOR_CAPEC', 'STEP', 'PHASE', 'DESCRIPTION', 'TECHNIQUE']
