# Automatically generated by Pynguin.
import ansible.vars.manager as module_0

def test_case_0():
    try:
        vars_with_sources_0 = module_0.VarsWithSources()
        str_0 = ',:iDuk4mB'
        variable_manager_0 = module_0.VariableManager(str_0)
        bool_0 = False
        var_0 = module_0.preprocess_vars(bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        list_0 = []
        var_0 = module_0.preprocess_vars(list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        variable_manager_0 = module_0.VariableManager()
        var_0 = dict()
        var_1 = dict()
        str_0 = 'localhost'
        var_2 = variable_manager_0.set_host_facts(str_0, var_1)
        var_3 = dict()
        var_4 = variable_manager_0.set_host_facts(str_0, var_3)
        bytes_0 = None
        var_5 = variable_manager_0.__setstate__(bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = True
        set_0 = set()
        bool_1 = False
        dict_0 = {}
        float_0 = -518.7
        variable_manager_0 = module_0.VariableManager(float_0)
        var_0 = variable_manager_0.get_vars(bool_0, set_0, bool_1, dict_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'\xbc\xe62"\xeak\x00`\xb6\x13\xe8'
        str_0 = 'E\\^y\rimWWaK/\x0c'
        variable_manager_0 = module_0.VariableManager(str_0)
        var_0 = variable_manager_0.clear_facts(bytes_0)
        vars_with_sources_0 = module_0.VarsWithSources()
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = False
        float_0 = 1037.2
        variable_manager_0 = module_0.VariableManager()
        var_0 = variable_manager_0.set_nonpersistent_facts(bool_0, float_0)
    except BaseException:
        pass

def test_case_6():
    try:
        dict_0 = {}
        vars_with_sources_0 = module_0.VarsWithSources()
        vars_with_sources_1 = module_0.VarsWithSources(**dict_0)
        dict_1 = {}
        variable_manager_0 = module_0.VariableManager()
        var_0 = variable_manager_0.set_nonpersistent_facts(dict_1, dict_1)
    except BaseException:
        pass

def test_case_7():
    try:
        bool_0 = False
        variable_manager_0 = module_0.VariableManager(bool_0)
        str_0 = 'E'
        dict_0 = {str_0: str_0}
        vars_with_sources_0 = module_0.VarsWithSources(**dict_0)
        list_0 = [vars_with_sources_0]
        vars_with_sources_1 = module_0.VarsWithSources(*list_0)
        var_0 = vars_with_sources_1.__getitem__(variable_manager_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'OT'
        variable_manager_0 = module_0.VariableManager(str_0)
        vars_with_sources_0 = module_0.VarsWithSources()
        var_0 = vars_with_sources_0.__delitem__(variable_manager_0)
    except BaseException:
        pass

def test_case_9():
    try:
        variable_manager_0 = module_0.VariableManager()
        str_0 = 'test'
        str_1 = 'my_varname'
        str_2 = 'my_value'
        var_0 = variable_manager_0.set_host_variable(str_0, str_1, str_2)
        str_3 = 'new_value'
        var_1 = variable_manager_0.set_host_variable(str_0, str_1, str_3)
        str_4 = 'some_value'
        vars_with_sources_0 = module_0.VarsWithSources()
        var_2 = vars_with_sources_0.__len__()
        dict_0 = {str_1: str_2, str_4: str_3}
        var_3 = variable_manager_0.set_host_facts(dict_0, variable_manager_0)
    except BaseException:
        pass

def test_case_10():
    try:
        dict_0 = None
        vars_with_sources_0 = module_0.VarsWithSources()
        str_0 = ',:iDuk4mB'
        str_1 = "g\n1[mH#LG2b3'1f7'"
        list_0 = None
        bytes_0 = b'\x12\x0e\x83\xf3\x0b\x831\xce\x15I\xd0\xf7j\x92\x93\x1c\t\xee\tf'
        float_0 = -1305.071925
        var_0 = vars_with_sources_0.__contains__(float_0)
        variable_manager_0 = module_0.VariableManager(vars_with_sources_0, bytes_0)
        var_1 = variable_manager_0.set_host_variable(str_1, dict_0, list_0)
        variable_manager_1 = module_0.VariableManager(str_0)
        str_2 = ''
        var_2 = module_0.preprocess_vars(str_2)
    except BaseException:
        pass

def test_case_11():
    try:
        bool_0 = False
        dict_0 = {}
        vars_with_sources_0 = module_0.VarsWithSources(**dict_0)
        str_0 = 'U3N hPb'
        dict_1 = {str_0: str_0}
        dict_2 = None
        variable_manager_0 = module_0.VariableManager()
        var_0 = variable_manager_0.set_inventory(dict_2)
        vars_with_sources_1 = module_0.VarsWithSources(**dict_1)
        var_1 = vars_with_sources_1.__iter__()
        var_2 = vars_with_sources_1.__iter__()
        dict_3 = {bool_0: bool_0, bool_0: bool_0}
        var_3 = module_0.preprocess_vars(dict_3)
        dict_4 = {}
        vars_with_sources_2 = module_0.VarsWithSources(**dict_4)
        float_0 = -43.575477
        var_4 = module_0.preprocess_vars(float_0)
    except BaseException:
        pass

def test_case_12():
    try:
        variable_manager_0 = module_0.VariableManager()
        str_0 = 'test'
        str_1 = 'my_varname'
        str_2 = 'my_value'
        var_0 = variable_manager_0.set_host_variable(str_0, str_1, str_2)
        var_1 = variable_manager_0.set_host_variable(str_0, str_1, str_2)
        vars_with_sources_0 = module_0.VarsWithSources()
        dict_0 = {str_1: str_2}
        var_2 = variable_manager_0.set_host_facts(dict_0, variable_manager_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = '\t]T4I_y1E=$'
        dict_0 = {str_0: str_0, str_0: str_0}
        vars_with_sources_0 = module_0.VarsWithSources()
        variable_manager_0 = module_0.VariableManager()
        var_0 = variable_manager_0.set_host_facts(dict_0, vars_with_sources_0)
    except BaseException:
        pass