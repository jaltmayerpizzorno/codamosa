# Automatically generated by Pynguin.
import ansible.vars.manager as module_0

def test_case_0():
    pass

def test_case_1():
    dict_0 = {}
    var_0 = module_0.preprocess_vars(dict_0)
    variable_manager_0 = module_0.VariableManager()

def test_case_2():
    variable_manager_0 = module_0.VariableManager()

def test_case_3():
    variable_manager_0 = module_0.VariableManager()
    str_0 = 'host1'
    var_0 = variable_manager_0.__getstate__()
    str_1 = 'value'
    var_1 = variable_manager_0.set_host_variable(str_0, str_1, str_1)
    str_2 = 'host2'
    var_2 = variable_manager_0.set_host_variable(str_2, str_0, str_1)
    str_3 = 'newvalue'
    var_3 = variable_manager_0.set_host_variable(str_0, str_1, str_3)

def test_case_4():
    variable_manager_0 = module_0.VariableManager()
    vars_with_sources_0 = module_0.VarsWithSources()
    var_0 = variable_manager_0.__setstate__(vars_with_sources_0)
    str_0 = 'ho~st1'
    var_1 = variable_manager_0.set_host_variable(str_0, str_0, str_0)
    str_1 = 'host2'
    var_2 = variable_manager_0.set_host_variable(str_1, str_0, str_0)
    str_2 = 'newvalue'
    var_3 = variable_manager_0.set_host_variable(str_0, str_2, str_2)

def test_case_5():
    dict_0 = {}
    float_0 = -690.990905
    variable_manager_0 = module_0.VariableManager(float_0)
    var_0 = variable_manager_0.set_inventory(dict_0)

def test_case_6():
    variable_manager_0 = module_0.VariableManager()
    str_0 = 'host1'
    bytes_0 = b'\xf2\x92'
    var_0 = variable_manager_0.clear_facts(bytes_0)
    str_1 = 'varname'
    str_2 = 'value'
    var_1 = variable_manager_0.set_host_variable(str_0, str_1, str_2)
    str_3 = 'newvalue'
    var_2 = variable_manager_0.set_host_variable(str_0, str_1, str_3)

def test_case_7():
    variable_manager_0 = module_0.VariableManager()
    str_0 = 'c'
    str_1 = 'b'
    str_2 = {str_1: str_1, str_0: str_1}
    str_3 = 'hostname'
    var_0 = variable_manager_0.set_host_facts(str_3, str_2)
    var_1 = variable_manager_0.set_host_facts(str_3, str_2)

def test_case_8():
    bool_0 = True
    float_0 = -2870.0
    bytes_0 = b'^\x84m\x9f\x93\xffP'
    variable_manager_0 = module_0.VariableManager()
    var_0 = variable_manager_0.set_host_variable(bool_0, float_0, bytes_0)

def test_case_9():
    list_0 = []
    vars_with_sources_0 = module_0.VarsWithSources(*list_0)
    var_0 = vars_with_sources_0.copy()

def test_case_10():
    str_0 = 'architecture'
    dict_0 = {str_0: str_0, str_0: str_0}
    variable_manager_0 = module_0.VariableManager(dict_0)
    str_1 = ')x]8I'
    variable_manager_1 = module_0.VariableManager(str_1)
    vars_with_sources_0 = module_0.VarsWithSources()
    var_0 = vars_with_sources_0.__len__()

def test_case_11():
    list_0 = []
    vars_with_sources_0 = module_0.VarsWithSources()
    str_0 = '8u?)Vqk\r)]-eS"WG'
    var_0 = module_0.preprocess_vars(list_0)
    str_1 = 'a&{3y\x0c'
    dict_0 = {str_0: list_0, str_1: list_0, str_0: str_0}
    vars_with_sources_1 = module_0.VarsWithSources(*list_0, **dict_0)
    var_1 = vars_with_sources_1.copy()

def test_case_12():
    variable_manager_0 = module_0.VariableManager()
    str_0 = 'value'
    var_0 = variable_manager_0.set_host_variable(str_0, str_0, str_0)
    var_1 = variable_manager_0.set_host_variable(str_0, str_0, str_0)
    var_2 = variable_manager_0.set_host_variable(str_0, str_0, str_0)