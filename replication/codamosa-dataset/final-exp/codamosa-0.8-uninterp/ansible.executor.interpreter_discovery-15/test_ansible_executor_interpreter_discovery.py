# Automatically generated by Pynguin.
import ansible.executor.interpreter_discovery as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '@wo'
    int_0 = 797
    set_0 = set()
    interpreter_discovery_required_error_0 = module_0.InterpreterDiscoveryRequiredError(str_0, int_0, set_0)

def test_case_2():
    var_0 = {}
    str_0 = 'python'
    str_1 = 'auto_silent'
    var_1 = module_0.discover_interpreter(str_0, str_0, str_1, var_0)