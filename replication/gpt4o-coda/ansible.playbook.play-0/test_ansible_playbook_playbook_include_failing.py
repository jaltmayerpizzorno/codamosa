# Automatically generated by Pynguin.
import ansible.playbook.playbook_include as module_0

def test_case_0():
    try:
        playbook_include_0 = module_0.PlaybookInclude()
        int_0 = 2255
        dict_0 = {}
        var_0 = playbook_include_0.load(int_0, dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        playbook_include_0 = module_0.PlaybookInclude()
        dict_0 = {playbook_include_0: playbook_include_0, playbook_include_0: playbook_include_0, playbook_include_0: playbook_include_0, playbook_include_0: playbook_include_0}
        var_0 = playbook_include_0.load_data(dict_0, dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        dict_0 = {}
        bool_0 = None
        playbook_include_0 = module_0.PlaybookInclude()
        var_0 = playbook_include_0.load(dict_0, bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'import_playbook'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
        playbook_include_0 = module_0.PlaybookInclude()
        var_0 = playbook_include_0.load_data(dict_0, dict_0, playbook_include_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'vars'
        str_1 = '~J"`Qa7nv+*j'
        str_2 = 'condition2'
        dict_0 = {str_2: str_1, str_2: str_2, str_0: str_2, str_2: str_1}
        playbook_include_0 = module_0.PlaybookInclude()
        var_0 = playbook_include_0.load_data(dict_0, playbook_include_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'import_playbook'
        dict_0 = {str_0: str_0, str_0: str_0}
        playbook_include_0 = module_0.PlaybookInclude()
        var_0 = playbook_include_0.load_data(dict_0, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'import_playbook'
        str_1 = 'tags'
        str_2 = 'when'
        str_3 = 'test_playbook.yml'
        str_4 = 'var1'
        str_5 = 'value1'
        str_6 = {str_4: str_5}
        dict_0 = {str_0: str_1, str_2: str_0, str_5: str_3, str_0: str_6}
        playbook_include_0 = module_0.PlaybookInclude()
        playbook_include_1 = module_0.PlaybookInclude()
        var_0 = playbook_include_1.load_data(dict_0, playbook_include_0)
    except BaseException:
        pass

def test_case_7():
    try:
        bool_0 = False
        dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
        playbook_include_0 = module_0.PlaybookInclude()
        var_0 = playbook_include_0.preprocess_data(dict_0)
        str_0 = 'import_playbook'
        playbook_include_1 = module_0.PlaybookInclude()
        var_1 = playbook_include_0.load_data(var_0, str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'vars'
        str_1 = 'tags'
        str_2 = 'when'
        str_3 = 'var1'
        str_4 = {str_3: str_1}
        dict_0 = {str_0: str_1, str_2: str_0, str_0: str_3, str_0: str_4}
        playbook_include_0 = module_0.PlaybookInclude()
        playbook_include_1 = module_0.PlaybookInclude()
        var_0 = playbook_include_1.load_data(dict_0, playbook_include_0)
    except BaseException:
        pass