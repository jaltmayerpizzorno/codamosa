# Automatically generated by Pynguin.
import ansible.vars.manager as module_0

def test_case_0():
    pass

def test_case_1():
    variable_manager_0 = module_0.VariableManager()

def test_case_2():
    variable_manager_0 = module_0.VariableManager()
    str_0 = 'hsu\rt'
    str_1 = '='
    var_0 = variable_manager_0.set_host_variable(str_0, str_1, str_1)
    var_1 = variable_manager_0.set_host_variable(str_0, str_0, str_0)
    list_0 = None
    var_2 = variable_manager_0.set_inventory(list_0)

def test_case_3():
    variable_manager_0 = module_0.VariableManager()
    str_0 = 'hst'
    var_0 = variable_manager_0.set_host_variable(str_0, str_0, str_0)
    str_1 = 'Could not determine remote revision for %'
    var_1 = variable_manager_0.clear_facts(str_0)
    var_2 = variable_manager_0.set_host_variable(str_0, str_0, str_1)

def test_case_4():
    variable_manager_0 = module_0.VariableManager()
    str_0 = 'hst'
    var_0 = variable_manager_0.set_host_variable(str_0, str_0, str_0)
    var_1 = variable_manager_0.set_host_variable(str_0, str_0, str_0)

def test_case_5():
    vars_with_sources_0 = module_0.VarsWithSources()

def test_case_6():
    vars_with_sources_0 = module_0.VarsWithSources()
    int_0 = 24
    str_0 = 'w~Q$}xpsk6O'
    var_0 = vars_with_sources_0.__setitem__(int_0, str_0)
    list_0 = [vars_with_sources_0, vars_with_sources_0, vars_with_sources_0]
    var_1 = module_0.preprocess_vars(list_0)
    dict_0 = None
    bytes_0 = b'\xbfY\xd6|\xad\xe8o`\x11\xbe5\x7f\x00c\xa9U'
    bytes_1 = b';\x99\x8f\x93t\xae4\x1e\xba-\xc2'
    variable_manager_0 = module_0.VariableManager(bytes_1)
    var_2 = variable_manager_0.set_host_variable(dict_0, bytes_0, list_0)
    variable_manager_1 = module_0.VariableManager()
    var_3 = variable_manager_1.set_nonpersistent_facts(int_0, vars_with_sources_0)

def test_case_7():
    str_0 = "H%{'ddGWpi"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    vars_with_sources_0 = module_0.VarsWithSources(**dict_0)
    var_0 = vars_with_sources_0.__iter__()

def test_case_8():
    vars_with_sources_0 = module_0.VarsWithSources()
    var_0 = vars_with_sources_0.__len__()

def test_case_9():
    variable_manager_0 = module_0.VariableManager()
    str_0 = 'hst'
    str_1 = ''
    var_0 = variable_manager_0.set_host_variable(str_0, str_1, str_1)
    str_2 = 'Could not determine remote revision for %s'
    dict_0 = {}
    var_1 = module_0.preprocess_vars(dict_0)
    str_3 = 'mtu'
    var_2 = variable_manager_0.clear_facts(str_3)
    var_3 = variable_manager_0.set_host_variable(str_0, str_0, str_2)

def test_case_10():
    variable_manager_0 = module_0.VariableManager()
    dict_0 = {}
    bool_0 = False
    tuple_0 = (bool_0,)
    var_0 = variable_manager_0.set_host_facts(tuple_0, dict_0)
    vars_with_sources_0 = module_0.VarsWithSources()
    var_1 = vars_with_sources_0.__iter__()
    var_2 = variable_manager_0.__getstate__()
    var_3 = variable_manager_0.set_host_facts(tuple_0, vars_with_sources_0)