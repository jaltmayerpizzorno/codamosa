# Automatically generated by Pynguin.
import ansible.config.manager as module_0

def test_case_0():
    pass

def test_case_1():
    config_manager_0 = module_0.ConfigManager()

def test_case_2():
    bytes_0 = b'\xdc\xda\x13\xc9\xa8='
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0, bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.get_ini_config_value(list_0, bytes_0)

def test_case_3():
    list_0 = None
    var_0 = module_0.find_ini_config_file(list_0)
    config_manager_0 = module_0.ConfigManager()

def test_case_4():
    list_0 = None
    config_manager_0 = module_0.ConfigManager()
    bool_0 = False
    var_0 = config_manager_0.get_plugin_vars(list_0, bool_0)

def test_case_5():
    list_0 = None
    config_manager_0 = module_0.ConfigManager()
    dict_0 = {list_0: list_0}
    var_0 = module_0.ensure_type(dict_0, list_0)
    bool_0 = True
    str_0 = 'C^,6'
    var_1 = module_0.get_ini_config_value(bool_0, str_0)
    var_2 = config_manager_0.get_plugin_vars(list_0, bool_0)
    int_0 = 266
    dict_1 = {}
    var_3 = config_manager_0.initialize_plugin_configuration_definitions(config_manager_0, list_0, dict_1)
    var_4 = module_0.find_ini_config_file()
    var_5 = config_manager_0.get_configuration_definition(int_0, bool_0)

def test_case_6():
    bytes_0 = b'Y\xafkCB\xd4\xad\x84J'
    var_0 = module_0.ensure_type(bytes_0, bytes_0)

def test_case_7():
    str_0 = '/foo/bar/ansible.cfg'
    var_0 = module_0.get_config_type(str_0)

def test_case_8():
    str_0 = '/foo/bar/ansible.cfg'
    var_0 = module_0.get_config_type(str_0)
    str_1 = '/foo/bar/ansible.yml'
    var_1 = module_0.get_config_type(str_1)
    str_2 = '/foo/bar/ansible.yaml'
    var_2 = module_0.get_config_type(str_2)