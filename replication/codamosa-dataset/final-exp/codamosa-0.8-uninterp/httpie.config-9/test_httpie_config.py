# Automatically generated by Pynguin.
import httpie.config as module_0
import pathlib as module_1

def test_case_0():
    pass

def test_case_1():
    config_0 = module_0.Config()

def test_case_2():
    path_0 = module_1.Path()
    base_config_dict_0 = module_0.BaseConfigDict(path_0)
    bool_0 = base_config_dict_0.is_new()

def test_case_3():
    config_file_error_0 = module_0.ConfigFileError()
    path_0 = module_0.get_default_config_dir()
    base_config_dict_0 = module_0.BaseConfigDict(path_0)
    var_0 = base_config_dict_0.save()
    var_1 = path_0.is_socket()
    base_config_dict_1 = module_0.BaseConfigDict(path_0)
    base_config_dict_2 = module_0.BaseConfigDict(path_0)
    var_2 = base_config_dict_2.load()
    bool_0 = base_config_dict_2.is_new()
    var_3 = base_config_dict_2.ensure_directory()
    base_config_dict_3 = module_0.BaseConfigDict(path_0)
    bool_1 = base_config_dict_2.is_new()
    bool_2 = base_config_dict_2.is_new()
    config_0 = module_0.Config()
    config_file_error_1 = module_0.ConfigFileError()
    var_4 = base_config_dict_2.delete()

def test_case_4():
    str_0 = 'YV3% 5'
    str_1 = '--version'
    path_0 = module_0.get_default_config_dir()
    base_config_dict_0 = module_0.BaseConfigDict(path_0)
    var_0 = base_config_dict_0.load()
    str_2 = '+`o(Qz\x0b)q@'
    dict_0 = {str_0: str_0, str_1: str_0, str_1: str_1, str_2: str_1}
    path_1 = module_0.get_default_config_dir()
    base_config_dict_1 = module_0.BaseConfigDict(path_1)
    var_1 = base_config_dict_1.save()
    path_2 = module_1.Path(**dict_0)
    base_config_dict_2 = module_0.BaseConfigDict(path_2)
    var_2 = base_config_dict_2.ensure_directory()
    var_3 = base_config_dict_2.ensure_directory()

def test_case_5():
    config_0 = module_0.Config()
    path_0 = module_1.Path()
    base_config_dict_0 = module_0.BaseConfigDict(path_0)
    var_0 = base_config_dict_0.save(config_0)
    config_1 = module_0.Config()
    var_1 = config_1.save(config_1)

def test_case_6():
    path_0 = module_0.get_default_config_dir()
    base_config_dict_0 = module_0.BaseConfigDict(path_0)
    bool_0 = base_config_dict_0.is_new()
    base_config_dict_1 = module_0.BaseConfigDict(path_0)
    config_0 = module_0.Config()
    base_config_dict_2 = module_0.BaseConfigDict(path_0)
    var_0 = base_config_dict_2.delete()
    bool_1 = base_config_dict_1.is_new()
    var_1 = base_config_dict_1.save()