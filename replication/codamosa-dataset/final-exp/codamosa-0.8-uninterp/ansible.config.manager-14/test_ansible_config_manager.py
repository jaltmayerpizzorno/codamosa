# Automatically generated by Pynguin.
import ansible.config.manager as module_0

def test_case_0():
    config_manager_0 = module_0.ConfigManager()

def test_case_1():
    float_0 = 1033.85
    config_manager_0 = module_0.ConfigManager()
    var_0 = config_manager_0.initialize_plugin_configuration_definitions(float_0, config_manager_0, float_0)
    set_0 = None
    var_1 = config_manager_0.get_configuration_definition(set_0, config_manager_0, set_0)
    var_2 = config_manager_0.update_config_data()
    str_0 = 'float'
    int_0 = 119
    config_manager_1 = module_0.ConfigManager()
    var_3 = config_manager_1.get_plugin_options(str_0, int_0)
    config_manager_2 = module_0.ConfigManager()

def test_case_2():
    set_0 = None
    bool_0 = False
    str_0 = 'CBL#@ft@8/'
    tuple_0 = (bool_0, str_0, set_0)
    config_manager_0 = module_0.ConfigManager()
    var_0 = config_manager_0.get_plugin_vars(set_0, tuple_0)
    config_manager_1 = module_0.ConfigManager()

def test_case_3():
    config_manager_0 = module_0.ConfigManager()
    str_0 = 'svuF'
    var_0 = config_manager_0.get_configuration_definition(str_0)
    bool_0 = False
    var_1 = config_manager_0.get_configuration_definition(bool_0)
    config_manager_1 = module_0.ConfigManager()
    var_2 = config_manager_1.get_configuration_definitions()

def test_case_4():
    str_0 = '=jN9jE{;|qM>^KuSw'
    bytes_0 = b'\xff4\xd8\x14\xb2\xf0H\xa3\xa8Y\xab\x96W'
    list_0 = [bytes_0]
    var_0 = module_0.get_ini_config_value(str_0, list_0)