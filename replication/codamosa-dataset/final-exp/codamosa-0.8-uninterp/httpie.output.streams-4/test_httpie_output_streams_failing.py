# Automatically generated by Pynguin.
import httpie.models as module_0
import httpie.output.streams as module_1
import httpie.output.processing as module_2

def test_case_0():
    try:
        str_0 = '\n    Set to "no" (or "false") to skip checking the host\'s SSL certificate.\n    Defaults to "yes" ("true"). You can also pass the path to a CA_BUNDLE file\n    for private certs. (Or you can set the REQUESTS_CA_BUNDLE environment\n    variable instead.)\n    '
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        list_0 = [str_0, dict_0, str_0, dict_0]
        h_t_t_p_message_0 = module_0.HTTPMessage(list_0)
        data_suppressed_error_0 = module_1.DataSuppressedError()
        base_stream_0 = module_1.BaseStream(h_t_t_p_message_0, data_suppressed_error_0)
        bytes_0 = base_stream_0.get_headers()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '\n    Set to "no" (or "false") to skip checking the host\'s SSL certificate.\n    Defaults to "yes" ("true"). You can also pass the path to a CA_BUNDLE file\n    for private certs. (Or you can set the REQUESTS_CA_BUNDLE environment\n    variable instead.)\n    '
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        list_0 = [str_0, dict_0, str_0, dict_0]
        h_t_t_p_message_0 = module_0.HTTPMessage(list_0)
        data_suppressed_error_0 = module_1.DataSuppressedError()
        base_stream_0 = module_1.BaseStream(h_t_t_p_message_0, data_suppressed_error_0)
        raw_stream_0 = module_1.RawStream(**dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        encoded_stream_0 = module_1.EncodedStream()
    except BaseException:
        pass

def test_case_3():
    try:
        conversion_0 = module_2.Conversion()
        list_0 = []
        dict_0 = {}
        formatting_0 = module_2.Formatting(list_0, **dict_0)
        pretty_stream_0 = module_1.PrettyStream(conversion_0, formatting_0)
    except BaseException:
        pass

def test_case_4():
    try:
        data_suppressed_error_0 = module_1.DataSuppressedError()
        h_t_t_p_message_0 = module_0.HTTPMessage(data_suppressed_error_0)
        tuple_0 = ()
        base_stream_0 = module_1.BaseStream(h_t_t_p_message_0, tuple_0)
        h_t_t_p_message_1 = module_0.HTTPMessage(base_stream_0)
        base_stream_1 = module_1.BaseStream(h_t_t_p_message_1)
        conversion_0 = module_2.Conversion()
        encoded_stream_0 = module_1.EncodedStream(tuple_0)
    except BaseException:
        pass

def test_case_5():
    try:
        data_suppressed_error_0 = module_1.DataSuppressedError()
        h_t_t_p_message_0 = module_0.HTTPMessage(data_suppressed_error_0)
        tuple_0 = ()
        base_stream_0 = module_1.BaseStream(h_t_t_p_message_0, tuple_0)
        iterable_0 = base_stream_0.iter_body()
    except BaseException:
        pass

def test_case_6():
    try:
        data_suppressed_error_0 = module_1.DataSuppressedError()
        h_t_t_p_message_0 = module_0.HTTPMessage(data_suppressed_error_0)
        tuple_0 = ()
        tuple_1 = None
        base_stream_0 = module_1.BaseStream(h_t_t_p_message_0, tuple_0, tuple_1)
    except BaseException:
        pass