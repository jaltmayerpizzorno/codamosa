# Automatically generated by Pynguin.
import ansible.plugins.action.service as module_0

def test_case_0():
    try:
        int_0 = -932
        str_0 = 'check'
        str_1 = ''
        int_1 = 944
        tuple_0 = ()
        bytes_0 = b'\xb9'
        float_0 = -2301.1249
        float_1 = -3422.30599
        action_module_0 = module_0.ActionModule(str_1, int_1, tuple_0, bytes_0, float_0, float_1)
        str_2 = 'wyJ6M\x0cbo .^:zj<W\x0bH'
        bytes_1 = b']R\xd7*{`*)Q\xe4\xab\xaf\xe9\x0f6\xeb\xd7Y\x13'
        action_module_1 = module_0.ActionModule(int_0, str_0, action_module_0, str_2, bytes_1, tuple_0)
        var_0 = action_module_1.run()
    except BaseException:
        pass