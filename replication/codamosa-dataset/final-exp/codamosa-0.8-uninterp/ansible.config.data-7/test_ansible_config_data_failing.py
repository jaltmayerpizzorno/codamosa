# Automatically generated by Pynguin.
import ansible.config.data as module_0

def test_case_0():
    try:
        config_data_0 = module_0.ConfigData()
        bool_0 = True
        config_data_1 = module_0.ConfigData()
        var_0 = config_data_1.get_setting(config_data_0, bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        config_data_0 = module_0.ConfigData()
        int_0 = 1984
        dict_0 = {config_data_0: config_data_0, config_data_0: config_data_0, config_data_0: int_0}
        var_0 = config_data_0.get_setting(dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        config_data_0 = module_0.ConfigData()
        var_0 = config_data_0.get_setting(config_data_0)
        bool_0 = True
        var_1 = config_data_0.get_setting(config_data_0, bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        config_data_0 = module_0.ConfigData()
        var_0 = config_data_0.get_settings()
        float_0 = 142.49
        var_1 = config_data_0.get_settings(float_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = None
        str_0 = '--enablerepo=%s'
        config_data_0 = module_0.ConfigData()
        var_0 = config_data_0.update_setting(bool_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        config_data_0 = module_0.ConfigData()
        var_0 = config_data_0.update_setting(config_data_0)
    except BaseException:
        pass