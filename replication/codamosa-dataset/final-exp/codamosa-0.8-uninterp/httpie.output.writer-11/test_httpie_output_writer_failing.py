# Automatically generated by Pynguin.
import requests.models as module_0
import httpie.context as module_1
import argparse as module_2
import httpie.output.writer as module_3
import httpie.models as module_4
import httpie.output.streams as module_5
import typing as module_6

def test_case_0():
    try:
        response_0 = module_0.Response()
        environment_0 = module_1.Environment()
        namespace_0 = module_2.Namespace()
        var_0 = module_3.write_message(response_0, environment_0, namespace_0, environment_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        var_0 = module_3.write_stream(bool_0, bool_0, bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = -490
        h_t_t_p_message_0 = module_4.HTTPMessage(int_0)
        var_0 = None
        base_stream_0 = module_5.BaseStream(h_t_t_p_message_0, var_0)
        list_0 = []
        text_i_o_0 = module_6.TextIO(*list_0)
        bool_0 = False
        var_1 = module_3.write_stream_with_colors_win_py3(base_stream_0, text_i_o_0, bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        environment_0 = module_1.Environment()
        namespace_0 = None
        tuple_0 = module_3.get_stream_type_and_kwargs(environment_0, namespace_0)
    except BaseException:
        pass

def test_case_4():
    try:
        response_0 = module_0.Response()
        environment_0 = module_1.Environment()
        str_0 = '.html'
        dict_0 = {str_0: response_0}
        namespace_0 = module_2.Namespace(**dict_0)
        var_0 = module_3.write_message(response_0, environment_0, namespace_0)
        str_1 = '7\rOv&-~kPTG'
        list_0 = None
        var_1 = module_3.write_message(response_0, environment_0, namespace_0, list_0, str_1)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b'hello_world'
        bytes_1 = [bytes_0]
        bool_0 = True
        var_0 = module_3.write_stream(bytes_1, bytes_1, bool_0)
    except BaseException:
        pass