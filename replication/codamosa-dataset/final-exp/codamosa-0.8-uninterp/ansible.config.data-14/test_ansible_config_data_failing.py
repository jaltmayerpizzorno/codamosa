# Automatically generated by Pynguin.
import ansible.config.data as module_0

def test_case_0():
    try:
        config_data_0 = module_0.ConfigData()
        bool_0 = True
        var_0 = config_data_0.get_setting(bool_0)
        str_0 = 'inventory'
        var_1 = config_data_0.get_setting(str_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        config_data_0 = module_0.ConfigData()
        str_0 = 'changes'
        var_0 = config_data_0.get_settings()
        var_1 = config_data_0.get_settings(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        config_data_0 = module_0.ConfigData()
        bool_0 = False
        var_0 = config_data_0.get_settings()
        var_1 = config_data_0.get_setting(bool_0)
        var_2 = config_data_0.get_settings()
        float_0 = 2.0
        var_3 = config_data_0.update_setting(float_0, config_data_0)
    except BaseException:
        pass

def test_case_3():
    try:
        config_data_0 = module_0.ConfigData()
        var_0 = config_data_0.update_setting(config_data_0)
    except BaseException:
        pass