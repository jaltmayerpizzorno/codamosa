# Automatically generated by Pynguin.
import mimesis.providers.path as module_0

def test_case_0():
    path_0 = module_0.Path()

def test_case_1():
    path_0 = module_0.Path()
    str_0 = path_0.dev_dir()
    str_1 = path_0.project_dir()
    str_2 = path_0.root()
    str_3 = path_0.dev_dir()
    str_4 = path_0.users_folder()
    str_5 = path_0.project_dir()
    str_6 = path_0.user()

def test_case_2():
    path_0 = module_0.Path()
    str_0 = path_0.home()

def test_case_3():
    path_0 = module_0.Path()
    str_0 = path_0.project_dir()

def test_case_4():
    path_0 = module_0.Path()
    str_0 = path_0.dev_dir()
    str_1 = path_0.project_dir()
    str_2 = path_0.dev_dir()
    str_3 = path_0.users_folder()
    str_4 = path_0.project_dir()

def test_case_5():
    str_0 = 'win32'
    path_0 = module_0.Path(str_0)
    var_0 = path_0.platform
    path_1 = module_0.Path()
    var_1 = path_1.platform

def test_case_6():
    str_0 = 'win32'
    path_0 = module_0.Path(str_0)
    var_0 = path_0.platform
    path_1 = module_0.Path()
    var_1 = path_1.platform
    str_1 = path_0.project_dir()