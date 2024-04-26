# -*- coding: utf-8 -*-
import csv
import pytest

def get_csv_test_data(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        # 跳过标题行
        next(reader)
        data = []
        for row in reader:
            data.append(row)
    return data


if __name__ == '__main__':
    pytest.main([__file__])