# Automatically generated by Pynguin.
import pathlib as module_0
import httpie.config as module_1

def test_case_0():
    try:
        str_0 = '`ul!\x0cN\x0cyW@WL\t^bJtC'
        dict_0 = {str_0: str_0, str_0: str_0}
        path_0 = module_0.Path(**dict_0)
        base_config_dict_0 = module_1.BaseConfigDict(path_0)
        var_0 = base_config_dict_0.load()
    except BaseException:
        pass

def test_case_1():
    try:
        config_0 = module_1.Config()
        config_file_error_0 = module_1.ConfigFileError()
        config_1 = module_1.Config()
        path_0 = module_1.get_default_config_dir()
        base_config_dict_0 = module_1.BaseConfigDict(path_0)
        var_0 = base_config_dict_0.load()
        path_1 = module_0.Path()
        base_config_dict_1 = module_1.BaseConfigDict(path_1)
        var_1 = base_config_dict_1.load()
    except BaseException:
        pass

def test_case_2():
    try:
        path_0 = module_1.get_default_config_dir()
        base_config_dict_0 = module_1.BaseConfigDict(path_0)
        var_0 = base_config_dict_0.save()
    except BaseException:
        pass

def test_case_3():
    try:
        path_0 = module_0.Path()
        base_config_dict_0 = module_1.BaseConfigDict(path_0)
        var_0 = path_0.exists()
        var_1 = base_config_dict_0.delete()
    except BaseException:
        pass

def test_case_4():
    try:
        path_0 = module_1.get_default_config_dir()
        base_config_dict_0 = module_1.BaseConfigDict(path_0)
        str_0 = '>{3+_.+d!GVK.h/YuxbF'
        var_0 = path_0.write_text(str_0)
        var_1 = base_config_dict_0.load()
    except BaseException:
        pass

def test_case_5():
    try:
        path_0 = module_1.get_default_config_dir()
        path_1 = None
        base_config_dict_0 = module_1.BaseConfigDict(path_1)
        var_0 = base_config_dict_0.ensure_directory()
    except BaseException:
        pass

def test_case_6():
    try:
        path_0 = module_1.get_default_config_dir()
        path_1 = None
        base_config_dict_0 = module_1.BaseConfigDict(path_1)
        var_0 = base_config_dict_0.delete()
    except BaseException:
        pass