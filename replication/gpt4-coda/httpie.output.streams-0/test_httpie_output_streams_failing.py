# Automatically generated by Pynguin.
import httpie.models as module_0
import httpie.output.processing as module_1
import httpie.output.streams as module_2

def test_case_0():
    try:
        bool_0 = True
        h_t_t_p_message_0 = module_0.HTTPMessage(bool_0)
        list_0 = []
        formatting_0 = module_1.Formatting(list_0)
        base_stream_0 = module_2.BaseStream(h_t_t_p_message_0, formatting_0)
        bytes_0 = base_stream_0.get_headers()
    except BaseException:
        pass

def test_case_1():
    try:
        raw_stream_0 = module_2.RawStream()
    except BaseException:
        pass

def test_case_2():
    try:
        encoded_stream_0 = module_2.EncodedStream()
    except BaseException:
        pass

def test_case_3():
    try:
        data_suppressed_error_0 = module_2.DataSuppressedError()
        conversion_0 = module_1.Conversion()
        list_0 = []
        dict_0 = {}
        formatting_0 = module_1.Formatting(list_0, **dict_0)
        pretty_stream_0 = module_2.PrettyStream(conversion_0, formatting_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = True
        h_t_t_p_message_0 = module_0.HTTPMessage(bool_0)
        list_0 = []
        formatting_0 = module_1.Formatting(list_0)
        tuple_0 = None
        callable_0 = None
        base_stream_0 = module_2.BaseStream(h_t_t_p_message_0, tuple_0, callable_0)
    except BaseException:
        pass

def test_case_5():
    try:
        binary_suppressed_error_0 = module_2.BinarySuppressedError()
        conversion_0 = module_1.Conversion()
        h_t_t_p_message_0 = module_0.HTTPMessage(conversion_0)
        conversion_1 = module_1.Conversion()
        str_0 = '}v/U1A'
        base_stream_0 = module_2.BaseStream(h_t_t_p_message_0, str_0)
        iterable_0 = base_stream_0.iter_body()
    except BaseException:
        pass