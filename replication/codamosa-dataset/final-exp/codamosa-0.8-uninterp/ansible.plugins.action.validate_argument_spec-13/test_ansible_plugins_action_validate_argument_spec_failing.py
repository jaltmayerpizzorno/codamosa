# Automatically generated by Pynguin.
import ansible.plugins.action.validate_argument_spec as module_0

def test_case_0():
    try:
        set_0 = set()
        str_0 = 'Mini Tower'
        str_1 = None
        bool_0 = False
        list_0 = []
        action_module_0 = module_0.ActionModule(set_0, str_0, str_1, str_1, bool_0, list_0)
        int_0 = 63
        var_0 = action_module_0.get_args_from_task_vars(action_module_0, int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = -446
        str_0 = "FS\x0cB\x0bn'2HdJytLk38i`\x0b"
        bool_0 = False
        bytes_0 = b'\xb4\xce\xf4\xa9\x1e\x03\xac\xc1\xb4\x00\x915a:\x06'
        dict_0 = {int_0: str_0, bool_0: bytes_0}
        list_0 = [bytes_0]
        bool_1 = True
        set_0 = set()
        list_1 = [bytes_0, str_0, str_0, set_0]
        dict_1 = {}
        action_module_0 = module_0.ActionModule(str_0, bool_1, set_0, list_1, dict_1, str_0)
        var_0 = action_module_0.get_args_from_task_vars(dict_0, list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = "FS\x0cB\x0bn'2HdJytLk38i`\x0b"
        bytes_0 = b'\xb4\xce\xf4\xa9\x1e\x03\xac\xc1\xb4\x00\x915a:\x06'
        list_0 = [bytes_0]
        bool_0 = True
        set_0 = set()
        list_1 = [bytes_0, str_0, str_0, set_0]
        dict_0 = {}
        action_module_0 = module_0.ActionModule(str_0, bool_0, set_0, list_1, dict_0, str_0)
        var_0 = action_module_0.get_args_from_task_vars(dict_0, list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        list_0 = []
        str_0 = 'FX8c6'
        action_module_0 = module_0.ActionModule(str_0, str_0, str_0, list_0, str_0, str_0)
        var_0 = action_module_0.run()
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = True
        bytes_0 = b'\xc2h\xfbf-o\xd8'
        int_0 = 43
        bool_1 = False
        bytes_1 = b'#\x91\xdb\xb2u\x96 l'
        list_0 = [bytes_1, bytes_1, bytes_1, bytes_1]
        str_0 = 'sv'
        tuple_0 = ()
        str_1 = 'cacheable'
        bool_2 = False
        str_2 = ']32d|I'
        bytes_2 = b'9,K\\2\xf5\x05\xbe\xc2a\x1e\x02\xdd4\x8f\xa4\x19'
        dict_0 = None
        int_1 = 1494
        action_module_0 = module_0.ActionModule(bool_2, str_2, bytes_2, dict_0, bytes_2, int_1)
        float_0 = -507.0
        str_3 = ''
        set_0 = set()
        action_module_1 = module_0.ActionModule(action_module_0, float_0, str_3, list_0, set_0, dict_0)
        action_module_2 = module_0.ActionModule(tuple_0, str_1, list_0, list_0, action_module_1, int_1)
        action_module_3 = module_0.ActionModule(list_0, list_0, bytes_0, str_0, int_0, action_module_2)
        bytes_3 = b'\xfd\xf8$'
        float_1 = 614.0
        dict_1 = {int_0: bytes_3, int_0: bytes_3, bool_1: float_1, bytes_0: bytes_3}
        str_4 = '/'
        action_module_4 = module_0.ActionModule(bool_0, bytes_0, int_0, bool_1, dict_1, str_4)
        str_5 = '"FOI|A"I2I\tn\t=j5Bj1A'
        bool_3 = True
        bytes_4 = b'\xd4\xb4\x1f\x9ei=\xff\x03n\xc2\x95\xb6\x16\x9f\xce\xc8'
        set_1 = {int_0, bool_3, str_5, action_module_4}
        str_6 = "-WZ@AZU'r.Y"
        dict_2 = {str_6: float_1, bytes_4: bool_0}
        list_1 = [bytes_0, str_5]
        tuple_1 = (str_6, bool_0, dict_2, list_1)
        action_module_5 = module_0.ActionModule(bool_3, bytes_4, set_1, bytes_4, int_0, tuple_1)
        var_0 = action_module_0.run(action_module_2, tuple_1)
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = -446
        str_0 = "FS\x0cB\x0bn'2HdJytLk38i`\x0b"
        bool_0 = False
        bytes_0 = b'\xb4\xce\xf4\xa9\x1e\x03\xac\xc1\xb4\x00\x915a:\x06'
        dict_0 = {int_0: int_0, bytes_0: bool_0, int_0: str_0}
        list_0 = [bytes_0]
        bool_1 = True
        set_0 = set()
        list_1 = [bytes_0, str_0, str_0, set_0]
        dict_1 = {}
        action_module_0 = module_0.ActionModule(str_0, bool_1, set_0, list_1, dict_1, str_0)
        var_0 = action_module_0.get_args_from_task_vars(dict_0, list_0)
    except BaseException:
        pass