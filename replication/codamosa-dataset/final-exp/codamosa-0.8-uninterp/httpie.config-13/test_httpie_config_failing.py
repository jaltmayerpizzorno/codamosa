# Automatically generated by Pynguin.
import pathlib as module_0
import httpie.config as module_1

def test_case_0():
    try:
        path_0 = module_0.Path()
        base_config_dict_0 = module_1.BaseConfigDict(path_0)
        var_0 = base_config_dict_0.save()
    except BaseException:
        pass

def test_case_1():
    try:
        path_0 = module_1.get_default_config_dir()
        base_config_dict_0 = module_1.BaseConfigDict(path_0)
        var_0 = path_0.touch()
        var_1 = base_config_dict_0.load()
    except BaseException:
        pass

def test_case_2():
    try:
        path_0 = module_0.Path()
        base_config_dict_0 = module_1.BaseConfigDict(path_0)
        var_0 = base_config_dict_0.load()
    except BaseException:
        pass

def test_case_3():
    try:
        path_0 = module_1.get_default_config_dir()
        base_config_dict_0 = module_1.BaseConfigDict(path_0)
        bool_0 = base_config_dict_0.is_new()
        bool_1 = base_config_dict_0.is_new()
        str_0 = 'password'
        str_1 = 'q4sA2u^I'
        var_0 = base_config_dict_0.delete()
        dict_0 = {str_0: bool_0, str_0: base_config_dict_0, str_1: str_0}
        var_1 = base_config_dict_0.save()
        var_2 = path_0.replace(dict_0)
    except BaseException:
        pass

def test_case_4():
    try:
        path_0 = module_1.get_default_config_dir()
        config_file_error_0 = module_1.ConfigFileError()
        path_1 = module_0.Path()
        base_config_dict_0 = module_1.BaseConfigDict(path_1)
        var_0 = base_config_dict_0.delete()
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'WVZdM<z,+zqK%'
        config_0 = module_1.Config(str_0)
        path_0 = module_0.Path()
        base_config_dict_0 = module_1.BaseConfigDict(path_0)
        var_0 = base_config_dict_0.save(config_0)
        path_1 = module_1.get_default_config_dir()
        base_config_dict_1 = module_1.BaseConfigDict(path_1)
        var_1 = base_config_dict_1.ensure_directory()
        var_2 = base_config_dict_1.ensure_directory()
        var_3 = base_config_dict_1.delete()
        var_4 = path_1.resolve()
        bool_0 = None
        var_5 = path_1.open(bool_0)
    except BaseException:
        pass

def test_case_6():
    try:
        path_0 = module_1.get_default_config_dir()
        path_1 = None
        path_2 = module_1.get_default_config_dir()
        base_config_dict_0 = module_1.BaseConfigDict(path_1)
        var_0 = base_config_dict_0.delete()
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = './test'
        base_config_dict_0 = module_1.BaseConfigDict(str_0)
        var_0 = base_config_dict_0.save()
    except BaseException:
        pass