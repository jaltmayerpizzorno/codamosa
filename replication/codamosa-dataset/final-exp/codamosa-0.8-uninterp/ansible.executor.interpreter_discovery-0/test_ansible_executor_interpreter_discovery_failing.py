# Automatically generated by Pynguin.
import ansible.executor.interpreter_discovery as module_0

def test_case_0():
    try:
        complex_0 = None
        dict_0 = {complex_0: complex_0, complex_0: complex_0, complex_0: complex_0}
        int_0 = 20
        bool_0 = True
        bytes_0 = b'\x89[?\x1a\x11\xa1f\xae+Ky\xdc1'
        str_0 = 'sending task start callback, copying the task so we can template it temporarily'
        tuple_0 = (int_0, bool_0, bytes_0, str_0)
        interpreter_discovery_required_error_0 = module_0.InterpreterDiscoveryRequiredError(dict_0, tuple_0, tuple_0)
        var_0 = interpreter_discovery_required_error_0.__str__()
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        list_0 = [bool_0, bool_0, bool_0]
        bool_1 = False
        str_0 = 'Hni=B;03\nG'
        interpreter_discovery_required_error_0 = module_0.InterpreterDiscoveryRequiredError(list_0, bool_1, str_0)
        var_0 = interpreter_discovery_required_error_0.__repr__()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'pythoA'
        var_0 = module_0.discover_interpreter(str_0, str_0, str_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'python'
        var_0 = dict()
        var_1 = module_0.discover_interpreter(var_0, str_0, str_0, var_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'python'
        var_0 = module_0.discover_interpreter(str_0, str_0, str_0, str_0)
    except BaseException:
        pass