# Automatically generated by Pynguin.
import mimesis.providers.path as module_0

def test_case_0():
    try:
        path_0 = module_0.Path()
        str_0 = path_0.users_folder()
        str_1 = path_0.root()
        str_2 = path_0.project_dir()
        list_0 = [str_1]
        path_1 = module_0.Path(*list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        path_0 = module_0.Path()
        str_0 = path_0.users_folder()
        str_1 = path_0.project_dir()
        list_0 = [str_1]
        path_1 = module_0.Path(*list_0)
    except BaseException:
        pass