# Automatically generated by Pynguin.
import ansible.template.safe_eval as module_0

def test_case_0():
    try:
        str_0 = "{'foo': 'bar'}"
        var_0 = module_0.safe_eval(str_0)
        str_1 = '[1, 2, 3]'
        var_1 = module_0.safe_eval(str_1)
        str_2 = '3 + 4'
        var_2 = module_0.safe_eval(str_2)
        str_3 = 'Fd_'
        int_0 = 472
        var_3 = module_0.safe_eval(str_3, str_0, int_0)
        str_4 = 'None'
        var_4 = module_0.safe_eval(str_4)
        str_5 = 'undefined_variable'
        int_1 = 42
        int_2 = {str_5: int_1}
        var_5 = module_0.safe_eval(str_5, int_2)
        int_3 = 1
        str_6 = "open('/etc/passwd')"
        bool_0 = True
        var_6 = safe_eval(str_6, include_exceptions=bool_0)[int_3]
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = "{'foo': 'bar'}"
        var_0 = module_0.safe_eval(str_0)
        str_1 = '[1, 2, 3]'
        var_1 = module_0.safe_eval(str_1)
        str_2 = '3 + 4'
        var_2 = module_0.safe_eval(str_0, var_0, str_2)
        str_3 = 'Jrue and False'
        var_3 = module_0.safe_eval(str_3)
        str_4 = 'undefinedvariable'
        int_0 = 42
        int_1 = {str_4: int_0}
        var_4 = module_0.safe_eval(str_4, int_1)
        int_2 = 1
        str_5 = "open('/etc/passwd')"
        bool_0 = True
        var_5 = safe_eval(str_5, include_exceptions=bool_0)[int_2]
    except BaseException:
        pass