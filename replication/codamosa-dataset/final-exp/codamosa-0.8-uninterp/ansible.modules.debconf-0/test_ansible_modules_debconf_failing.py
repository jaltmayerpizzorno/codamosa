# Automatically generated by Pynguin.
import ansible.modules.debconf as module_0

def test_case_0():
    try:
        bytes_0 = b'P\xd2\xa1|l8\xd3\x00z\x11\x9d#T\x90'
        set_0 = {bytes_0}
        var_0 = module_0.get_selections(bytes_0, set_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = True
        list_0 = [bool_0, bool_0, bool_0]
        dict_0 = None
        str_0 = 'P&KKn7fK(='
        var_0 = module_0.set_selection(bool_0, list_0, dict_0, str_0, bool_0, str_0)
    except BaseException:
        pass