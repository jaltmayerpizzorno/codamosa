# Automatically generated by Pynguin.
import ansible.executor.play_iterator as module_0

def test_case_0():
    try:
        play_iterator_0 = module_0.PlayIterator()
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = True
        host_state_0 = module_0.HostState(bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'timestamping'
        bytes_0 = None
        tuple_0 = (str_0, bytes_0)
        str_1 = 'galaxy_tags'
        float_0 = -176.0
        dict_0 = {bytes_0: bytes_0, str_1: float_0, float_0: tuple_0, float_0: str_0}
        float_1 = 1000.0
        bool_0 = True
        play_iterator_0 = module_0.PlayIterator(tuple_0, str_1, dict_0, tuple_0, float_1, bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'k/QXs:fM'
        list_0 = [str_0, str_0, str_0]
        host_state_0 = module_0.HostState(list_0)
        var_0 = host_state_0.__eq__(str_0)
        var_1 = host_state_0.__str__()
        var_2 = host_state_0.__repr__()
        var_3 = host_state_0.copy()
    except BaseException:
        pass