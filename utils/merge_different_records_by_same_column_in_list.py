def merge_different_records_in_same_column_in_list(query_result: list):
    same_queries_dict = {}
    merged_list = []

    for item in query_result:
        if item[0] not in same_queries_dict:
            same_queries_dict[item[0]] = []
        same_queries_dict[item[0]].append(item)

    for key in same_queries_dict:
        unique_records = {}
        for record in same_queries_dict[key]:
            for idx, value in enumerate(record):
                if idx not in unique_records:
                    unique_records[idx] = value
                elif isinstance(unique_records[idx], list):
                    if value not in unique_records[idx]:
                        unique_records[idx].append(value)
                else:
                    if unique_records[idx] != value:
                        unique_records[idx] = [unique_records[idx], value] if unique_records[idx] is not None else [value]

        merged_record = []
        for idx in range(len(record)):
            merged_record.append(unique_records.get(idx))
        merged_list.append(merged_record)
    return merged_list
