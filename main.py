from config import *
from arg_parser import arg_parse
from db_queries import build_query
import sqlite3


def main():
    args = arg_parse()

    conn = sqlite3.connect('cve_database.db')
    cursor = conn.cursor()

    query, parameters = build_query(args)

    cursor.execute(query, parameters)
    results = cursor.fetchall()

    for row in results:
        print(row)

    conn.close()


if __name__ == '__main__':
    main()
