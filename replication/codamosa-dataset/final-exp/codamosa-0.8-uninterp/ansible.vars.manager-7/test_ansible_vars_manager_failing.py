# Automatically generated by Pynguin.
import ansible.vars.manager as module_0
import ansible.inventory.host as module_1

def test_case_0():
    try:
        variable_manager_0 = module_0.VariableManager()
        var_0 = variable_manager_0.__getstate__()
        bool_0 = False
        dict_0 = None
        vars_with_sources_0 = module_0.VarsWithSources()
        var_1 = vars_with_sources_0.__len__()
        var_2 = vars_with_sources_0.copy()
        var_3 = module_0.preprocess_vars(dict_0)
        bytes_0 = b'\xc0\xc2\x04\x05\xa8\x97\x9d\xef\x93\x9e'
        var_4 = variable_manager_0.clear_facts(bytes_0)
        str_0 = '<+\x0cs;'
        int_0 = 1378
        tuple_0 = (str_0, int_0, dict_0)
        var_5 = variable_manager_0.set_nonpersistent_facts(tuple_0, bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        vars_with_sources_0 = module_0.VarsWithSources()
        variable_manager_0 = module_0.VariableManager()
        var_0 = vars_with_sources_0.copy()
        var_1 = vars_with_sources_0.copy()
        var_2 = module_0.preprocess_vars(vars_with_sources_0)
        str_0 = '`Z'
        str_1 = '{jW`$XIC77J;n"h}'
        var_3 = variable_manager_0.set_nonpersistent_facts(str_0, str_1)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 3511
        vars_with_sources_0 = module_0.VarsWithSources()
        var_0 = vars_with_sources_0.copy()
        variable_manager_0 = module_0.VariableManager()
        var_1 = vars_with_sources_0.copy()
        vars_with_sources_1 = module_0.VarsWithSources()
        var_2 = module_0.preprocess_vars(vars_with_sources_1)
        var_3 = variable_manager_0.clear_facts(variable_manager_0)
        var_4 = vars_with_sources_1.get_source(int_0)
        variable_manager_1 = module_0.VariableManager()
        bytes_0 = b'B\x15'
        dict_0 = {}
        var_5 = variable_manager_1.set_host_facts(bytes_0, dict_0)
        var_6 = vars_with_sources_0.copy()
        var_7 = variable_manager_0.__setstate__(variable_manager_0)
    except BaseException:
        pass

def test_case_3():
    try:
        dict_0 = {}
        vars_with_sources_0 = module_0.VarsWithSources(**dict_0)
        variable_manager_0 = module_0.VariableManager(vars_with_sources_0)
        variable_manager_1 = module_0.VariableManager()
        str_0 = None
        var_0 = variable_manager_1.get_vars(vars_with_sources_0, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        float_0 = -2402.139
        variable_manager_0 = module_0.VariableManager()
        var_0 = variable_manager_0.clear_facts(float_0)
        vars_with_sources_0 = module_0.VarsWithSources()
        vars_with_sources_1 = module_0.VarsWithSources()
        var_1 = vars_with_sources_1.__getitem__(vars_with_sources_0)
    except BaseException:
        pass

def test_case_5():
    try:
        variable_manager_0 = module_0.VariableManager()
        str_0 = 'a$9x\tU\\XNkV+xQ@5OV'
        vars_with_sources_0 = None
        var_0 = variable_manager_0.set_host_facts(str_0, vars_with_sources_0)
    except BaseException:
        pass

def test_case_6():
    try:
        variable_manager_0 = module_0.VariableManager()
        dict_0 = {}
        var_0 = variable_manager_0.set_nonpersistent_facts(dict_0, dict_0)
    except BaseException:
        pass

def test_case_7():
    try:
        list_0 = []
        vars_with_sources_0 = module_0.VarsWithSources()
        int_0 = -1696
        tuple_0 = (vars_with_sources_0, int_0)
        vars_with_sources_1 = module_0.VarsWithSources(*list_0)
        var_0 = vars_with_sources_1.__setitem__(tuple_0, vars_with_sources_0)
    except BaseException:
        pass

def test_case_8():
    try:
        vars_with_sources_0 = module_0.VarsWithSources()
        int_0 = 1796
        var_0 = vars_with_sources_0.__delitem__(int_0)
    except BaseException:
        pass

def test_case_9():
    try:
        vars_with_sources_0 = module_0.VarsWithSources()
        var_0 = vars_with_sources_0.copy()
        str_0 = 'ENvADz7PM0ur'
        var_1 = vars_with_sources_0.__contains__(str_0)
        variable_manager_0 = module_0.VariableManager()
        var_2 = vars_with_sources_0.copy()
        vars_with_sources_1 = module_0.VarsWithSources()
        var_3 = vars_with_sources_0.__len__()
        var_4 = vars_with_sources_0.copy()
        var_5 = module_0.preprocess_vars(vars_with_sources_1)
        var_6 = variable_manager_0.clear_facts(variable_manager_0)
        str_1 = '`Z'
        str_2 = '{jW`$XIC77J;n"h}'
        var_7 = variable_manager_0.set_nonpersistent_facts(str_1, str_2)
    except BaseException:
        pass

def test_case_10():
    try:
        int_0 = 44
        var_0 = module_0.preprocess_vars(int_0)
    except BaseException:
        pass

def test_case_11():
    try:
        vars_with_sources_0 = module_0.VarsWithSources()
        var_0 = vars_with_sources_0.copy()
        dict_0 = {}
        variable_manager_0 = module_0.VariableManager()
        var_1 = vars_with_sources_0.copy()
        vars_with_sources_1 = module_0.VarsWithSources()
        var_2 = vars_with_sources_0.copy()
        list_0 = [dict_0, var_0, dict_0]
        var_3 = module_0.preprocess_vars(list_0)
        bool_0 = True
        var_4 = variable_manager_0.clear_facts(bool_0)
        float_0 = -202.41
        var_5 = variable_manager_0.set_nonpersistent_facts(float_0, list_0)
    except BaseException:
        pass

def test_case_12():
    try:
        variable_manager_0 = module_0.VariableManager()
        bool_0 = False
        dict_0 = None
        str_0 = "<dF$'0h=cu{#bef_lG8"
        float_0 = None
        tuple_0 = (dict_0, dict_0)
        complex_0 = None
        var_0 = variable_manager_0.set_host_variable(float_0, tuple_0, complex_0)
        str_1 = '.config'
        dict_1 = {str_1: tuple_0, str_0: bool_0}
        var_1 = variable_manager_0.set_host_facts(dict_1, dict_1)
    except BaseException:
        pass

def test_case_13():
    try:
        variable_manager_0 = None
        str_0 = 'R'
        variable_manager_1 = module_0.VariableManager()
        var_0 = variable_manager_1.set_host_variable(variable_manager_0, str_0, str_0)
        variable_manager_2 = module_0.VariableManager()
        var_1 = variable_manager_2.__getstate__()
        bool_0 = True
        dict_0 = None
        vars_with_sources_0 = module_0.VarsWithSources()
        var_2 = variable_manager_2.set_host_facts(dict_0, vars_with_sources_0)
        var_3 = vars_with_sources_0.__len__()
        var_4 = vars_with_sources_0.copy()
        var_5 = module_0.preprocess_vars(dict_0)
        bytes_0 = b'\xc0\xc2\x04\x05\x97\x9d\xef\x93\x9aY\x9e'
        var_6 = vars_with_sources_0.get_source(variable_manager_2)
        var_7 = variable_manager_2.clear_facts(bytes_0)
        str_1 = ''
        complex_0 = None
        host_0 = module_1.Host()
        var_8 = variable_manager_1.set_host_variable(complex_0, host_0, vars_with_sources_0)
        int_0 = 1372
        float_0 = -3228.0125
        list_0 = []
        tuple_0 = (list_0,)
        list_1 = [bool_0, tuple_0, str_1, var_5]
        var_9 = variable_manager_2.set_nonpersistent_facts(int_0, vars_with_sources_0)
        var_10 = variable_manager_2.set_host_facts(float_0, list_1)
    except BaseException:
        pass

def test_case_14():
    try:
        variable_manager_0 = None
        str_0 = 'chgroup'
        variable_manager_1 = module_0.VariableManager()
        var_0 = variable_manager_1.set_host_variable(variable_manager_0, str_0, str_0)
        variable_manager_2 = module_0.VariableManager()
        var_1 = variable_manager_2.__getstate__()
        dict_0 = None
        vars_with_sources_0 = module_0.VarsWithSources()
        var_2 = variable_manager_2.set_host_facts(dict_0, vars_with_sources_0)
        var_3 = vars_with_sources_0.__len__()
        var_4 = vars_with_sources_0.copy()
        var_5 = module_0.preprocess_vars(dict_0)
        bytes_0 = b'\xc0\xc2\x04\x05\x97\x9d\xef\x93\x9aY\x9e'
        var_6 = variable_manager_2.clear_facts(bytes_0)
        host_0 = module_1.Host()
        int_0 = 1372
        var_7 = vars_with_sources_0.__setitem__(dict_0, int_0)
        list_0 = []
        int_1 = 1542
        var_8 = variable_manager_2.set_nonpersistent_facts(int_1, vars_with_sources_0)
        dict_1 = {int_0: variable_manager_2, var_7: int_0}
        var_9 = variable_manager_2.set_nonpersistent_facts(list_0, dict_1)
    except BaseException:
        pass