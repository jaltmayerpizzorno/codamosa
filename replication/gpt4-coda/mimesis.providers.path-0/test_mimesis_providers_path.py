# Automatically generated by Pynguin.
import mimesis.providers.path as module_0

def test_case_0():
    path_0 = module_0.Path()

def test_case_1():
    path_0 = module_0.Path()
    path_1 = module_0.Path()
    str_0 = path_1.dev_dir()
    str_1 = path_0.dev_dir()
    str_2 = path_1.user()
    str_3 = path_0.dev_dir()
    str_4 = path_0.home()

def test_case_2():
    path_0 = module_0.Path()
    str_0 = path_0.users_folder()

def test_case_3():
    path_0 = module_0.Path()
    str_0 = path_0.dev_dir()
    str_1 = path_0.dev_dir()
    str_2 = path_0.user()

def test_case_4():
    str_0 = 'win32'
    path_0 = module_0.Path(str_0)
    str_1 = 'linux'
    path_1 = module_0.Path(str_1)
    str_2 = path_0.user()
    str_3 = path_1.user()
    str_4 = path_0.home()
    str_5 = path_1.home()