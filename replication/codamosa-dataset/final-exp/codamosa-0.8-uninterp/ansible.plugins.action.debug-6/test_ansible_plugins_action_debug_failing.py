# Automatically generated by Pynguin.
import ansible.plugins.action.debug as module_0

def test_case_0():
    try:
        bool_0 = False
        float_0 = 1156.14891
        bool_1 = False
        dict_0 = {bool_0: bool_1}
        float_1 = -1265.341547
        tuple_0 = (float_1,)
        action_module_0 = module_0.ActionModule(bool_0, float_0, bool_1, dict_0, tuple_0, dict_0)
        var_0 = action_module_0.run()
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'U&$\xb9\xfd\x1fWV\xc9\xb6;\xf6'
        tuple_0 = (bytes_0,)
        int_0 = -3270
        str_0 = '&JZ\r\rBH(w9'
        bool_0 = True
        float_0 = 2695.5
        str_1 = '4JN4BJn9>d/N,*B(/S@'
        bool_1 = False
        list_0 = [bytes_0, bytes_0]
        action_module_0 = module_0.ActionModule(bool_1, tuple_0, bool_0, float_0, float_0, list_0)
        action_module_1 = module_0.ActionModule(str_0, int_0, bool_0, tuple_0, float_0, str_1)
        str_2 = '4V``rZHsiuaiXig5e\n'
        action_module_2 = module_0.ActionModule(action_module_1, str_1, bool_0, int_0, str_2, bytes_0)
        var_0 = action_module_2.run(tuple_0, tuple_0)
    except BaseException:
        pass