# Automatically generated by Pynguin.
import httpie.models as module_0
import httpie.output.streams as module_1
import httpie.output.processing as module_2

def test_case_0():
    try:
        bytes_0 = b'n\xe7\xc3\xc85\xd0.'
        h_t_t_p_message_0 = module_0.HTTPMessage(bytes_0)
        binary_suppressed_error_0 = module_1.BinarySuppressedError()
        base_stream_0 = module_1.BaseStream(h_t_t_p_message_0, binary_suppressed_error_0)
        bytes_1 = base_stream_0.get_headers()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '@hoHFIR0tbBbI%('
        h_t_t_p_message_0 = module_0.HTTPMessage(str_0)
        base_stream_0 = module_1.BaseStream(h_t_t_p_message_0)
        iterable_0 = base_stream_0.iter_body()
    except BaseException:
        pass

def test_case_2():
    try:
        raw_stream_0 = module_1.RawStream()
    except BaseException:
        pass

def test_case_3():
    try:
        encoded_stream_0 = module_1.EncodedStream()
    except BaseException:
        pass

def test_case_4():
    try:
        tuple_0 = ()
        h_t_t_p_message_0 = module_0.HTTPMessage(tuple_0)
        list_0 = []
        base_stream_0 = module_1.BaseStream(h_t_t_p_message_0, list_0)
        iterable_0 = base_stream_0.__iter__()
        h_t_t_p_message_1 = module_0.HTTPMessage(iterable_0)
        conversion_0 = module_2.Conversion()
        list_1 = []
        formatting_0 = module_2.Formatting(list_1)
        pretty_stream_0 = module_1.PrettyStream(conversion_0, formatting_0)
    except BaseException:
        pass

def test_case_5():
    try:
        conversion_0 = module_2.Conversion()
        str_0 = '(7T6Xd'
        dict_0 = {str_0: conversion_0, str_0: conversion_0}
        h_t_t_p_message_0 = module_0.HTTPMessage(dict_0)
        bytes_0 = None
        callable_0 = None
        base_stream_0 = module_1.BaseStream(h_t_t_p_message_0, bytes_0, callable_0)
    except BaseException:
        pass