# Automatically generated by Pynguin.
import argparse as module_0
import httpie.context as module_1
import requests.models as module_2
import httpie.output.writer as module_3
import typing as module_4
import httpie.models as module_5
import httpie.output.streams as module_6

def test_case_0():
    try:
        namespace_0 = module_0.Namespace()
        environment_0 = module_1.Environment()
        prepared_request_0 = module_2.PreparedRequest()
        bool_0 = True
        var_0 = module_3.write_message(prepared_request_0, environment_0, namespace_0, bool_0, bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        base_stream_0 = None
        dict_0 = {}
        i_o_0 = module_4.IO(**dict_0)
        bool_0 = False
        var_0 = module_3.write_stream(base_stream_0, i_o_0, bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = None
        h_t_t_p_message_0 = module_5.HTTPMessage(int_0)
        h_t_t_p_message_1 = module_5.HTTPMessage(h_t_t_p_message_0)
        i_o_0 = module_4.IO()
        var_0 = i_o_0.read()
        var_1 = i_o_0.readline()
        list_0 = [var_0, var_0, var_1]
        base_stream_0 = module_6.BaseStream(h_t_t_p_message_1, i_o_0, list_0)
        text_i_o_0 = module_4.TextIO()
        bool_0 = False
        var_2 = module_3.write_stream_with_colors_win_py3(base_stream_0, text_i_o_0, bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        list_0 = []
        tuple_0 = (list_0,)
        h_t_t_p_message_0 = module_5.HTTPMessage(tuple_0)
        base_stream_0 = module_6.BaseStream(h_t_t_p_message_0)
        text_i_o_0 = None
        bool_0 = True
        var_0 = module_3.write_stream_with_colors_win_py3(base_stream_0, text_i_o_0, bool_0)
    except BaseException:
        pass

def test_case_4():
    try:
        environment_0 = module_1.Environment()
        namespace_0 = module_0.Namespace()
        tuple_0 = module_3.get_stream_type_and_kwargs(environment_0, namespace_0)
    except BaseException:
        pass

def test_case_5():
    try:
        response_0 = module_2.Response()
        float_0 = None
        environment_0 = module_1.Environment(float_0)
        namespace_0 = module_0.Namespace()
        list_0 = [float_0, environment_0]
        var_0 = module_3.write_message(response_0, environment_0, namespace_0, list_0)
    except BaseException:
        pass