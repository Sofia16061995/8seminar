
from sort import sort, get_da
from viev import get_number_operation, get_data
from input_output import read_file, write_file
from basic import sort_data


def button():
    return sort_data(get_number_operation, read_file, write_file, sort, get_da, get_data)