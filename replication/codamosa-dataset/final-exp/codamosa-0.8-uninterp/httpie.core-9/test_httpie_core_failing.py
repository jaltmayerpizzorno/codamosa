# Automatically generated by Pynguin.
import argparse as module_0
import httpie.core as module_1
import httpie.context as module_2

def test_case_0():
    try:
        namespace_0 = module_0.Namespace()
        prepared_request_0 = None
        tuple_0 = module_1.get_output_options(namespace_0, prepared_request_0)
    except BaseException:
        pass

def test_case_1():
    try:
        var_0 = None
        exit_status_0 = module_1.program(var_0, var_0)
    except BaseException:
        pass

def test_case_2():
    try:
        environment_0 = None
        var_0 = module_1.print_debug_info(environment_0)
    except BaseException:
        pass

def test_case_3():
    try:
        environment_0 = module_2.Environment()
        bytes_0 = b'\xea\xa6'
        list_0 = [bytes_0, bytes_0, bytes_0]
        exit_status_0 = module_1.main(list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'p'
        environment_0 = module_2.Environment()
        var_0 = module_1.print_debug_info(environment_0)
        list_0 = [str_0, str_0]
        exit_status_0 = module_1.main(list_0)
        namespace_0 = module_0.Namespace()
        exit_status_1 = module_1.main()
        bool_0 = True
        str_1 = 'Adds additional logic to `argparse.ArgumentParser`.\n\n    Handles all input (CLI args, file args, stdin), applies defaults,\n    and performs extra validation.\n\n    '
        dict_0 = {str_0: bool_0, str_0: list_0, str_1: var_0}
        exit_status_2 = module_1.main(dict_0)
        exit_status_3 = module_1.program(namespace_0, environment_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '--debug'
        str_1 = [str_0]
        exit_status_0 = module_1.main(str_1)
        str_2 = 'http://www.example.com/'
        str_3 = [str_0, str_2, str_0, exit_status_0]
        exit_status_1 = module_1.main(str_3)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '--help'
        str_1 = [str_0]
        environment_0 = module_2.Environment()
        exit_status_0 = module_1.program(str_1, environment_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '--debug'
        str_1 = [str_0]
        exit_status_0 = module_1.main(str_1)
        str_2 = 'http://www.exaaple.crm/'
        str_3 = [str_2, str_0, str_2]
        exit_status_1 = module_1.main(str_3)
    except BaseException:
        pass