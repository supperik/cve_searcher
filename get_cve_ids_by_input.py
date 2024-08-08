from configs.config import query_dict
from utils.merge_different_records_in_same_column_in_list import merge_different_records_in_same_column_in_list


def get_cve_id(cursor):
    base_query = """
        SELECT
            CVE.CVE_ID
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
    selected_cols = []

    def add_parameter(arg: str):
        arg = arg.split(';')
        try:
            for item in arg:
                parameters.append(float(item))
        except ValueError:
            for item in arg:
                parameters.append(item)

    def add_condition(arg: str):
        conditions.append(f"{query_dict[arg][0]} IN (" + ",".join(["?"] * len(arg.split(';'))) + ")")

    def add_selected_col(arg: str):
        selected_cols.append(query_dict[arg][1] + ': ')

    for dict_key in query_dict:
        if query_dict[dict_key]:
            add_condition(dict_key)
            add_parameter(dict_key)
            add_selected_col(dict_key)

    if not conditions:
        raise ValueError("Необходимо указать хотя бы один параметр для поиска.")

    query = base_query + " AND ".join(conditions) + " ORDER BY CVE.CVE_ID"

    cursor.execute(query, parameters)

    result = cursor.fetchall()

    merged_results = merge_different_records_in_same_column_in_list(result)
    merged_results = [item[0] for item in merged_results]
    print(merged_results)
    return merged_results
