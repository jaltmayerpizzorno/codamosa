# Automatically generated by Pynguin.
import ansible.config.manager as module_0

def test_case_0():
    config_manager_0 = module_0.ConfigManager()

def test_case_1():
    var_0 = module_0.find_ini_config_file()

def test_case_2():
    config_manager_0 = module_0.ConfigManager()
    int_0 = None
    var_0 = config_manager_0.get_plugin_vars(int_0, config_manager_0)

def test_case_3():
    str_0 = '(%1G!-s^f'
    str_1 = 'some_def'
    bool_0 = True
    config_manager_0 = module_0.ConfigManager()
    var_0 = config_manager_0.initialize_plugin_configuration_definitions(str_0, str_1, bool_0)

def test_case_4():
    setting_0 = None
    float_0 = 0.1
    str_0 = 'tmppath'
    tuple_0 = (float_0, str_0, str_0)
    str_1 = 'amd64'
    config_manager_0 = module_0.ConfigManager()
    var_0 = config_manager_0.get_plugin_options(setting_0, tuple_0, str_1)
    config_manager_1 = module_0.ConfigManager()

def test_case_5():
    bytes_0 = b'\xd3\xe0Ms\xd9_\x82W6'
    config_manager_0 = module_0.ConfigManager()
    config_manager_1 = module_0.ConfigManager()
    int_0 = -3634
    str_0 = '\tgnW0\x0b\x0c;r.'
    var_0 = config_manager_0.get_configuration_definition(int_0, str_0)
    str_1 = 'CloudLinux'
    var_1 = module_0.resolve_path(str_1)
    var_2 = config_manager_1.get_plugin_vars(bytes_0, config_manager_0)
    bytes_1 = b'\xc6\xa3'
    var_3 = module_0.get_ini_config_value(config_manager_1, bytes_1)
    list_0 = None
    bytes_2 = b'\x8e\x89'
    var_4 = config_manager_1.get_plugin_vars(list_0, bytes_2)