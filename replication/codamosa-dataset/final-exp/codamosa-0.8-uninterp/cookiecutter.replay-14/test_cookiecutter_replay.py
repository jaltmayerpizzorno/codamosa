# Automatically generated by Pynguin.
import cookiecutter.replay as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'Expand abbreviations in a template name.\n\n    :param template: The project template name.\n    :param abbre_iytions: Abbreviation definitions.\n    '
    str_1 = 'cookiecutter'
    str_2 = {str_1: str_0}
    var_0 = module_0.dump(str_0, str_0, str_2)

def test_case_2():
    str_0 = '.'
    str_1 = 'mw-xroNect'
    var_0 = module_0.get_file_name(str_0, str_1)
    str_2 = 'my-project.json'
    var_1 = module_0.get_file_name(str_0, str_2)
    str_3 = 'my-\trojecP/'
    var_2 = module_0.get_file_name(str_0, str_3)
    var_3 = module_0.get_file_name(str_0, str_2)
    str_4 = 'path/to/my-project.json'
    var_4 = module_0.get_file_name(str_3, str_4)

def test_case_3():
    str_0 = 'cookiecutter'
    var_0 = module_0.load(str_0, str_0)