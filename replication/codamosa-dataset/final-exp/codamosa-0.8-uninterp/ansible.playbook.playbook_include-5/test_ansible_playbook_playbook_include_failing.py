# Automatically generated by Pynguin.
import ansible.parsing.yaml.objects as module_0
import ansible.playbook.playbook_include as module_1

def test_case_0():
    try:
        ansible_mapping_0 = module_0.AnsibleMapping()
        list_0 = [ansible_mapping_0, ansible_mapping_0]
        playbook_include_0 = module_1.PlaybookInclude()
        var_0 = playbook_include_0.load(ansible_mapping_0, list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        playbook_include_0 = module_1.PlaybookInclude()
        str_0 = 'import_playbook'
        str_1 = {str_0: str_0}
        var_0 = playbook_include_0.load_data(str_1, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        playbook_include_0 = module_1.PlaybookInclude()
        str_0 = '/path/to/basedir'
        str_1 = 'test.yml'
        str_2 = {str_1: str_1}
        var_0 = playbook_include_0.load_data(str_2, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        playbook_include_0 = module_1.PlaybookInclude()
        set_0 = {playbook_include_0, playbook_include_0}
        playbook_include_1 = module_1.PlaybookInclude()
        var_0 = playbook_include_1.preprocess_data(set_0)
    except BaseException:
        pass

def test_case_4():
    try:
        dict_0 = {}
        str_0 = "sKfe'sM$"
        playbook_include_0 = module_1.PlaybookInclude()
        var_0 = playbook_include_0.load(dict_0, str_0, playbook_include_0, dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        playbook_include_0 = module_1.PlaybookInclude()
        str_0 = ''
        playbook_include_1 = module_1.PlaybookInclude()
        str_1 = 'import_playbook'
        str_2 = {str_1: str_0}
        var_0 = playbook_include_0.load_data(str_2, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        playbook_include_0 = module_1.PlaybookInclude()
        str_0 = 'import_playbook'
        str_1 = 'test.yml'
        bytes_0 = b'\x05\x9c\x7f\xa6\xbf\xda\xa3/_&\xe6\xa7\x9d\xa3\xc6\x02\xe4'
        dict_0 = {playbook_include_0: playbook_include_0, str_0: playbook_include_0, str_1: str_0, bytes_0: str_0}
        str_2 = 'z(#JlG6)'
        var_0 = playbook_include_0.load_data(dict_0, str_2)
    except BaseException:
        pass

def test_case_7():
    try:
        playbook_include_0 = module_1.PlaybookInclude()
        str_0 = '/path/to/basedir'
        str_1 = 'import_playbook'
        str_2 = {str_1: str_0}
        var_0 = playbook_include_0.load_data(str_2, str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        playbook_include_0 = module_1.PlaybookInclude()
        str_0 = 'import_playbook'
        str_1 = '3K%vu4Gitd\nOz'
        str_2 = {str_0: str_1}
        var_0 = playbook_include_0.load_data(str_2, str_1)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'import_playbook'
        playbook_include_0 = module_1.PlaybookInclude()
        var_0 = None
        var_1 = {str_0: var_0}
        var_2 = playbook_include_0.preprocess_data(var_1)
    except BaseException:
        pass