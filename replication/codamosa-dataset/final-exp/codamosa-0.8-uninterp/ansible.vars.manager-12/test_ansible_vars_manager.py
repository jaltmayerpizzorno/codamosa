# Automatically generated by Pynguin.
import ansible.vars.manager as module_0

def test_case_0():
    pass

def test_case_1():
    variable_manager_0 = module_0.VariableManager()

def test_case_2():
    int_0 = -2649
    variable_manager_0 = module_0.VariableManager()
    var_0 = variable_manager_0.clear_facts(int_0)

def test_case_3():
    bytes_0 = b'\xfd\x00\xa7\xf0m\xbb\xab\xf0\x87.0\xa5\xb2RZ6\xfc0'
    variable_manager_0 = module_0.VariableManager(bytes_0)
    str_0 = "DV'BEE'MBFK"
    dict_0 = {}
    var_0 = variable_manager_0.set_host_facts(str_0, dict_0)

def test_case_4():
    int_0 = 38
    str_0 = 'a :\tI\\@%/'
    list_0 = [int_0]
    variable_manager_0 = module_0.VariableManager()
    var_0 = variable_manager_0.set_host_variable(int_0, str_0, list_0)
    bytes_0 = b'`\x9a\xf0\x9d\xefg\xd0&\xa3\t\x83n\x97\xe1X\xcf'
    float_0 = -2528.474
    variable_manager_1 = module_0.VariableManager(bytes_0, float_0)

def test_case_5():
    vars_with_sources_0 = module_0.VarsWithSources()
    var_0 = vars_with_sources_0.__len__()

def test_case_6():
    str_0 = 'mZhwxTo\\I\\V+'
    str_1 = '@:;V@pl{a}`8'
    dict_0 = {str_0: str_0, str_1: str_0}
    vars_with_sources_0 = module_0.VarsWithSources(**dict_0)
    var_0 = vars_with_sources_0.copy()
    vars_with_sources_1 = module_0.VarsWithSources()

def test_case_7():
    list_0 = None
    str_0 = 'lp~]X~-/'
    list_1 = [list_0, str_0, list_0]
    variable_manager_0 = module_0.VariableManager(str_0, list_1)
    var_0 = variable_manager_0.__getstate__()
    float_0 = -1997.0
    dict_0 = {}
    vars_with_sources_0 = module_0.VarsWithSources(**dict_0)
    var_1 = vars_with_sources_0.__iter__()
    dict_1 = None
    variable_manager_1 = module_0.VariableManager(float_0, dict_1)
    vars_with_sources_1 = module_0.VarsWithSources()
    var_2 = vars_with_sources_1.get_source(list_0)

def test_case_8():
    dict_0 = {}
    vars_with_sources_0 = module_0.VarsWithSources(**dict_0)
    var_0 = vars_with_sources_0.__iter__()

def test_case_9():
    bytes_0 = b''
    vars_with_sources_0 = module_0.VarsWithSources()
    var_0 = vars_with_sources_0.__contains__(bytes_0)

def test_case_10():
    bool_0 = False
    dict_0 = {bool_0: bool_0, bool_0: bool_0}
    str_0 = '|`foNqDJ<\x0c{:4e]}L'
    variable_manager_0 = module_0.VariableManager(str_0)
    tuple_0 = None
    list_0 = None
    var_0 = variable_manager_0.set_host_variable(tuple_0, list_0, bool_0)
    var_1 = variable_manager_0.set_inventory(dict_0)

def test_case_11():
    str_0 = 'y]>'
    dict_0 = {str_0: str_0}
    vars_with_sources_0 = module_0.VarsWithSources(**dict_0)
    var_0 = vars_with_sources_0.copy()
    var_1 = vars_with_sources_0.__len__()
    var_2 = vars_with_sources_0.__len__()
    variable_manager_0 = module_0.VariableManager(vars_with_sources_0)
    var_3 = module_0.preprocess_vars(dict_0)
    dict_1 = {str_0: str_0}
    variable_manager_1 = module_0.VariableManager(dict_1)
    variable_manager_2 = module_0.VariableManager(str_0)
    bytes_0 = None
    var_4 = vars_with_sources_0.__contains__(bytes_0)
    tuple_0 = None
    var_5 = variable_manager_2.clear_facts(tuple_0)
    bool_0 = False
    bytes_1 = b'_\x14p\xbb\x9aj\x9c\x8c}l\x98\x9c'
    var_6 = variable_manager_0.set_host_variable(bool_0, bytes_1, tuple_0)
    variable_manager_3 = module_0.VariableManager()
    int_0 = 3233
    str_1 = 'r0oV?\t3Y($I+0@8HT])'
    variable_manager_4 = module_0.VariableManager(int_0, str_1)
    var_7 = variable_manager_1.set_nonpersistent_facts(tuple_0, vars_with_sources_0)

def test_case_12():
    variable_manager_0 = module_0.VariableManager()
    str_0 = 'h1'
    str_1 = 'a'
    int_0 = 2
    float_0 = -1676.0
    bool_0 = False
    dict_0 = {str_1: str_0}
    vars_with_sources_0 = module_0.VarsWithSources(**dict_0)
    var_0 = vars_with_sources_0.__setitem__(float_0, bool_0)
    var_1 = variable_manager_0.set_host_variable(str_0, str_1, int_0)
    str_2 = 'b'
    int_1 = 1
    int_2 = {str_2: int_1}
    var_2 = variable_manager_0.set_host_variable(str_0, str_1, int_2)
    str_3 = 'c'
    int_3 = {str_3: int_0}
    var_3 = variable_manager_0.set_host_variable(str_0, str_1, int_3)
    str_4 = 'x'
    int_4 = {str_3: int_0}
    list_0 = []
    var_4 = module_0.preprocess_vars(list_0)
    var_5 = variable_manager_0.set_host_variable(str_0, str_4, int_4)

def test_case_13():
    variable_manager_0 = module_0.VariableManager()
    str_0 = 'a'
    int_0 = 2
    var_0 = variable_manager_0.set_host_variable(str_0, str_0, int_0)
    int_1 = 1
    int_2 = {str_0: int_1}
    var_1 = variable_manager_0.set_host_variable(str_0, str_0, int_2)
    str_1 = 'c'
    int_3 = {str_1: int_0}
    var_2 = variable_manager_0.set_host_variable(str_0, str_0, int_3)
    str_2 = 'x'
    int_4 = {str_1: int_0}
    var_3 = variable_manager_0.set_host_variable(str_2, str_2, int_4)

def test_case_14():
    variable_manager_0 = module_0.VariableManager()
    str_0 = 'dummy'
    var_0 = variable_manager_0.set_host_variable(str_0, str_0, str_0)
    str_1 = 'dummy2'
    var_1 = variable_manager_0.set_host_variable(str_0, str_1, str_1)

def test_case_15():
    variable_manager_0 = module_0.VariableManager()
    str_0 = 'h1'
    str_1 = 'a'
    int_0 = 2
    var_0 = variable_manager_0.set_host_variable(str_0, str_1, int_0)
    vars_with_sources_0 = module_0.VarsWithSources()
    var_1 = vars_with_sources_0.__len__()
    str_2 = 'b'
    int_1 = 1
    int_2 = {str_2: int_1}
    var_2 = variable_manager_0.set_host_variable(str_0, str_1, int_2)
    str_3 = 'c'
    var_3 = variable_manager_0.set_host_variable(str_0, str_1, int_0)
    str_4 = 'x'
    int_3 = {str_3: int_0}
    var_4 = variable_manager_0.set_host_variable(str_0, str_4, int_3)

def test_case_16():
    variable_manager_0 = module_0.VariableManager()
    str_0 = 'host'
    str_1 = {str_0: str_0}
    str_2 = 'host'
    str_3 = {str_0: str_1}
    var_0 = variable_manager_0.set_host_facts(str_2, str_3)
    var_1 = variable_manager_0.set_host_facts(str_2, str_3)