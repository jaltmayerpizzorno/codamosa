# Automatically generated by Pynguin.
import ansible.vars.manager as module_0

def test_case_0():
    try:
        tuple_0 = ()
        var_0 = module_0.preprocess_vars(tuple_0)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = -368.7
        list_0 = [float_0, float_0, float_0, float_0]
        dict_0 = None
        tuple_0 = (float_0, list_0, dict_0)
        str_0 = '`w_]]rkm'
        dict_1 = {str_0: str_0}
        variable_manager_0 = module_0.VariableManager(dict_1)
        var_0 = variable_manager_0.__setstate__(tuple_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'varname'
        str_1 = 'value'
        float_0 = 1415.765569
        str_2 = '.e'
        str_3 = "XD2'n\x0b\n\\UZa"
        variable_manager_0 = module_0.VariableManager()
        dict_0 = {str_3: str_0, str_1: variable_manager_0}
        var_0 = variable_manager_0.__setstate__(dict_0)
        dict_1 = {str_0: str_1, str_1: str_0, str_0: float_0, str_2: variable_manager_0}
        var_1 = variable_manager_0.set_host_facts(float_0, dict_1)
        list_0 = [variable_manager_0]
        var_2 = variable_manager_0.set_host_facts(str_1, list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b''
        variable_manager_0 = module_0.VariableManager(bytes_0)
        list_0 = [variable_manager_0]
        var_0 = variable_manager_0.get_vars(list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = ';D`.\\Uyk[_Q`]st3un'
        dict_0 = {str_0: str_0, str_0: str_0}
        bool_0 = True
        str_1 = 'Operation not supported'
        variable_manager_0 = module_0.VariableManager(str_1)
        var_0 = variable_manager_0.set_host_facts(dict_0, bool_0)
    except BaseException:
        pass

def test_case_5():
    try:
        variable_manager_0 = module_0.VariableManager()
        str_0 = 'value2'
        var_0 = variable_manager_0.set_host_variable(str_0, str_0, str_0)
        var_1 = variable_manager_0.set_host_variable(str_0, str_0, str_0)
        float_0 = 944.060514
        bool_0 = False
        var_2 = variable_manager_0.set_nonpersistent_facts(float_0, bool_0)
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = -152
        vars_with_sources_0 = module_0.VarsWithSources()
        var_0 = vars_with_sources_0.__getitem__(int_0)
    except BaseException:
        pass

def test_case_7():
    try:
        set_0 = None
        tuple_0 = None
        bool_0 = True
        bool_1 = True
        dict_0 = {}
        variable_manager_0 = module_0.VariableManager(bool_1, dict_0)
        var_0 = variable_manager_0.set_host_variable(set_0, tuple_0, bool_0)
        vars_with_sources_0 = module_0.VarsWithSources()
        dict_1 = {}
        vars_with_sources_1 = module_0.VarsWithSources(**dict_1)
        var_1 = vars_with_sources_1.__setitem__(set_0, vars_with_sources_0)
        vars_with_sources_2 = module_0.VarsWithSources(**dict_1)
        list_0 = [bool_0]
        vars_with_sources_3 = module_0.VarsWithSources()
        var_2 = vars_with_sources_3.__delitem__(list_0)
    except BaseException:
        pass

def test_case_8():
    try:
        set_0 = None
        tuple_0 = None
        bool_0 = True
        bool_1 = True
        dict_0 = {}
        variable_manager_0 = module_0.VariableManager(bool_1, dict_0)
        var_0 = variable_manager_0.set_host_variable(set_0, tuple_0, bool_0)
        vars_with_sources_0 = module_0.VarsWithSources()
        dict_1 = {}
        vars_with_sources_1 = module_0.VarsWithSources(**dict_1)
        var_1 = vars_with_sources_1.__setitem__(set_0, vars_with_sources_0)
        vars_with_sources_2 = module_0.VarsWithSources(**dict_1)
        list_0 = [bool_0]
        var_2 = vars_with_sources_1.__contains__(list_0)
    except BaseException:
        pass

def test_case_9():
    try:
        vars_with_sources_0 = None
        dict_0 = {}
        vars_with_sources_1 = module_0.VarsWithSources()
        dict_1 = {}
        vars_with_sources_2 = module_0.VarsWithSources(**dict_1)
        var_0 = vars_with_sources_1.__setitem__(vars_with_sources_0, dict_0)
        variable_manager_0 = module_0.VariableManager()
        list_0 = None
        variable_manager_1 = module_0.VariableManager(list_0)
        var_1 = variable_manager_0.set_nonpersistent_facts(dict_0, dict_0)
    except BaseException:
        pass

def test_case_10():
    try:
        list_0 = []
        dict_0 = {}
        var_0 = module_0.preprocess_vars(dict_0)
        vars_with_sources_0 = module_0.VarsWithSources(*list_0)
        var_1 = vars_with_sources_0.copy()
    except BaseException:
        pass

def test_case_11():
    try:
        vars_with_sources_0 = module_0.VarsWithSources()
        list_0 = [vars_with_sources_0, vars_with_sources_0, vars_with_sources_0]
        dict_0 = {}
        str_0 = ':)YGs@gG\r9n|fb\nMx'
        variable_manager_0 = module_0.VariableManager(str_0)
        var_0 = variable_manager_0.set_host_facts(list_0, dict_0)
    except BaseException:
        pass