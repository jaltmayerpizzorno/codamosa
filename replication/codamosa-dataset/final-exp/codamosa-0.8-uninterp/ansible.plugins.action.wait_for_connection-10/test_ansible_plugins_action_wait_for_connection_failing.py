# Automatically generated by Pynguin.
import ansible.plugins.action.wait_for_connection as module_0

def test_case_0():
    try:
        str_0 = '6;wi,%t/Ik.v`zxa'
        dict_0 = {str_0: str_0, str_0: str_0}
        bool_0 = False
        str_1 = 'bckrefs'
        float_0 = 1473.68
        bool_1 = True
        list_0 = [dict_0, float_0, float_0]
        str_2 = 'Positional arguments: %s'
        bytes_0 = b'\xd6'
        dict_1 = {}
        action_module_0 = module_0.ActionModule(str_2, bool_0, bytes_0, str_1, dict_1, dict_0)
        var_0 = action_module_0.do_until_success_or_timeout(float_0, bool_1, list_0, float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'2\xad\x01:\xec\x1a\x9c\x1d\x16/1\xcf\xa9'
        list_0 = [bytes_0, bytes_0]
        timed_out_exception_0 = module_0.TimedOutException()
        int_0 = 128
        bytes_1 = b'\xae\xd8\xe9<\xab\x88GY\x9a\xab'
        bytes_2 = b'\x1c>\xe3\xcdh8\t\x88i\xf2l\xa4\x94\x00\xc4\xabg\xae'
        action_module_0 = module_0.ActionModule(bytes_0, list_0, timed_out_exception_0, int_0, bytes_1, bytes_2)
        var_0 = action_module_0.run()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '6;wi,%t/Ik.v`zxa'
        dict_0 = {str_0: str_0, str_0: str_0}
        bool_0 = False
        float_0 = 365.54
        str_1 = 'backrefs'
        str_2 = "\\g'Q4#3ad)f6C3"
        dict_1 = {}
        list_0 = [str_1, dict_1, dict_1, dict_1]
        bool_1 = False
        int_0 = 384
        str_3 = 'U1f4@K'
        str_4 = '.|mnJ'
        str_5 = 'Y_=CK $gXD5N@S'
        list_1 = [str_5, str_1]
        action_module_0 = module_0.ActionModule(bool_1, int_0, str_3, str_4, str_5, list_1)
        bytes_0 = b'\xabo3)\x06\xf2$#J\xcb\x02\x97\xb0'
        tuple_0 = ()
        dict_2 = {}
        action_module_1 = module_0.ActionModule(list_0, action_module_0, bytes_0, tuple_0, dict_1, dict_2)
        action_module_2 = module_0.ActionModule(str_1, str_2, str_2, dict_1, action_module_1, bool_1)
        var_0 = action_module_2.do_until_success_or_timeout(dict_0, bool_0, float_0, dict_0, bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        action_module_0 = None
        bytes_0 = b'\xafS1\x88\xb7AU\xb1\x0c)'
        str_0 = 'yT;G+X*aJ\x0c?{u?'
        str_1 = '8'
        dict_0 = {str_0: str_0, str_1: str_1, str_1: str_1}
        bool_0 = True
        dict_1 = {str_1: dict_0}
        bool_1 = False
        bytes_1 = b'*%\xcc\xe1F\xd6'
        action_module_1 = module_0.ActionModule(dict_0, bool_0, dict_1, bool_1, bytes_1, dict_1)
        var_0 = action_module_1.run(action_module_0, bytes_0)
    except BaseException:
        pass