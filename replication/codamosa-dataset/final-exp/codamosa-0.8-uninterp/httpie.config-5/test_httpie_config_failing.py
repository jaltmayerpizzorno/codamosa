# Automatically generated by Pynguin.
import pathlib as module_0
import httpie.config as module_1

def test_case_0():
    try:
        path_0 = module_0.Path()
        base_config_dict_0 = module_1.BaseConfigDict(path_0)
        var_0 = base_config_dict_0.load()
    except BaseException:
        pass

def test_case_1():
    try:
        path_0 = module_1.get_default_config_dir()
        base_config_dict_0 = module_1.BaseConfigDict(path_0)
        var_0 = base_config_dict_0.save()
        base_config_dict_1 = module_1.BaseConfigDict(path_0)
        path_1 = module_1.get_default_config_dir()
        var_1 = base_config_dict_1.load()
        var_2 = base_config_dict_1.delete()
        var_3 = path_1.readlink()
    except BaseException:
        pass

def test_case_2():
    try:
        config_0 = module_1.Config()
        var_0 = config_0.save()
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'json.sort_keys:true'
        dict_0 = {str_0: str_0, str_0: str_0}
        path_0 = module_0.Path(**dict_0)
        base_config_dict_0 = module_1.BaseConfigDict(path_0)
        var_0 = base_config_dict_0.delete()
    except BaseException:
        pass

def test_case_4():
    try:
        path_0 = module_1.get_default_config_dir()
        base_config_dict_0 = module_1.BaseConfigDict(path_0)
        var_0 = base_config_dict_0.load()
        path_1 = module_0.Path()
        base_config_dict_1 = module_1.BaseConfigDict(path_1)
        var_1 = base_config_dict_1.delete()
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'Vc,Hf2Mrk`8*O'
        path_0 = module_1.get_default_config_dir()
        bool_0 = False
        var_0 = path_0.glob(bool_0)
        base_config_dict_0 = module_1.BaseConfigDict(path_0)
        var_1 = base_config_dict_0.ensure_directory()
        base_config_dict_1 = module_1.BaseConfigDict(path_0)
        var_2 = base_config_dict_1.save(str_0)
        path_1 = module_1.get_default_config_dir()
        path_2 = module_1.get_default_config_dir()
        var_3 = path_2.glob(path_1)
        base_config_dict_2 = module_1.BaseConfigDict(path_2)
        var_4 = base_config_dict_2.load()
        var_5 = base_config_dict_0.ensure_directory()
        var_6 = base_config_dict_0.ensure_directory()
        var_7 = path_0.is_fifo()
        var_8 = path_2.read_bytes()
        dict_0 = {str_0: base_config_dict_2, str_0: base_config_dict_1}
        path_3 = module_0.Path(**dict_0)
        path_4 = None
        base_config_dict_3 = module_1.BaseConfigDict(path_4)
        var_9 = base_config_dict_0.ensure_directory()
        str_1 = ''
        config_0 = module_1.Config(str_1)
        path_5 = module_1.get_default_config_dir()
        var_10 = base_config_dict_0.ensure_directory()
        var_11 = base_config_dict_3.delete()
    except BaseException:
        pass

def test_case_6():
    try:
        list_0 = []
        str_0 = "'\r"
        path_0 = module_1.get_default_config_dir()
        base_config_dict_0 = module_1.BaseConfigDict(path_0)
        base_config_dict_1 = module_1.BaseConfigDict(path_0)
        bool_0 = base_config_dict_0.is_new()
        var_0 = base_config_dict_0.load()
        dict_0 = {str_0: str_0}
        path_1 = module_0.Path(*list_0, **dict_0)
        path_2 = module_1.get_default_config_dir()
        base_config_dict_2 = module_1.BaseConfigDict(path_1)
        bool_1 = base_config_dict_2.is_new()
        base_config_dict_3 = module_1.BaseConfigDict(path_1)
        path_3 = None
        base_config_dict_4 = module_1.BaseConfigDict(path_3)
        path_4 = module_1.get_default_config_dir()
        bool_2 = base_config_dict_0.is_new()
        path_5 = module_1.get_default_config_dir()
        base_config_dict_5 = module_1.BaseConfigDict(path_5)
        bool_3 = base_config_dict_3.is_new()
        var_1 = base_config_dict_5.save()
        var_2 = base_config_dict_0.load()
        config_0 = module_1.Config(path_1)
        var_3 = base_config_dict_4.save()
    except BaseException:
        pass

def test_case_7():
    try:
        config_file_error_0 = module_1.ConfigFileError()
        path_0 = None
        base_config_dict_0 = module_1.BaseConfigDict(path_0)
        var_0 = base_config_dict_0.load()
    except BaseException:
        pass