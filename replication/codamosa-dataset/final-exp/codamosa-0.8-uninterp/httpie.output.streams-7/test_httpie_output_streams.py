# Automatically generated by Pynguin.
import httpie.output.streams as module_0
import httpie.models as module_1

def test_case_0():
    binary_suppressed_error_0 = module_0.BinarySuppressedError()

def test_case_1():
    str_0 = 'BZ\rg<'
    h_t_t_p_message_0 = module_1.HTTPMessage(str_0)
    tuple_0 = ()
    str_1 = 'XN /Xo_Re'
    base_stream_0 = module_0.BaseStream(h_t_t_p_message_0, tuple_0, str_1)

def test_case_2():
    str_0 = '\n    The main function.\n\n    Pre-process args, handle some special types of invocations,\n    and run the main program with error handling.\n\n    Return exit status code.\n\n    '
    h_t_t_p_message_0 = module_1.HTTPMessage(str_0)
    bytes_0 = b'\xac\xc4L\xf0\xff\x88'
    binary_suppressed_error_0 = module_0.BinarySuppressedError()
    base_stream_0 = module_0.BaseStream(h_t_t_p_message_0, bytes_0, binary_suppressed_error_0)
    iterable_0 = base_stream_0.__iter__()