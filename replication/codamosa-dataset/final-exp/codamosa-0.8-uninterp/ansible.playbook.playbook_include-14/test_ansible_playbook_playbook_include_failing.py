# Automatically generated by Pynguin.
import ansible.playbook.playbook_include as module_0
import ansible.parsing.yaml.objects as module_1

def test_case_0():
    try:
        str_0 = 'OxYY4sM3Yk'
        playbook_include_0 = module_0.PlaybookInclude()
        tuple_0 = (playbook_include_0,)
        playbook_include_1 = module_0.PlaybookInclude()
        var_0 = playbook_include_1.load(str_0, tuple_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = -245
        str_0 = 'Vn[vTzP;0+}(~4?\\'
        playbook_include_0 = module_0.PlaybookInclude()
        var_0 = playbook_include_0.load_data(int_0, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        list_0 = []
        playbook_include_0 = module_0.PlaybookInclude()
        var_0 = playbook_include_0.preprocess_data(list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        dict_0 = {}
        list_0 = [dict_0, dict_0, dict_0]
        playbook_include_0 = module_0.PlaybookInclude()
        var_0 = playbook_include_0.load_data(dict_0, list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        dict_0 = {}
        playbook_include_0 = module_0.PlaybookInclude()
        bytes_0 = None
        set_0 = {bytes_0, playbook_include_0}
        var_0 = playbook_include_0.load_data(dict_0, bytes_0, set_0)
    except BaseException:
        pass

def test_case_5():
    try:
        playbook_include_0 = module_0.PlaybookInclude()
        str_0 = 'import_playbook'
        str_1 = {str_0: str_0, str_0: str_0}
        var_0 = playbook_include_0.load_data(str_1, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        playbook_include_0 = module_0.PlaybookInclude()
        str_0 = 'import_playbook'
        str_1 = {str_0: str_0, str_0: str_0}
        var_0 = playbook_include_0.load_data(str_1, str_1)
    except BaseException:
        pass

def test_case_7():
    try:
        playbook_include_0 = module_0.PlaybookInclude()
        str_0 = 'import_playbook'
        dict_0 = {str_0: playbook_include_0}
        var_0 = playbook_include_0.preprocess_data(dict_0)
    except BaseException:
        pass

def test_case_8():
    try:
        playbook_include_0 = module_0.PlaybookInclude()
        str_0 = 'import_playbook'
        str_1 = ';c1\x0c(5RKg\nX`5'
        str_2 = {str_0: str_1, str_0: str_1}
        var_0 = playbook_include_0.load_data(str_2, str_1)
    except BaseException:
        pass

def test_case_9():
    try:
        ansible_mapping_0 = module_1.AnsibleMapping()
        list_0 = [ansible_mapping_0, ansible_mapping_0, ansible_mapping_0, ansible_mapping_0]
        list_1 = []
        playbook_include_0 = module_0.PlaybookInclude()
        var_0 = playbook_include_0.load_data(ansible_mapping_0, list_0, list_1)
    except BaseException:
        pass

def test_case_10():
    try:
        playbook_include_0 = module_0.PlaybookInclude()
        str_0 = 'import_playbook'
        str_1 = 'tags'
        str_2 = ''
        str_3 = 'm@Y1'
        str_4 = {str_0: str_2, str_1: str_3}
        str_5 = ''
        var_0 = playbook_include_0.load_data(str_4, str_5)
    except BaseException:
        pass

def test_case_11():
    try:
        playbook_include_0 = module_0.PlaybookInclude()
        var_0 = playbook_include_0.serialize()
        str_0 = '/tmp'
        var_1 = playbook_include_0.load_data(var_0, str_0)
    except BaseException:
        pass