# Automatically generated by Pynguin.
import mimesis.providers.path as module_0

def test_case_0():
    try:
        path_0 = module_0.Path()
        str_0 = path_0.root()
        path_1 = module_0.Path()
        str_1 = path_1.home()
        str_2 = 'linux'
        path_2 = module_0.Path(str_2)
        str_3 = path_1.project_dir()
        str_4 = path_2.home()
        path_3 = module_0.Path()
        str_5 = path_3.home()
        str_6 = 'win32'
        path_4 = module_0.Path(str_6)
        str_7 = path_4.home()
        path_5 = module_0.Path(str_2)
        str_8 = path_5.user()
        path_6 = module_0.Path(str_6)
        str_9 = path_6.user()
        path_7 = module_0.Path()
        str_10 = path_7.users_folder()
        path_8 = module_0.Path(str_7)
    except BaseException:
        pass