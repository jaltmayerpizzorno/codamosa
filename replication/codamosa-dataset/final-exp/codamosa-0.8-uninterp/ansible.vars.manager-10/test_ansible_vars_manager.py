# Automatically generated by Pynguin.
import ansible.vars.manager as module_0

def test_case_0():
    pass

def test_case_1():
    tuple_0 = ()
    tuple_1 = None
    var_0 = module_0.preprocess_vars(tuple_1)
    set_0 = {var_0, tuple_0, var_0}
    variable_manager_0 = module_0.VariableManager(set_0)

def test_case_2():
    variable_manager_0 = module_0.VariableManager()

def test_case_3():
    bool_0 = False
    variable_manager_0 = module_0.VariableManager(bool_0)
    var_0 = variable_manager_0.__getstate__()
    bytes_0 = b'\x0b\x99K'
    str_0 = '_workers'
    var_1 = variable_manager_0.set_host_variable(bytes_0, bytes_0, str_0)

def test_case_4():
    tuple_0 = None
    variable_manager_0 = module_0.VariableManager(tuple_0)
    str_0 = 'O"4?%'
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    variable_manager_1 = module_0.VariableManager()
    variable_manager_2 = module_0.VariableManager(dict_0, variable_manager_1)
    var_0 = variable_manager_2.set_inventory(variable_manager_0)

def test_case_5():
    vars_with_sources_0 = None
    variable_manager_0 = module_0.VariableManager(vars_with_sources_0)
    int_0 = 4096
    var_0 = variable_manager_0.clear_facts(int_0)

def test_case_6():
    int_0 = -571
    str_0 = 'deb'
    dict_0 = {str_0: int_0, str_0: int_0, str_0: str_0}
    variable_manager_0 = module_0.VariableManager()
    var_0 = variable_manager_0.set_host_facts(int_0, dict_0)

def test_case_7():
    bytes_0 = b'n7\x81\xdfEo\xba\xffcx]\xa4\x0c\x9a\xc81'
    float_0 = 913.644
    variable_manager_0 = module_0.VariableManager(float_0)
    var_0 = variable_manager_0.set_host_variable(bytes_0, bytes_0, variable_manager_0)

def test_case_8():
    list_0 = []
    vars_with_sources_0 = module_0.VarsWithSources(*list_0)

def test_case_9():
    vars_with_sources_0 = module_0.VarsWithSources()
    var_0 = vars_with_sources_0.copy()

def test_case_10():
    float_0 = 1753.86
    list_0 = []
    vars_with_sources_0 = module_0.VarsWithSources(*list_0)
    var_0 = vars_with_sources_0.get_source(float_0)

def test_case_11():
    set_0 = None
    vars_with_sources_0 = module_0.VarsWithSources()
    dict_0 = {}
    var_0 = vars_with_sources_0.__setitem__(set_0, vars_with_sources_0)
    tuple_0 = (set_0,)
    vars_with_sources_1 = module_0.VarsWithSources(**dict_0)
    bool_0 = True
    variable_manager_0 = module_0.VariableManager(bool_0)
    var_1 = variable_manager_0.clear_facts(tuple_0)

def test_case_12():
    vars_with_sources_0 = module_0.VarsWithSources()
    var_0 = vars_with_sources_0.__iter__()

def test_case_13():
    vars_with_sources_0 = module_0.VarsWithSources()
    var_0 = vars_with_sources_0.copy()
    var_1 = vars_with_sources_0.__len__()

def test_case_14():
    str_0 = 'merge'
    str_1 = 'fCP+o]jBAy-\t'
    str_2 = 'n(B2?Y0`3.ue(;\r'
    str_3 = '$&PSxso'
    dict_0 = {str_1: str_1, str_0: str_0, str_2: str_1, str_3: str_0}
    vars_with_sources_0 = module_0.VarsWithSources(**dict_0)
    bytes_0 = b'?\x905\xee'
    list_0 = [bytes_0]
    bool_0 = False
    variable_manager_0 = module_0.VariableManager(list_0, bool_0, bool_0)
    var_0 = variable_manager_0.set_nonpersistent_facts(str_0, vars_with_sources_0)

def test_case_15():
    vars_with_sources_0 = module_0.VarsWithSources()
    set_0 = set()
    list_0 = [set_0, vars_with_sources_0, vars_with_sources_0]
    variable_manager_0 = module_0.VariableManager()
    var_0 = variable_manager_0.__getstate__()
    list_1 = []
    str_0 = '}\x0cOE+}<tea'
    variable_manager_1 = module_0.VariableManager(variable_manager_0, list_1, str_0)
    var_1 = variable_manager_1.set_inventory(list_0)
    variable_manager_2 = module_0.VariableManager()
    var_2 = module_0.preprocess_vars(list_1)

def test_case_16():
    variable_manager_0 = module_0.VariableManager()
    str_0 = 'value2'
    var_0 = variable_manager_0.set_host_variable(str_0, str_0, str_0)
    var_1 = variable_manager_0.set_host_variable(str_0, str_0, str_0)

def test_case_17():
    variable_manager_0 = module_0.VariableManager()
    str_0 = 'hostname'
    str_1 = 'foo'
    str_2 = {str_1: str_1}
    var_0 = variable_manager_0.set_host_facts(str_0, str_2)
    str_3 = 'baz'
    str_4 = {str_3: str_3}
    var_1 = variable_manager_0.set_host_facts(str_0, str_4)