# Automatically generated by Pynguin.
import mimesis.providers.path as module_0

def test_case_0():
    path_0 = module_0.Path()
    str_0 = path_0.user()

def test_case_1():
    path_0 = module_0.Path()
    str_0 = path_0.root()
    str_1 = path_0.dev_dir()

def test_case_2():
    path_0 = module_0.Path()
    str_0 = path_0.users_folder()
    str_1 = path_0.home()
    str_2 = path_0.project_dir()

def test_case_3():
    path_0 = module_0.Path()
    str_0 = path_0.dev_dir()

def test_case_4():
    str_0 = 'win32'
    path_0 = module_0.Path(str_0)
    str_1 = path_0.user()