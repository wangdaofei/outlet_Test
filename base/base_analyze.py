import os

import yaml


def analyze_file(file_name, key):
    with open(".%sdata%s%s" % (os.sep, os.sep, file_name), "r", encoding="utf-8") as f:
        case_data = yaml.safe_load(f)[key]

        data_list = list()
        for i in case_data.values():
            data_list.append(i)

        return data_list


def analyze_file_test(file_name, key):
    with open(file_name, "r", encoding="utf-8") as f:
        case_data = yaml.safe_load(f)[key]
        print(case_data)
        print(case_data.values())

        data_list = list()
        for i in case_data.values():
            data_list.append(i)

        return data_list


if __name__ == '__main__':
    analyze_file_test("../data/data_test_address.yaml", "test_address")
