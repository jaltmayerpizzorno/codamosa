# Automatically generated by Pynguin.
import ansible.parsing.yaml.objects as module_0
import ansible.playbook.playbook_include as module_1

def test_case_0():
    try:
        ansible_mapping_0 = module_0.AnsibleMapping()
        bool_0 = False
        playbook_include_0 = module_1.PlaybookInclude()
        var_0 = playbook_include_0.load(ansible_mapping_0, bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 69
        playbook_include_0 = module_1.PlaybookInclude()
        playbook_include_1 = module_1.PlaybookInclude()
        var_0 = playbook_include_1.load_data(int_0, playbook_include_0)
    except BaseException:
        pass

def test_case_2():
    try:
        dict_0 = {}
        bool_0 = True
        playbook_include_0 = module_1.PlaybookInclude()
        var_0 = playbook_include_0.load_data(dict_0, bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = './test/test.yml'
        str_1 = 'var1'
        str_2 = 'value1'
        playbook_include_0 = module_1.PlaybookInclude()
        str_3 = {str_1: str_2}
        str_4 = 'True'
        playbook_include_1 = module_1.PlaybookInclude()
        playbook_include_2 = module_1.PlaybookInclude()
        str_5 = 'import_playbook'
        str_6 = 'vars'
        str_7 = 'when'
        str_8 = {str_1: str_2}
        str_9 = {str_5: str_0, str_6: str_8, str_7: str_4}
        str_10 = './test'
        var_0 = playbook_include_2.load_data(str_9, str_10, str_9, str_9)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '/dummy/path/dummy_playbook.yml'
        var_0 = dict(import_playbook=str_0)
        playbook_include_0 = module_1.PlaybookInclude()
        var_1 = playbook_include_0.load_data(var_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'vars'
        str_1 = 'var_a'
        str_2 = 'abc'
        str_3 = {str_1: str_2}
        str_4 = 'tag1,tag2'
        str_5 = {str_2: str_3, str_0: str_3, str_0: str_4}
        playbook_include_0 = module_1.PlaybookInclude()
        var_0 = playbook_include_0.preprocess_data(str_5)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = './test/test.yml'
        str_1 = 'value1'
        str_2 = 'FQsfg*'
        playbook_include_0 = module_1.PlaybookInclude()
        str_3 = 'import_playbook'
        str_4 = 'vars'
        str_5 = 'when'
        str_6 = {str_5: str_1}
        str_7 = {str_3: str_0, str_4: str_6, str_5: str_2}
        var_0 = None
        var_1 = playbook_include_0.load_data(str_7, str_7, var_0, var_0)
    except BaseException:
        pass

def test_case_7():
    try:
        playbook_include_0 = module_1.PlaybookInclude()
        var_0 = dict(import_playbook=playbook_include_0)
        var_1 = playbook_include_0.preprocess_data(var_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'Pu}47ui+L;|w'
        var_0 = dict(import_playbook=str_0)
        playbook_include_0 = module_1.PlaybookInclude()
        var_1 = playbook_include_0.load_data(var_0, str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = ''
        str_1 = 'r1'
        str_2 = 'value1'
        playbook_include_0 = module_1.PlaybookInclude()
        str_3 = {str_1: str_2}
        str_4 = 'True'
        playbook_include_1 = module_1.PlaybookInclude()
        playbook_include_2 = module_1.PlaybookInclude()
        str_5 = 'import_playbook'
        str_6 = 'vars'
        str_7 = 'when'
        str_8 = {str_1: str_2, str_5: str_4, str_4: playbook_include_1}
        str_9 = {str_5: str_0, str_6: str_8, str_7: str_4}
        str_10 = './test'
        var_0 = None
        var_1 = playbook_include_2.load_data(str_9, str_10, var_0, var_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = ' Create a tempfile containing defined content '
        str_1 = 'var1'
        str_2 = 'value1'
        str_3 = {str_1: str_2}
        str_4 = 'True'
        playbook_include_0 = module_1.PlaybookInclude()
        str_5 = 'import_playbook'
        str_6 = 'vars'
        str_7 = 'when'
        str_8 = {str_5: str_0, str_6: str_6, str_7: str_4}
        var_0 = None
        var_1 = playbook_include_0.load_data(str_8, str_7, var_0, var_0)
    except BaseException:
        pass

def test_case_11():
    try:
        playbook_include_0 = module_1.PlaybookInclude()
        str_0 = 'import_playbook'
        str_1 = 'tags'
        str_2 = 'example.yml vars="a=1 b=2" tags="tag_a,tag_b"'
        str_3 = [str_2]
        str_4 = {str_0: str_2, str_1: str_2, str_1: str_3}
        var_0 = playbook_include_0.load_data(str_4, str_4)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = ' Create a tempfile containing defined content '
        str_1 = 'var1'
        str_2 = 'value1'
        str_3 = {str_1: str_2}
        str_4 = 'True'
        playbook_include_0 = module_1.PlaybookInclude()
        str_5 = 'import_playbook'
        str_6 = 'when'
        str_7 = {str_5: str_0, str_6: str_6, str_6: str_4}
        var_0 = None
        var_1 = playbook_include_0.load_data(str_7, str_6, var_0, var_0)
    except BaseException:
        pass