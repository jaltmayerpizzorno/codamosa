# Automatically generated by Pynguin.
import ansible.executor.interpreter_discovery as module_0

def test_case_0():
    try:
        dict_0 = None
        set_0 = {dict_0, dict_0, dict_0}
        list_0 = [set_0, dict_0, set_0]
        bool_0 = True
        float_0 = 501.733662
        interpreter_discovery_required_error_0 = module_0.InterpreterDiscoveryRequiredError(bool_0, float_0, list_0)
        var_0 = interpreter_discovery_required_error_0.__str__()
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = True
        bytes_0 = b'\x81\xce\xbd\xa1@\x04'
        str_0 = 'e2$g"]V0<j~%E'
        interpreter_discovery_required_error_0 = module_0.InterpreterDiscoveryRequiredError(bool_0, bytes_0, str_0)
        var_0 = interpreter_discovery_required_error_0.__repr__()
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 880
        float_0 = 1560.56
        bool_0 = True
        var_0 = module_0.discover_interpreter(int_0, float_0, bool_0, int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        var_0 = None
        var_1 = {}
        str_0 = 'python'
        var_2 = module_0.discover_interpreter(var_0, str_0, str_0, var_1)
    except BaseException:
        pass