# Automatically generated by Pynguin.
import httpie.models as module_0
import httpie.output.streams as module_1

def test_case_0():
    pass

def test_case_1():
    bool_0 = True
    h_t_t_p_message_0 = module_0.HTTPMessage(bool_0)
    dict_0 = {}
    base_stream_0 = module_1.BaseStream(h_t_t_p_message_0, dict_0)

def test_case_2():
    dict_0 = {}
    h_t_t_p_message_0 = module_0.HTTPMessage(dict_0)
    h_t_t_p_message_1 = module_0.HTTPMessage(h_t_t_p_message_0)
    base_stream_0 = module_1.BaseStream(h_t_t_p_message_1)
    h_t_t_p_message_2 = module_0.HTTPMessage(base_stream_0)