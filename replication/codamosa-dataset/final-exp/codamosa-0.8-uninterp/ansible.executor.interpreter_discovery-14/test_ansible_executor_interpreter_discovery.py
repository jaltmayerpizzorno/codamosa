# Automatically generated by Pynguin.
import ansible.executor.interpreter_discovery as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'Z\nqK*Sn~!f'
    list_0 = [str_0, str_0, str_0, str_0]
    int_0 = 3440
    interpreter_discovery_required_error_0 = module_0.InterpreterDiscoveryRequiredError(str_0, list_0, int_0)

def test_case_2():
    str_0 = 'python'
    str_1 = 'auto_silent'
    var_0 = {}
    var_1 = module_0.discover_interpreter(str_0, str_0, str_1, var_0)