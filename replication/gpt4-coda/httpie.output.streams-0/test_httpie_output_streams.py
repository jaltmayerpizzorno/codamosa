# Automatically generated by Pynguin.
import httpie.output.streams as module_0
import httpie.models as module_1
import httpie.output.processing as module_2

def test_case_0():
    data_suppressed_error_0 = module_0.DataSuppressedError()

def test_case_1():
    bool_0 = True
    h_t_t_p_message_0 = module_1.HTTPMessage(bool_0)
    list_0 = []
    formatting_0 = module_2.Formatting(list_0)
    base_stream_0 = module_0.BaseStream(h_t_t_p_message_0, formatting_0)

def test_case_2():
    binary_suppressed_error_0 = module_0.BinarySuppressedError()
    conversion_0 = module_2.Conversion()
    h_t_t_p_message_0 = module_1.HTTPMessage(conversion_0)
    optional_0 = None
    base_stream_0 = module_0.BaseStream(h_t_t_p_message_0, optional_0)