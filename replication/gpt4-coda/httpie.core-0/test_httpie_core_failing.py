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
        str_0 = 'M\tzRnpu_H[S9o}w'
        list_0 = [str_0, str_0]
        environment_0 = module_3.Environment()
        var_0 = module_2.print_debug_info(environment_0)
        var_1 = environment_0.__repr__()
        exit_status_0 = module_2.main(list_0)
    except BaseException:
        pass