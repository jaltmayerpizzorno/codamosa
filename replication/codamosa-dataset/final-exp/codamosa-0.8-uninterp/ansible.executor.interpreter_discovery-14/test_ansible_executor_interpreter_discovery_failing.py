# Automatically generated by Pynguin.
import ansible.executor.interpreter_discovery as module_0

def test_case_0():
    try:
        str_0 = 'Z\nqK*Sn~!f'
        list_0 = [str_0, str_0, str_0, str_0]
        int_0 = 3440
        interpreter_discovery_required_error_0 = module_0.InterpreterDiscoveryRequiredError(str_0, list_0, int_0)
        var_0 = interpreter_discovery_required_error_0.__str__()
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        int_0 = 711
        list_0 = [bool_0, bool_0, bool_0]
        interpreter_discovery_required_error_0 = module_0.InterpreterDiscoveryRequiredError(bool_0, int_0, list_0)
        var_0 = interpreter_discovery_required_error_0.__repr__()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'python'
        var_0 = module_0.discover_interpreter(str_0, str_0, str_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = None
        str_0 = 'm-t'
        float_0 = 2998.0
        str_1 = 'DBZ mK`}Yas]5C'
        var_0 = module_0.discover_interpreter(bytes_0, str_0, float_0, str_1)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'python'
        var_0 = {}
        var_1 = module_0.discover_interpreter(var_0, str_0, str_0, var_0)
    except BaseException:
        pass