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
        int_0 = 1
        exit_status_0 = module_2.program(int_0, int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        exit_status_0 = module_2.main()
        bytes_0 = b'2\xbd\xf5\x12\x93\x84aT\x1a\xba\x85\x91\xd5\xb8\xe5~!\x976'
        list_0 = [bytes_0, bytes_0]
        str_0 = '--ssl'
        list_1 = module_2.decode_raw_args(list_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = "^dL!+a:'bk6(ITBO)cY"
        bytes_0 = None
        list_0 = [str_0, str_0, bytes_0]
        list_1 = module_2.decode_raw_args(list_0, str_0)
        dict_0 = {str_0: str_0, str_0: str_0}
        exit_status_0 = module_2.main()
        environment_0 = module_3.Environment(dict_0)
        namespace_0 = module_0.Namespace(**dict_0)
        exit_status_1 = module_2.main(list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '--debug'
        str_1 = 'h&tp://localhost'
        str_2 = [str_0, str_0, str_1]
        exit_status_0 = module_2.main(str_2)
    except BaseException:
        pass

def test_case_5():
    try:
        var_0 = []
        environment_0 = module_3.Environment()
        exit_status_0 = module_2.program(var_0, environment_0)
    except BaseException:
        pass