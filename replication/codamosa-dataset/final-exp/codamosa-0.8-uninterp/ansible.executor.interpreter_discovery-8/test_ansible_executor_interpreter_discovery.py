# Automatically generated by Pynguin.
import ansible.executor.interpreter_discovery as module_0

def test_case_0():
    pass

def test_case_1():
    int_0 = 342
    dict_0 = {int_0: int_0, int_0: int_0}
    list_0 = [int_0, int_0]
    interpreter_discovery_required_error_0 = module_0.InterpreterDiscoveryRequiredError(int_0, dict_0, list_0)

def test_case_2():
    str_0 = 'python'
    str_1 = 'auto_silent'
    var_0 = {}
    var_1 = module_0.discover_interpreter(str_1, str_0, str_1, var_0)