# Automatically generated by Pynguin.
import ansible.config.data as module_0

def test_case_0():
    try:
        str_0 = ':'
        str_1 = 'r6p,VPO&]:Q{Pg\x0chY'
        config_data_0 = module_0.ConfigData()
        var_0 = config_data_0.get_setting(str_0, str_1)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = -2535.1498
        list_0 = [float_0]
        config_data_0 = module_0.ConfigData()
        var_0 = config_data_0.get_setting(list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        config_data_0 = module_0.ConfigData()
        var_0 = config_data_0.get_settings()
        str_0 = 'l6}q^66;vP0'
        var_1 = config_data_0.get_settings(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'4`\x89'
        config_data_0 = module_0.ConfigData()
        var_0 = config_data_0.update_setting(bytes_0, bytes_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = False
        config_data_0 = module_0.ConfigData()
        var_0 = config_data_0.update_setting(bool_0)
    except BaseException:
        pass