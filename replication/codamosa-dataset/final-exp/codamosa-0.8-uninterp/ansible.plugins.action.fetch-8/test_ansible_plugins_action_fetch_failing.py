# Automatically generated by Pynguin.
import ansible.plugins.action.fetch as module_0

def test_case_0():
    try:
        str_0 = 'V\x0bhhm/d'
        str_1 = 'Qv)~U<eL\x0b;gZa'
        list_0 = [str_1]
        dict_0 = {str_1: list_0, str_1: list_0, str_1: str_1}
        float_0 = 0.001
        int_0 = -689
        action_module_0 = module_0.ActionModule(str_1, list_0, dict_0, float_0, int_0, str_1)
        var_0 = action_module_0.run(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = -2006
        float_0 = -1646.447
        str_0 = 'M^GT[4q\x0b\t+STw6$\x0bV'
        bytes_0 = b'\xd6#\x9ddqI\xae\xeaB\xe1'
        bool_0 = True
        dict_0 = {}
        bool_1 = True
        tuple_0 = (str_0, bool_1)
        tuple_1 = (bool_1, bytes_0, tuple_0)
        float_1 = 441.749
        str_1 = '/\x0bBA%~{37\tF$>u'
        action_module_0 = module_0.ActionModule(bytes_0, bool_0, dict_0, tuple_1, float_1, str_1)
        int_1 = -1169
        bool_2 = False
        bool_3 = False
        action_module_1 = module_0.ActionModule(str_0, action_module_0, int_1, bytes_0, bool_2, bool_3)
        var_0 = action_module_1.run(int_0, float_0)
    except BaseException:
        pass