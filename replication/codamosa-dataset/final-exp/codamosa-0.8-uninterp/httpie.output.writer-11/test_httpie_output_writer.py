# Automatically generated by Pynguin.
import requests.models as module_0
import httpie.context as module_1
import argparse as module_2
import httpie.output.writer as module_3

def test_case_0():
    pass

def test_case_1():
    response_0 = module_0.Response()
    environment_0 = module_1.Environment()
    namespace_0 = module_2.Namespace()
    var_0 = module_3.write_message(response_0, environment_0, namespace_0)

def test_case_2():
    bytes_0 = b'hello_world'
    bool_0 = True
    bytes_1 = [bytes_0]
    str_0 = 'test'
    str_1 = 'w'
    var_0 = open(str_0, str_1)
    var_1 = module_3.write_stream(bytes_1, var_0, bool_0)

def test_case_3():
    var_0 = []
    bool_0 = False
    var_1 = module_3.write_stream(var_0, bool_0, bool_0)

def test_case_4():
    prepared_request_0 = module_0.PreparedRequest()
    environment_0 = module_1.Environment()
    namespace_0 = module_2.Namespace()
    var_0 = module_3.write_message(prepared_request_0, environment_0, namespace_0)
    bytes_0 = b'hello_world'
    bool_0 = False
    bytes_1 = [bytes_0]
    str_0 = 'test'
    str_1 = 'w'
    var_1 = open(str_0, str_1)
    var_2 = module_3.write_stream(bytes_1, var_1, bool_0)