import pprint
import sqlite3

from utils.redirect_output import redirect_output
from utils.redirect_input import redirect_input
from utils.print_query_result import print_query_result
from utils.get_database_path import get_db_path
from utils.merge_different_records_by_same_column_in_list import merge_different_records_in_same_column_in_list
from arg_parser import arg_parse, process_args
from db_queries import build_query
from configs.config import database_name
from get_cve_ids_by_input import get_cve_id


def main():
    args = arg_parse()
    process_args(args)

    conn = sqlite3.connect(get_db_path(__file__))
    cursor = conn.cursor()

    redirect_input()
    cve_id_list = get_cve_id(cursor)

    build_query(cursor, cve_id_list)

    merged_results = merge_different_records_in_same_column_in_list(list(set(cursor.fetchall())))
    merged_results.sort(key=lambda i: i[1])

    output_file = redirect_output()
    print_query_result(merged_results, output_file)

    conn.close()


if __name__ == '__main__':
    main()
