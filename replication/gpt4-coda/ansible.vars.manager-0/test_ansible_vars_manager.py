# Automatically generated by Pynguin.
import ansible.vars.manager as module_0

def test_case_0():
    pass

def test_case_1():
    list_0 = []
    var_0 = module_0.preprocess_vars(list_0)

def test_case_2():
    variable_manager_0 = module_0.VariableManager()

def test_case_3():
    list_0 = []
    variable_manager_0 = module_0.VariableManager(list_0)
    var_0 = variable_manager_0.__getstate__()
    float_0 = -515.9
    var_1 = variable_manager_0.set_inventory(float_0)
    variable_manager_1 = module_0.VariableManager(variable_manager_0)

def test_case_4():
    str_0 = None
    str_1 = 'cookies'
    str_2 = '<^l\r()"\r_'
    dict_0 = {str_0: str_0, str_1: str_0, str_2: str_2, str_2: str_1}
    bytes_0 = b',%\x95\xe0\xb2br\x0c\xa7\xab\xb5r\xc1\x96\xc9_\x1e\xcct\xde'
    variable_manager_0 = module_0.VariableManager(bytes_0)
    var_0 = variable_manager_0.__setstate__(dict_0)

def test_case_5():
    str_0 = ';BQ*.2k'
    dict_0 = {str_0: str_0}
    variable_manager_0 = module_0.VariableManager(dict_0)
    var_0 = variable_manager_0.set_inventory(dict_0)

def test_case_6():
    float_0 = 2867.20938
    list_0 = [float_0, float_0, float_0, float_0]
    list_1 = [list_0]
    variable_manager_0 = module_0.VariableManager()
    var_0 = variable_manager_0.set_inventory(list_1)
    float_1 = 751.53
    dict_0 = {float_1: float_1, float_1: float_1, float_1: float_1}
    variable_manager_1 = module_0.VariableManager(float_1, dict_0)
    var_1 = variable_manager_1.clear_facts(variable_manager_1)

def test_case_7():
    tuple_0 = ()
    dict_0 = {}
    variable_manager_0 = module_0.VariableManager(dict_0)
    var_0 = variable_manager_0.set_host_facts(tuple_0, dict_0)
    variable_manager_1 = module_0.VariableManager()

def test_case_8():
    bytes_0 = b'\x90\xd4\xfe\x0f\x1d\xc4.4\xc3-\xf3Y\xe8d'
    variable_manager_0 = module_0.VariableManager(bytes_0)
    bytes_1 = b'\xe2\x00H,\x9c\xc2Z\xba\x9d'
    list_0 = [variable_manager_0, bytes_1]
    str_0 = '&'
    str_1 = ']vmqJ=iz~Vf'
    str_2 = 'B1,\n:-B'
    dict_0 = {str_0: list_0, str_1: variable_manager_0, str_2: list_0}
    vars_with_sources_0 = module_0.VarsWithSources(**dict_0)
    var_0 = vars_with_sources_0.__iter__()
    str_3 = "i'hG|^sq='QE"
    dict_1 = {str_0: list_0, str_3: str_0, str_3: list_0}
    vars_with_sources_1 = module_0.VarsWithSources(**dict_1)
    var_1 = vars_with_sources_1.copy()
    bytes_2 = b'\x11\x10\x12\x8e\xc4\xa1\xc3A\xc9:\x1d'
    var_2 = variable_manager_0.set_nonpersistent_facts(bytes_2, vars_with_sources_1)

def test_case_9():
    bytes_0 = b'\xe2\x00\x9dH,\xd5\x80CZ\xba\x9d'
    variable_manager_0 = module_0.VariableManager(bytes_0)
    var_0 = variable_manager_0.set_host_variable(bytes_0, variable_manager_0, bytes_0)

def test_case_10():
    bytes_0 = b'\x90\xd4\xfe\x0f\x1d\xc4.4\xc3-\xf3Y\xe8d'
    bytes_1 = b'\xe2\x00\x9dH,\xd5\x80CZ\xba\x9d'
    variable_manager_0 = module_0.VariableManager(bytes_1)
    bytes_2 = None
    var_0 = variable_manager_0.set_host_variable(bytes_0, variable_manager_0, bytes_2)
    vars_with_sources_0 = module_0.VarsWithSources()
    var_1 = vars_with_sources_0.copy()
    str_0 = 'V8CY:vR!:@\\v"bFF('
    str_1 = 'ZX(AvF(Uyx &z2J2F2'
    dict_0 = {str_0: bytes_0, str_1: var_1}
    var_2 = module_0.preprocess_vars(dict_0)

def test_case_11():
    variable_manager_0 = module_0.VariableManager()
    str_0 = 'test_host'
    str_1 = 'simple_var'
    str_2 = 't<!L'
    var_0 = variable_manager_0.set_host_variable(str_0, str_1, str_2)
    str_3 = 'dict_var'
    str_4 = {str_2: str_1}
    var_1 = variable_manager_0.set_host_variable(str_0, str_3, str_4)
    str_5 = 'key2'
    str_6 = {str_5: str_3}
    var_2 = variable_manager_0.set_host_variable(str_0, str_3, str_6)

def test_case_12():
    float_0 = None
    str_0 = None
    dict_0 = {str_0: str_0, str_0: float_0, str_0: str_0}
    variable_manager_0 = module_0.VariableManager()
    var_0 = variable_manager_0.set_nonpersistent_facts(float_0, dict_0)
    str_1 = 'simple_var'
    str_2 = 'EXEC %s'
    str_3 = {str_1: str_0}
    var_1 = variable_manager_0.set_host_variable(str_2, str_0, str_3)
    str_4 = 'key2'
    var_2 = variable_manager_0.__setstate__(dict_0)
    str_5 = 'vatlue2'
    str_6 = {str_4: str_5}
    var_3 = variable_manager_0.set_host_variable(str_2, str_1, str_6)
    var_4 = variable_manager_0.set_host_facts(variable_manager_0, dict_0)