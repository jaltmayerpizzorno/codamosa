# Automatically generated by Pynguin.
import ansible.executor.interpreter_discovery as module_0

def test_case_0():
    pass

def test_case_1():
    int_0 = 80
    str_0 = '`\n(0x'
    set_0 = {str_0, int_0}
    interpreter_discovery_required_error_0 = module_0.InterpreterDiscoveryRequiredError(int_0, str_0, set_0)

def test_case_2():
    var_0 = None
    str_0 = 'python'
    str_1 = 'auto_silent'
    var_1 = dict()
    var_2 = module_0.discover_interpreter(var_0, str_0, str_1, var_1)
    str_2 = [str_1]
    var_3 = dict(INTERPRETER_PYTHON_FALLBACK=str_2)
    var_4 = dict(var_3)
    var_5 = dict(config=var_4)
    var_6 = module_0.discover_interpreter(var_0, str_0, str_1, var_5)