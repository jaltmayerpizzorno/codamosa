# Automatically generated by Pynguin.
import ansible.playbook.playbook_include as module_0
import ansible.parsing.yaml.objects as module_1

def test_case_0():
    try:
        playbook_include_0 = module_0.PlaybookInclude()
        int_0 = 703
        playbook_include_1 = module_0.PlaybookInclude()
        var_0 = playbook_include_1.load(playbook_include_0, int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        playbook_include_0 = module_0.PlaybookInclude()
        list_0 = None
        set_0 = {list_0, list_0, list_0, list_0}
        var_0 = playbook_include_0.load_data(list_0, set_0, set_0)
    except BaseException:
        pass

def test_case_2():
    try:
        playbook_include_0 = module_0.PlaybookInclude()
        str_0 = 'import_playbook'
        str_1 = {str_0: str_0}
        var_0 = playbook_include_0.load_data(str_1, str_0, str_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '4Fx'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        int_0 = 968
        playbook_include_0 = module_0.PlaybookInclude()
        var_0 = playbook_include_0.load_data(dict_0, int_0)
    except BaseException:
        pass

def test_case_4():
    try:
        ansible_mapping_0 = module_1.AnsibleMapping()
        str_0 = 'E\\?_fgHnK-AgGvi%\x0b0Xq'
        playbook_include_0 = module_0.PlaybookInclude()
        var_0 = playbook_include_0.load_data(ansible_mapping_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        playbook_include_0 = module_0.PlaybookInclude()
        str_0 = 'import_playbook'
        str_1 = {str_0: str_0}
        var_0 = None
        var_1 = playbook_include_0.load_data(str_1, str_0, var_0, var_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'include'
        str_1 = 'vars'
        tuple_0 = ()
        dict_0 = {str_0: str_0, str_0: tuple_0, str_1: tuple_0, str_0: tuple_0}
        playbook_include_0 = module_0.PlaybookInclude()
        var_0 = playbook_include_0.preprocess_data(dict_0)
    except BaseException:
        pass

def test_case_7():
    try:
        playbook_include_0 = module_0.PlaybookInclude()
        str_0 = 'var1'
        str_1 = 'import_playbook'
        str_2 = '.'
        float_0 = -1636.3
        dict_0 = {str_0: str_0, str_1: float_0}
        var_0 = playbook_include_0.load_data(dict_0, str_2)
    except BaseException:
        pass

def test_case_8():
    try:
        playbook_include_0 = module_0.PlaybookInclude()
        str_0 = 'var1'
        str_1 = 'gPU{\r;_Y\nDP\x0bj=Wt'
        str_2 = 'import_playbook'
        str_3 = '/L\\'
        str_4 = {str_2: str_3}
        dict_0 = {str_0: playbook_include_0, str_1: str_2, str_2: str_4, str_3: str_4, str_2: str_1, str_0: str_2}
        var_0 = playbook_include_0.preprocess_data(dict_0)
        var_1 = None
        var_2 = playbook_include_0.load_data(str_4, str_1, var_1, var_1)
    except BaseException:
        pass

def test_case_9():
    try:
        playbook_include_0 = module_0.PlaybookInclude()
        str_0 = ':,~841F`:\nrI'
        ansible_mapping_0 = module_1.AnsibleMapping()
        str_1 = 'import_playbook'
        str_2 = {str_1: str_0}
        var_0 = playbook_include_0.load_data(str_2, str_1, str_0, str_0)
    except BaseException:
        pass

def test_case_10():
    try:
        playbook_include_0 = module_0.PlaybookInclude()
        str_0 = 'var1'
        str_1 = ':,~841F`:\nrI'
        ansible_mapping_0 = module_1.AnsibleMapping()
        str_2 = 'import_playbook'
        str_3 = {str_2: str_1}
        str_4 = ''
        var_0 = None
        playbook_include_1 = module_0.PlaybookInclude()
        dict_0 = {playbook_include_0: str_0, str_2: var_0, str_1: playbook_include_1, str_0: str_3}
        list_0 = [dict_0, playbook_include_0, str_0, str_4]
        var_1 = playbook_include_0.load_data(dict_0, list_0)
    except BaseException:
        pass

def test_case_11():
    try:
        playbook_include_0 = module_0.PlaybookInclude()
        playbook_include_1 = module_0.PlaybookInclude()
        str_0 = 'var1'
        str_1 = 'U{>;_Y\nDPDK\x0bA:oCWt'
        str_2 = 'import_playbook'
        str_3 = '\\'
        str_4 = {str_2: str_3}
        dict_0 = {str_0: playbook_include_1, str_1: str_2, str_2: str_4, str_3: str_4, str_2: str_1, str_0: str_2}
        var_0 = playbook_include_1.preprocess_data(dict_0)
        var_1 = playbook_include_1.preprocess_data(dict_0)
        var_2 = None
        var_3 = playbook_include_1.load_data(str_4, str_0, var_2, var_2)
    except BaseException:
        pass