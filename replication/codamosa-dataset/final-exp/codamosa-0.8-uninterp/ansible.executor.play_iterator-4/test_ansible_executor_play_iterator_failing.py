# Automatically generated by Pynguin.
import ansible.executor.play_iterator as module_0

def test_case_0():
    try:
        set_0 = None
        tuple_0 = (set_0, set_0, set_0)
        host_state_0 = module_0.HostState(tuple_0)
        var_0 = host_state_0.copy()
        var_1 = host_state_0.get_current_block()
        var_2 = host_state_0.copy()
        var_3 = host_state_0.__repr__()
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\x874'
        int_0 = -550
        dict_0 = {}
        float_0 = 0.0001
        play_iterator_0 = module_0.PlayIterator(bytes_0, int_0, dict_0, dict_0, float_0, float_0)
    except BaseException:
        pass