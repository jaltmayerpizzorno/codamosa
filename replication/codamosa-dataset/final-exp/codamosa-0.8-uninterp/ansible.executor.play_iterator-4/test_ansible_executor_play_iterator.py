# Automatically generated by Pynguin.
import ansible.executor.play_iterator as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'jIZr/G%OF5L,<Uy&72%V'
    host_state_0 = module_0.HostState(str_0)

def test_case_2():
    str_0 = 'A:a+HZ6d}xYv$CY<A'
    host_state_0 = module_0.HostState(str_0)
    var_0 = host_state_0.__str__()

def test_case_3():
    str_0 = 'jIZr/G%OF5L,<Uy&72%V'
    host_state_0 = module_0.HostState(str_0)
    var_0 = host_state_0.get_current_block()

def test_case_4():
    str_0 = 'lt,'
    host_state_0 = module_0.HostState(str_0)
    var_0 = host_state_0.copy()

def test_case_5():
    str_0 = 'A:a+HZ6d}xYv$CY<A'
    host_state_0 = module_0.HostState(str_0)
    var_0 = host_state_0.get_current_block()
    var_1 = host_state_0.__str__()
    float_0 = -2579.9962
    str_1 = 'uc'
    host_state_1 = module_0.HostState(str_1)
    var_2 = host_state_1.__eq__(float_0)

def test_case_6():
    bytes_0 = b'5p'
    host_state_0 = module_0.HostState(bytes_0)
    var_0 = host_state_0.__eq__(host_state_0)
    var_1 = host_state_0.__str__()