# Automatically generated by Pynguin.
import ansible.config.data as module_0

def test_case_0():
    try:
        float_0 = None
        str_0 = "9&AqZ084\x0b6zK6,Q'n"
        config_data_0 = module_0.ConfigData()
        var_0 = config_data_0.get_setting(float_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = ''
        set_0 = {str_0, str_0}
        config_data_0 = module_0.ConfigData()
        var_0 = config_data_0.get_setting(set_0)
    except BaseException:
        pass

def test_case_2():
    try:
        config_data_0 = module_0.ConfigData()
        float_0 = 518.0
        var_0 = config_data_0.get_setting(float_0)
        int_0 = -364
        var_1 = config_data_0.get_setting(int_0, config_data_0)
    except BaseException:
        pass

def test_case_3():
    try:
        config_data_0 = module_0.ConfigData()
        var_0 = config_data_0.get_settings()
        float_0 = 502.69284
        var_1 = config_data_0.get_settings(float_0)
    except BaseException:
        pass

def test_case_4():
    try:
        config_data_0 = module_0.ConfigData()
        var_0 = config_data_0.get_settings()
        config_data_1 = module_0.ConfigData()
        bool_0 = True
        str_0 = 'l]7O'
        var_1 = config_data_0.update_setting(bool_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        complex_0 = None
        config_data_0 = module_0.ConfigData()
        var_0 = config_data_0.update_setting(complex_0)
    except BaseException:
        pass