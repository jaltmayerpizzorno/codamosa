# Automatically generated by Pynguin.
import ansible.plugins.action.copy as module_0

def test_case_0():
    try:
        tuple_0 = ()
        bool_0 = True
        set_0 = set()
        str_0 = '!tK)oTcf4+@'
        list_0 = []
        int_0 = 4096
        bytes_0 = b'\x06\xd9\x96\xd6\xbe\xfc\xae\x1b\x9d\xa5\xc1e\xa1\x8d>\x03Q'
        action_module_0 = module_0.ActionModule(tuple_0, str_0, list_0, int_0, bytes_0, bytes_0)
        action_module_1 = module_0.ActionModule(tuple_0, bool_0, set_0, set_0, action_module_0, int_0)
        var_0 = action_module_1.run()
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 25
        set_0 = {int_0, int_0}
        tuple_0 = (set_0,)
        float_0 = 829.52
        list_0 = [float_0, float_0]
        bool_0 = False
        str_0 = "]RNRy,2.'h7Sc~J?G} \x0c"
        bytes_0 = b'Yo'
        action_module_0 = module_0.ActionModule(float_0, list_0, bool_0, str_0, float_0, bytes_0)
        var_0 = action_module_0.run(tuple_0, set_0)
    except BaseException:
        pass