# Automatically generated by Pynguin.
import ansible.config.manager as module_0

def test_case_0():
    try:
        str_0 = 'e5'
        str_1 = 'default'
        tuple_0 = None
        float_0 = 169.6881
        list_0 = [tuple_0, tuple_0, float_0, str_1]
        config_manager_0 = module_0.ConfigManager()
        var_0 = config_manager_0.get_plugin_options(tuple_0, float_0, list_0)
        list_1 = [str_1, float_0, str_0, str_0]
        str_2 = 'Sun Microsystems'
        var_1 = config_manager_0.get_config_value(float_0, list_1, str_2, float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = 1883.723
        config_manager_0 = module_0.ConfigManager()
        config_manager_1 = module_0.ConfigManager()
        var_0 = config_manager_1.get_config_value(float_0, config_manager_0)
    except BaseException:
        pass

def test_case_2():
    try:
        config_manager_0 = module_0.ConfigManager()
        bool_0 = False
        config_manager_1 = module_0.ConfigManager(bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '\x0c_kT6]d)Kd)V~Tz9VI}'
        var_0 = module_0.get_config_type(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '1snYB\x0bMMiqIIHV'
        dict_0 = {str_0: str_0}
        config_manager_0 = module_0.ConfigManager(dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        config_manager_0 = module_0.ConfigManager()
        list_0 = [config_manager_0]
        str_0 = '\nHo3""'
        dict_0 = {}
        var_0 = config_manager_0.get_config_value(list_0, str_0, dict_0)
    except BaseException:
        pass

def test_case_6():
    try:
        setting_0 = None
        config_manager_0 = module_0.ConfigManager()
        var_0 = config_manager_0.update_config_data()
        int_0 = 69
        list_0 = [setting_0]
        var_1 = config_manager_0.initialize_plugin_configuration_definitions(int_0, list_0, config_manager_0)
    except BaseException:
        pass

def test_case_7():
    try:
        bool_0 = False
        tuple_0 = ()
        config_manager_0 = module_0.ConfigManager(bool_0, tuple_0)
    except BaseException:
        pass

def test_case_8():
    try:
        float_0 = 1883.723
        setting_0 = None
        config_manager_0 = module_0.ConfigManager()
        var_0 = config_manager_0.get_plugin_vars(float_0, setting_0)
        var_1 = config_manager_0.get_config_value(float_0, var_0, float_0)
    except BaseException:
        pass

def test_case_9():
    try:
        float_0 = 1883.723
        config_manager_0 = module_0.ConfigManager()
        set_0 = {float_0, float_0}
        list_0 = [config_manager_0, set_0, config_manager_0, config_manager_0]
        tuple_0 = (set_0, set_0, list_0, list_0)
        bytes_0 = None
        var_0 = module_0.ensure_type(tuple_0, bytes_0)
        setting_0 = None
        var_1 = config_manager_0.update_config_data(setting_0)
        config_manager_1 = module_0.ConfigManager()
        var_2 = config_manager_0.get_plugin_vars(float_0, setting_0)
        var_3 = config_manager_1.get_config_value(float_0, config_manager_0)
    except BaseException:
        pass

def test_case_10():
    try:
        float_0 = 1875.1075578169534
        set_0 = {float_0, float_0}
        bool_0 = True
        config_manager_0 = module_0.ConfigManager()
        str_0 = '1|hg}JIxGY66'
        int_0 = 1797
        var_0 = config_manager_0.get_configuration_definition(str_0, int_0)
        str_1 = '('
        complex_0 = None
        float_1 = 502.84183052377324
        dict_0 = None
        var_1 = module_0.get_ini_config_value(dict_0, set_0)
        dict_1 = {str_1: config_manager_0, str_1: var_0, float_1: bool_0, config_manager_0: config_manager_0}
        var_2 = config_manager_0.get_plugin_options(complex_0, set_0, complex_0, dict_1, float_0)
    except BaseException:
        pass

def test_case_11():
    try:
        bool_0 = True
        config_manager_0 = module_0.ConfigManager()
        config_manager_1 = module_0.ConfigManager(bool_0, config_manager_0)
    except BaseException:
        pass

def test_case_12():
    try:
        float_0 = 1883.723
        config_manager_0 = module_0.ConfigManager()
        setting_0 = None
        config_manager_1 = module_0.ConfigManager()
        var_0 = config_manager_1.get_plugin_vars(float_0, setting_0)
        str_0 = ''
        var_1 = config_manager_1.update_config_data(str_0, config_manager_1)
    except BaseException:
        pass

def test_case_13():
    try:
        config_manager_0 = module_0.ConfigManager()
        dict_0 = {config_manager_0: config_manager_0, config_manager_0: config_manager_0, config_manager_0: config_manager_0, config_manager_0: config_manager_0}
        list_0 = [config_manager_0]
        var_0 = config_manager_0.update_config_data(dict_0, list_0)
    except BaseException:
        pass

def test_case_14():
    try:
        bool_0 = False
        str_0 = 'I];'
        bool_1 = False
        str_1 = None
        str_2 = None
        dict_0 = {str_0: bool_1, str_1: str_0, str_2: bool_1}
        config_manager_0 = module_0.ConfigManager()
        var_0 = config_manager_0.get_configuration_definition(bool_0, dict_0, dict_0)
    except BaseException:
        pass

def test_case_15():
    try:
        float_0 = 1875.1075578169534
        set_0 = {float_0, float_0}
        bool_0 = True
        config_manager_0 = module_0.ConfigManager()
        str_0 = '1|hg}JIxGY66'
        int_0 = 1785
        var_0 = config_manager_0.get_configuration_definition(str_0, int_0)
        str_1 = '('
        complex_0 = None
        float_1 = 512.0
        dict_0 = {str_1: config_manager_0, str_1: var_0, float_1: bool_0, config_manager_0: config_manager_0}
        var_1 = config_manager_0.get_plugin_options(complex_0, set_0, complex_0, dict_0, float_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = 'foo.ini'
        var_0 = module_0.get_config_type(str_0)
        str_1 = 'foo.cfg'
        var_1 = module_0.get_config_type(str_1)
        str_2 = 'foo.yaml'
        var_2 = module_0.get_config_type(str_2)
        str_3 = 'foo.yml'
        var_3 = module_0.get_config_type(str_3)
        str_4 = 'foo.xml'
        var_4 = module_0.get_config_type(str_4)
    except BaseException:
        pass