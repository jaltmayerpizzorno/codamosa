# Automatically generated by Pynguin.
import httpie.config as module_0
import pathlib as module_1

def test_case_0():
    pass

def test_case_1():
    config_0 = module_0.Config()

def test_case_2():
    config_0 = module_0.Config()
    var_0 = config_0.save()

def test_case_3():
    path_0 = module_1.Path()
    base_config_dict_0 = module_0.BaseConfigDict(path_0)
    bool_0 = base_config_dict_0.is_new()

def test_case_4():
    path_0 = module_0.get_default_config_dir()
    base_config_dict_0 = module_0.BaseConfigDict(path_0)
    path_1 = module_0.get_default_config_dir()
    config_0 = module_0.Config(path_1)
    bool_0 = base_config_dict_0.is_new()
    var_0 = base_config_dict_0.load()

def test_case_5():
    str_0 = '(G]+yAxDMz\\\\O8O.W:qU'
    path_0 = module_0.get_default_config_dir()
    base_config_dict_0 = module_0.BaseConfigDict(path_0)
    var_0 = base_config_dict_0.save(str_0)
    var_1 = base_config_dict_0.delete()
    path_1 = module_0.get_default_config_dir()
    base_config_dict_1 = module_0.BaseConfigDict(path_1)
    var_2 = base_config_dict_0.save(base_config_dict_1)
    var_3 = base_config_dict_1.load()
    var_4 = path_1.exists()
    base_config_dict_2 = module_0.BaseConfigDict(path_1)
    var_5 = base_config_dict_2.load()

def test_case_6():
    path_0 = module_0.get_default_config_dir()
    base_config_dict_0 = module_0.BaseConfigDict(path_0)
    var_0 = path_0.exists()
    var_1 = base_config_dict_0.delete()
    config_0 = module_0.Config(path_0)

def test_case_7():
    path_0 = module_1.Path()
    base_config_dict_0 = module_0.BaseConfigDict(path_0)
    var_0 = base_config_dict_0.save(base_config_dict_0)