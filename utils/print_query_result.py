from configs.config import str_list


def print_query_result(result, file):
    for i in range(len(result)):
        for j in range(len(result[i])):
            if isinstance(result[i][j], list):
                for k in range(len(result[i][j])):
                    print(f"{str_list[j]}_{k}: {result[i][j][k]}", file=file)
            else:
                print(f"{str_list[j]}: {result[i][j]}", file=file)
        print('\n')
