# Automatically generated by Pynguin.
import ansible.plugins.action.assert as module_0

def test_case_0():
    try:
        list_0 = []
        bool_0 = True
        tuple_0 = ()
        bytes_0 = b'$gf\x19A'
        dict_0 = {bytes_0: bool_0}
        action_module_0 = module_0.ActionModule(bool_0, tuple_0, bool_0, bool_0, bytes_0, dict_0)
        var_0 = action_module_0.run(list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        list_0 = []
        bool_0 = True
        tuple_0 = ()
        bool_1 = True
        bool_2 = True
        bytes_0 = b'$gf\x19A'
        dict_0 = {bytes_0: bool_2}
        action_module_0 = module_0.ActionModule(bool_0, tuple_0, bool_1, bool_2, bytes_0, dict_0)
        var_0 = action_module_0.run(tuple_0, list_0)
    except BaseException:
        pass