# Automatically generated by Pynguin.
import httpie.models as module_0
import httpie.output.streams as module_1
import httpie.output.processing as module_2

def test_case_0():
    try:
        bool_0 = True
        h_t_t_p_message_0 = module_0.HTTPMessage(bool_0)
        list_0 = [h_t_t_p_message_0, bool_0, h_t_t_p_message_0]
        bool_1 = False
        base_stream_0 = module_1.BaseStream(h_t_t_p_message_0, list_0, bool_1)
        bytes_0 = base_stream_0.get_headers()
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 973
        h_t_t_p_message_0 = module_0.HTTPMessage(int_0)
        bool_0 = True
        base_stream_0 = module_1.BaseStream(h_t_t_p_message_0, bool_0)
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
        conversion_0 = module_2.Conversion()
        bool_0 = False
        h_t_t_p_message_0 = module_0.HTTPMessage(bool_0)
        list_0 = []
        base_stream_0 = module_1.BaseStream(h_t_t_p_message_0, list_0)
        list_1 = []
        formatting_0 = module_2.Formatting(list_1)
        buffered_pretty_stream_0 = module_1.BufferedPrettyStream(conversion_0, formatting_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'FZ\x0cr'
        conversion_0 = module_2.Conversion()
        optional_0 = conversion_0.get_converter(str_0)
        h_t_t_p_message_0 = module_0.HTTPMessage(conversion_0)
        bool_0 = False
        base_stream_0 = module_1.BaseStream(h_t_t_p_message_0, bool_0, bool_0)
    except BaseException:
        pass