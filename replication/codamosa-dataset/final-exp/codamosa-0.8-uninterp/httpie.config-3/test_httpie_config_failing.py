# Automatically generated by Pynguin.
import httpie.config as module_0
import pathlib as module_1

def test_case_0():
    try:
        path_0 = module_0.get_default_config_dir()
        base_config_dict_0 = module_0.BaseConfigDict(path_0)
        bool_0 = base_config_dict_0.is_new()
        config_0 = module_0.Config()
        path_1 = module_0.get_default_config_dir()
        var_0 = path_1.readlink()
    except BaseException:
        pass

def test_case_1():
    try:
        path_0 = module_1.Path()
        base_config_dict_0 = module_0.BaseConfigDict(path_0)
        var_0 = base_config_dict_0.load()
    except BaseException:
        pass

def test_case_2():
    try:
        config_0 = module_0.Config()
        var_0 = config_0.save()
    except BaseException:
        pass

def test_case_3():
    try:
        path_0 = module_0.get_default_config_dir()
        base_config_dict_0 = module_0.BaseConfigDict(path_0)
        var_0 = base_config_dict_0.delete()
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'test.json'
        base_config_dict_0 = module_0.BaseConfigDict(str_0)
        var_0 = base_config_dict_0.save()
    except BaseException:
        pass

def test_case_5():
    try:
        path_0 = module_0.get_default_config_dir()
        config_0 = module_0.Config()
        path_1 = module_0.get_default_config_dir()
        base_config_dict_0 = module_0.BaseConfigDict(path_1)
        var_0 = base_config_dict_0.ensure_directory()
        var_1 = base_config_dict_0.save()
        path_2 = None
        base_config_dict_1 = module_0.BaseConfigDict(path_2)
        var_2 = base_config_dict_1.delete()
    except BaseException:
        pass

def test_case_6():
    try:
        config_file_error_0 = module_0.ConfigFileError()
        path_0 = module_0.get_default_config_dir()
        base_config_dict_0 = module_0.BaseConfigDict(path_0)
        var_0 = base_config_dict_0.load()
    except BaseException:
        pass