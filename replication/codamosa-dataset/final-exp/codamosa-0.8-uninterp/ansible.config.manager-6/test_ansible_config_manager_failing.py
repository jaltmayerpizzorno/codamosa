# Automatically generated by Pynguin.
import ansible.config.manager as module_0

def test_case_0():
    try:
        list_0 = None
        str_0 = 'Bfpalt'
        config_manager_0 = module_0.ConfigManager()
        var_0 = config_manager_0.get_config_value(list_0, str_0, config_manager_0)
    except BaseException:
        pass

def test_case_1():
    try:
        config_manager_0 = module_0.ConfigManager()
        var_0 = config_manager_0.get_configuration_definitions()
        plugin_0 = module_0.Plugin()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '~ Kq;,+F4TEab}3WLqA'
        config_manager_0 = module_0.ConfigManager(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        config_manager_0 = module_0.ConfigManager()
        list_0 = [config_manager_0, config_manager_0, config_manager_0, config_manager_0, config_manager_0, config_manager_0]
        str_0 = 'p_ce'
        dict_0 = {str_0: config_manager_0}
        bytes_0 = b'\x7fX\xeahe\x03Xy\r\xb1:_\xf6%\xe5'
        float_0 = 549.7959300378208
        var_0 = config_manager_0.get_configuration_definition(bytes_0, float_0)
        plugin_0 = module_0.Plugin(*list_0, **dict_0)
    except BaseException:
        pass

def test_case_4():
    try:
        list_0 = None
        config_manager_0 = module_0.ConfigManager()
        float_0 = -642.0
        str_0 = '@EvQWHF#Fb]{\tL\x0c7Y+C'
        var_0 = config_manager_0.get_configuration_definition(float_0)
        list_1 = [str_0, list_0, str_0]
        tuple_0 = (list_1,)
        int_0 = 127
        var_1 = module_0.get_ini_config_value(tuple_0, int_0)
        str_1 = '\x0b\n5}l~+(&2'
        var_2 = config_manager_0.get_config_value(list_0, str_1, config_manager_0)
    except BaseException:
        pass

def test_case_5():
    try:
        float_0 = None
        dict_0 = {float_0: float_0, float_0: float_0, float_0: float_0, float_0: float_0}
        list_0 = []
        dict_1 = None
        config_manager_0 = module_0.ConfigManager()
        var_0 = config_manager_0.get_config_value_and_origin(float_0, dict_0, list_0, dict_1)
    except BaseException:
        pass

def test_case_6():
    try:
        config_manager_0 = module_0.ConfigManager()
        str_0 = 'config_file'
        list_0 = [str_0, config_manager_0]
        var_0 = config_manager_0.get_config_value(list_0)
    except BaseException:
        pass

def test_case_7():
    try:
        int_0 = 631
        set_0 = {int_0, int_0}
        list_0 = [set_0, set_0, set_0, set_0]
        list_1 = [list_0, list_0]
        var_0 = module_0.resolve_path(list_1)
        dict_0 = {}
        config_manager_0 = module_0.ConfigManager(dict_0)
    except BaseException:
        pass

def test_case_8():
    try:
        list_0 = None
        str_0 = '@EvQWHF#Fb]{\tL\x0c7Y+C'
        list_1 = [str_0, list_0, str_0]
        tuple_0 = (list_1,)
        var_0 = module_0.find_ini_config_file()
        set_0 = set()
        config_manager_0 = module_0.ConfigManager()
        var_1 = config_manager_0.initialize_plugin_configuration_definitions(str_0, str_0, set_0)
        int_0 = 127
        var_2 = module_0.get_ini_config_value(tuple_0, int_0)
        config_manager_1 = module_0.ConfigManager()
        bool_0 = True
        var_3 = config_manager_0.update_config_data(set_0, bool_0)
    except BaseException:
        pass

def test_case_9():
    try:
        var_0 = module_0.find_ini_config_file()
        list_0 = [var_0, var_0, var_0]
        tuple_0 = ()
        config_manager_0 = module_0.ConfigManager()
        str_0 = 'd>1V'
        dict_0 = {str_0: list_0, var_0: config_manager_0, str_0: config_manager_0}
        var_1 = config_manager_0.get_config_value(tuple_0, dict_0)
    except BaseException:
        pass

def test_case_10():
    try:
        bool_0 = False
        config_manager_0 = module_0.ConfigManager(bool_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = '{FYY=hf!}`[Ix#g}AW\x0cC'
        float_0 = -245.09
        list_0 = [str_0, float_0, float_0]
        list_1 = [float_0, str_0]
        config_manager_0 = module_0.ConfigManager()
        config_manager_1 = module_0.ConfigManager(list_0, list_1)
    except BaseException:
        pass

def test_case_12():
    try:
        list_0 = None
        str_0 = '@EvQWHF#Fb]{\tL\x0c7Y+C'
        var_0 = module_0.find_ini_config_file()
        str_1 = '0'
        dict_0 = None
        var_1 = module_0.get_ini_config_value(dict_0, list_0)
        set_0 = set()
        config_manager_0 = module_0.ConfigManager()
        var_2 = config_manager_0.initialize_plugin_configuration_definitions(str_1, str_0, set_0)
        config_manager_1 = module_0.ConfigManager()
        config_manager_2 = module_0.ConfigManager()
        tuple_0 = ()
        config_manager_3 = module_0.ConfigManager(tuple_0)
    except BaseException:
        pass

def test_case_13():
    try:
        list_0 = None
        str_0 = '@EvQWHF#Fb]{\tL\x0c7Y+C'
        list_1 = [str_0, list_0, str_0]
        tuple_0 = (list_1,)
        int_0 = 127
        var_0 = module_0.get_ini_config_value(tuple_0, int_0)
        dict_0 = {str_0: list_0}
        config_manager_0 = module_0.ConfigManager()
        var_1 = config_manager_0.get_configuration_definitions()
        bytes_0 = None
        config_manager_1 = module_0.ConfigManager(bytes_0)
        dict_1 = None
        var_2 = config_manager_1.get_plugin_vars(dict_1, dict_0)
        config_manager_2 = module_0.ConfigManager(list_0)
        bool_0 = False
        var_3 = config_manager_2.get_configuration_definition(bool_0)
        config_manager_3 = module_0.ConfigManager()
        str_1 = '4\t'
        float_0 = -3492.1
        str_2 = 'x=YEazr a6tIln.'
        var_4 = config_manager_3.get_config_value(str_1, float_0, str_2, float_0)
    except BaseException:
        pass

def test_case_14():
    try:
        list_0 = None
        str_0 = '@EvQWHF#Fb]{\tL\x0c7Y+C'
        list_1 = [str_0, list_0, str_0]
        tuple_0 = (list_1,)
        int_0 = 127
        var_0 = module_0.get_ini_config_value(tuple_0, int_0)
        dict_0 = {str_0: list_0}
        bytes_0 = None
        config_manager_0 = module_0.ConfigManager(bytes_0)
        dict_1 = None
        var_1 = config_manager_0.get_plugin_vars(dict_1, dict_0)
        config_manager_1 = module_0.ConfigManager(list_0)
        var_2 = config_manager_0.get_configuration_definition(dict_1, tuple_0, list_1)
    except BaseException:
        pass

def test_case_15():
    try:
        list_0 = None
        str_0 = '@EvQWHF#Fb]{\tL\x0c7Y+C'
        list_1 = [str_0, list_0, str_0]
        tuple_0 = (list_1,)
        int_0 = 127
        var_0 = module_0.get_ini_config_value(tuple_0, int_0)
        dict_0 = {str_0: list_0}
        config_manager_0 = module_0.ConfigManager()
        var_1 = config_manager_0.get_configuration_definitions()
        bytes_0 = None
        config_manager_1 = module_0.ConfigManager(bytes_0)
        dict_1 = None
        var_2 = config_manager_1.get_plugin_vars(dict_1, dict_0)
        config_manager_2 = module_0.ConfigManager(list_0)
        str_1 = None
        var_3 = config_manager_2.get_configuration_definitions(str_1, bytes_0, str_0)
        float_0 = -737.3957
        var_4 = config_manager_2.get_configuration_definition(tuple_0, float_0)
    except BaseException:
        pass

def test_case_16():
    try:
        list_0 = None
        str_0 = '@EvQWHF#Fb]{\tL\x0c7Y+C'
        list_1 = [str_0, list_0, str_0]
        str_1 = '`ubW&'
        str_2 = None
        dict_0 = {str_1: list_1, str_2: list_1}
        config_manager_0 = module_0.ConfigManager()
        var_0 = config_manager_0.update_config_data(dict_0)
    except BaseException:
        pass