# Automatically generated by Pynguin.
import ansible.executor.interpreter_discovery as module_0
import ansible.utils.display as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = 'illegal runlevel specified'
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    interpreter_discovery_required_error_0 = module_0.InterpreterDiscoveryRequiredError(str_0, str_0, dict_0)

def test_case_2():
    var_0 = {}
    str_0 = 'python'
    str_1 = 'auto_legacy_silent'
    var_1 = {}
    display_0 = module_1.Display()
    var_2 = module_0.discover_interpreter(var_0, str_0, str_1, var_1)