# Automatically generated by Pynguin.
import ansible.executor.interpreter_discovery as module_0

def test_case_0():
    try:
        str_0 = 'DVHDPZ_2'
        float_0 = 2620.0
        set_0 = {str_0}
        interpreter_discovery_required_error_0 = module_0.InterpreterDiscoveryRequiredError(str_0, float_0, set_0)
        var_0 = interpreter_discovery_required_error_0.__str__()
    except BaseException:
        pass

def test_case_1():
    try:
        dict_0 = {}
        bool_0 = False
        interpreter_discovery_required_error_0 = module_0.InterpreterDiscoveryRequiredError(dict_0, bool_0, bool_0)
        var_0 = interpreter_discovery_required_error_0.__repr__()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'python'
        var_0 = {}
        var_1 = module_0.discover_interpreter(var_0, str_0, str_0, var_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'c$n\x0b$'
        int_0 = 3928
        bytes_0 = None
        list_0 = []
        var_0 = module_0.discover_interpreter(str_0, int_0, bytes_0, list_0)
    except BaseException:
        pass