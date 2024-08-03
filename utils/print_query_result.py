from configs.config import str_list
import json


def print_query_result(result, file):
    for i in range(len(result)):
        for j in range(len(result[i])):
            if str_list[j] == "CAPEC.RELATED_ATTACK_PATTERN AS CAPEC_RELATED_ATTACK_PATTERN" or str_list[j] == "CAPEC.EXECUTION_FLOW AS CAPEC_EXECUTION_FLOW":
                if isinstance(result[i][j], list):
                    for k in range(len(result[i][j])):
                        if isinstance(result[i][j][k], str) and result[i][j][k] != "None":
                            result[i][j][k] = json.loads(result[i][j][k].replace("'", '"'))
                        print(json.dumps(result[i][j][k], indent=2), file=file)
                continue

            if isinstance(result[i][j], list):
                for k in range(len(result[i][j])):
                    pass
                    print(f"{str_list[j]}_{k}: {result[i][j][k]}", file=file)
                continue

            print(f"{str_list[j]}: {result[i][j]}", file=file)
        print('\n')


def format_capec_related_attack_pattern_output():
    pass