# Automatically generated by Pynguin.
import ansible.plugins.action.fetch as module_0

def test_case_0():
    try:
        bool_0 = False
        dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
        bytes_0 = b'\r\x07U\x03\x87\xd4~c\xef\xc9\xfb'
        set_0 = {bytes_0, bytes_0, bytes_0, bytes_0}
        bytes_1 = b'H\xd3])${\xd0'
        list_0 = [bytes_1, bytes_1, set_0, bytes_1]
        bytes_2 = b'\xa9\xa5d\xdaw\x8d\xec;&\xe9&p3\xed\xe1\xf4\xdc\x9e\x96'
        bool_1 = False
        action_module_0 = module_0.ActionModule(bytes_0, set_0, list_0, bytes_2, list_0, bool_1)
        var_0 = action_module_0.run(dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'WDv(%UC6DO/iE8z'
        tuple_0 = None
        tuple_1 = None
        bytes_0 = None
        bytes_1 = b''
        set_0 = {bytes_0, bytes_1, tuple_0}
        dict_0 = {bytes_0: set_0}
        bool_0 = False
        float_0 = 1880.78857
        list_0 = []
        bytes_2 = b'\x804N\r\xde.H\xc4\x9e\x18<-|M\xcc\xf5V\xd0\x0b'
        int_0 = -222
        str_1 = '7pz)vWsAM'
        action_module_0 = module_0.ActionModule(float_0, float_0, list_0, int_0, str_1, dict_0)
        float_1 = 4871.552382
        action_module_1 = module_0.ActionModule(bool_0, action_module_0, dict_0, float_1, bool_0, int_0)
        int_1 = 40
        str_2 = 'root'
        action_module_2 = module_0.ActionModule(bytes_1, bytes_2, tuple_1, action_module_1, int_1, str_2)
        action_module_3 = module_0.ActionModule(str_0, bool_0, float_0, list_0, dict_0, action_module_2)
        var_0 = action_module_3.run(dict_0, dict_0)
    except BaseException:
        pass