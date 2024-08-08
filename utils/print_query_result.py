from configs.config import str_list
import pprint
import json


def print_query_result(result, file):
    for i in range(len(result)):
        for j in range(len(result[i])):
            # print('-' * 40)
            if (str_list[j] == "CAPEC.RELATED_ATTACK_PATTERN AS CAPEC_RELATED_ATTACK_PATTERN" or
                    str_list[j] == "CAPEC.EXECUTION_FLOW AS CAPEC_EXECUTION_FLOW" or
                    str_list[j] == "CAPEC.PREREQUISITES AS CAPEC_PREREQUISITES" or
                    str_list[j] == "CAPEC.EXAMPLE_INSTANCES AS CAPEC_EXAMPLE_INSTANCES" or
                    str_list[j] == "CAPEC.SKILL AS CAPEC_SKILL" or
                    str_list[j] == "CAPEC.CONSEQUENCES AS CAPEC_CONSEQUENCES" or
                    str_list[j] == "CAPEC.MITIGATIONS AS CAPEC_MITIGATIONS"):
                if isinstance(result[i][j], list):
                    for k in range(len(result[i][j])):
                        if isinstance(result[i][j][k], str) and result[i][j][k] != "None":
                            result[i][j][k] = json.loads(result[i][j][k])

                        print('-' * 40, file=file)
                        print(f"{str_list[j]}_{k + 1}: ", end='\n', file=file)
                        pprint.pprint(result[i][j][k], stream=file)
                continue

            if isinstance(result[i][j], list):
                for k in range(len(result[i][j])):
                    print('-' * 40, file=file)
                    print(f"{str_list[j]}_{k + 1}: {result[i][j][k]}", file=file)
                continue

            print('-' * 40, file=file)
            print(f"{str_list[j]}: {result[i][j]}", file=file)
        print('-' * 40, file=file)
        print('\n', file=file)
    file.close()


def format_capec_related_attack_pattern_output():
    pass