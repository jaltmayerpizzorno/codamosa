# Automatically generated by Pynguin.
import ansible.vars.reserved as module_0

def test_case_0():
    try:
        bool_0 = False
        dict_0 = {bool_0: bool_0}
        str_0 = '2tt5<3-n#d#'
        var_0 = module_0.warn_if_reserved(dict_0, str_0)
        var_1 = module_0.get_reserved_names(bool_0)
        var_2 = module_0.warn_if_reserved(bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'ocb'
        var_0 = module_0.warn_if_reserved(str_0)
        list_0 = [str_0]
        var_1 = module_0.warn_if_reserved(list_0, list_0)
        set_0 = set()
        var_2 = module_0.is_reserved_name(set_0)
        bool_0 = True
        str_1 = 'C!H"2"O2/+\r<k'
        var_3 = module_0.warn_if_reserved(bool_0, str_1)
    except BaseException:
        pass