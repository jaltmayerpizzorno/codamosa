# Automatically generated by Pynguin.
import ansible.executor.play_iterator as module_0

def test_case_0():
    try:
        bool_0 = True
        host_state_0 = module_0.HostState(bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 0
        str_0 = 'b*isOIe>r.2"F\\'
        float_0 = 2109.6
        tuple_0 = (str_0, float_0)
        host_state_0 = module_0.HostState(tuple_0)
        host_state_1 = module_0.HostState(str_0)
        var_0 = host_state_1.__eq__(host_state_0)
        var_1 = host_state_0.copy()
        bool_0 = True
        play_iterator_0 = module_0.PlayIterator(bool_0, int_0, tuple_0, bool_0, tuple_0)
    except BaseException:
        pass

def test_case_2():
    try:
        tuple_0 = ()
        host_state_0 = module_0.HostState(tuple_0)
        var_0 = host_state_0.get_current_block()
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = 254
        str_0 = "9'SFH16SKkJ"
        str_1 = '^vjXx_3Xl;Cb4#*\t'
        bytes_0 = b',\xf7\xa7sy\xc3\xaaz\x11\x9f\xd8\x89\x92\xbe\x0c'
        play_iterator_0 = module_0.PlayIterator(int_0, str_0, str_1, bytes_0, str_0)
    except BaseException:
        pass