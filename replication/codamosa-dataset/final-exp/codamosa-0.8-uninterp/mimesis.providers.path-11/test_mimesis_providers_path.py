# Automatically generated by Pynguin.
import mimesis.providers.path as module_0

def test_case_0():
    path_0 = module_0.Path()

def test_case_1():
    path_0 = module_0.Path()
    str_0 = path_0.dev_dir()
    str_1 = path_0.root()
    str_2 = path_0.project_dir()
    str_3 = path_0.root()

def test_case_2():
    path_0 = module_0.Path()
    str_0 = path_0.home()

def test_case_3():
    path_0 = module_0.Path()
    str_0 = path_0.user()

def test_case_4():
    path_0 = module_0.Path()
    str_0 = path_0.user()
    path_1 = module_0.Path()
    str_1 = path_1.users_folder()
    str_2 = path_1.dev_dir()
    str_3 = path_1.root()
    str_4 = path_1.user()
    str_5 = path_1.user()
    str_6 = path_1.dev_dir()
    str_7 = path_1.root()
    str_8 = path_1.users_folder()
    str_9 = path_1.dev_dir()

def test_case_5():
    path_0 = module_0.Path()
    str_0 = path_0.dev_dir()

def test_case_6():
    str_0 = 'win64'
    path_0 = module_0.Path(str_0)
    str_1 = path_0.root()
    var_0 = print(str_1)
    str_2 = path_0.home()
    var_1 = print(str_2)
    str_3 = path_0.user()
    var_2 = print(str_3)
    str_4 = path_0.users_folder()
    var_3 = print(str_4)
    str_5 = path_0.dev_dir()
    var_4 = print(str_5)
    str_6 = path_0.project_dir()
    var_5 = print(str_6)