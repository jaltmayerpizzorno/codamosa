# Automatically generated by Pynguin.
import ansible.config.manager as module_0

def test_case_0():
    pass

def test_case_1():
    config_manager_0 = module_0.ConfigManager()

def test_case_2():
    bool_0 = False
    int_0 = 12
    var_0 = module_0.get_ini_config_value(bool_0, int_0)

def test_case_3():
    complex_0 = None
    config_manager_0 = module_0.ConfigManager(complex_0)
    bool_0 = True
    var_0 = config_manager_0.get_configuration_definitions(bool_0, complex_0)

def test_case_4():
    str_0 = ''
    str_1 = 'test_path'
    config_manager_0 = module_0.ConfigManager()
    str_2 = 'test_plugin_type'
    str_3 = 'test_name'
    var_0 = config_manager_0.initialize_plugin_configuration_definitions(str_2, str_3, str_1)

def test_case_5():
    int_0 = 1647
    config_manager_0 = module_0.ConfigManager()
    str_0 = '1*$YID T\tn:TH'
    var_0 = config_manager_0.get_plugin_vars(str_0, int_0)
    bool_0 = True
    bool_1 = False
    var_1 = module_0.get_ini_config_value(bool_0, bool_1)
    config_manager_1 = module_0.ConfigManager()

def test_case_6():
    str_0 = 'test_path'
    config_manager_0 = module_0.ConfigManager()
    str_1 = 'test_name'
    str_2 = 'Lj+$<R,WWks0'
    var_0 = config_manager_0.initialize_plugin_configuration_definitions(str_1, str_1, str_2)
    bool_0 = True
    var_1 = config_manager_0.get_configuration_definitions(str_2, str_1, bool_0)