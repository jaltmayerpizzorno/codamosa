# Automatically generated by Pynguin.
import argparse as module_0
import requests.models as module_1
import httpie.core as module_2
import httpie.context as module_3

def test_case_0():
    try:
        namespace_0 = module_0.Namespace()
        prepared_request_0 = module_1.PreparedRequest()
        tuple_0 = module_2.get_output_options(namespace_0, prepared_request_0)
    except BaseException:
        pass

def test_case_1():
    try:
        namespace_0 = module_0.Namespace()
        environment_0 = module_3.Environment()
        exit_status_0 = module_2.program(namespace_0, environment_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'httpie'
        str_1 = '--debug'
        str_2 = [str_0, str_1]
        exit_status_0 = module_2.main(str_2)
        bytes_0 = b''
        bytes_1 = b'|E\xab\x14'
        list_0 = [str_2, str_1, bytes_0, bytes_1]
        list_1 = module_2.decode_raw_args(list_0, str_2)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'https://httpbin.org/get'
        str_1 = [str_0, str_0, str_0]
        environment_0 = module_3.Environment()
        var_0 = environment_0.__repr__()
        var_1 = module_2.print_debug_info(environment_0)
        exit_status_0 = module_2.main(str_1)
        list_0 = [var_0, var_0]
        exit_status_1 = module_2.main(list_0)
        list_1 = [var_0, exit_status_0, exit_status_0, list_0]
        exit_status_2 = module_2.main(list_1)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'http'
        str_1 = '-v'
        str_2 = '-H'
        str_3 = 'Tccept:appliation/jl$n'
        str_4 = 'http://httpbin.org/get'
        str_5 = [str_0, str_1, str_2, str_3, str_4, str_0]
        environment_0 = module_3.Environment()
        exit_status_0 = module_2.program(str_5, environment_0)
    except BaseException:
        pass