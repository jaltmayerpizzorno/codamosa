# Automatically generated by Pynguin.
import ansible.module_utils.common.dict_transformations as module_0

def test_case_0():
    try:
        float_0 = 838.83
        var_0 = module_0.camel_dict_to_snake_dict(float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        set_0 = None
        dict_0 = {set_0: set_0}
        var_0 = module_0.recursive_diff(dict_0, dict_0)
        str_0 = "u S\x0c')&[@O{Vq`8&.n\t"
        var_1 = module_0.snake_dict_to_camel_dict(str_0)
        str_1 = 'JpJ<bjy4O{|~'
        var_2 = module_0.snake_dict_to_camel_dict(str_1)
        var_3 = module_0.snake_dict_to_camel_dict(dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 't%'
        dict_0 = {str_0: str_0, str_0: str_0}
        var_0 = module_0.dict_merge(str_0, dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'T~\x0b%Yz7V}5\x0cfKy>zqE'
        int_0 = -1974
        var_0 = module_0.recursive_diff(str_0, int_0)
    except BaseException:
        pass

def test_case_4():
    try:
        set_0 = None
        dict_0 = {set_0: set_0, set_0: set_0}
        var_0 = module_0.recursive_diff(dict_0, dict_0)
        list_0 = [set_0]
        var_1 = module_0.snake_dict_to_camel_dict(list_0)
        var_2 = module_0.snake_dict_to_camel_dict(list_0)
        int_0 = 7602
        var_3 = module_0.snake_dict_to_camel_dict(int_0, int_0)
        bool_0 = True
        var_4 = module_0.dict_merge(set_0, list_0)
        var_5 = module_0.snake_dict_to_camel_dict(dict_0, bool_0)
    except BaseException:
        pass

def test_case_5():
    try:
        set_0 = None
        dict_0 = {set_0: set_0}
        var_0 = module_0.recursive_diff(dict_0, dict_0)
        list_0 = []
        var_1 = module_0.snake_dict_to_camel_dict(list_0)
        var_2 = module_0.dict_merge(list_0, dict_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = ''
        str_1 = 'B'
        str_2 = 'a'
        str_3 = '"'
        str_4 = 'c'
        str_5 = "%xwi7:?Y='@E_\n8iZ"
        dict_0 = {str_5: str_3, str_4: str_4}
        var_0 = module_0.snake_dict_to_camel_dict(dict_0)
        str_6 = [str_2, str_3, str_4]
        str_7 = 'W'
        dict_1 = {str_3: var_0, str_0: var_0, str_1: str_6, str_3: str_4}
        var_1 = module_0.snake_dict_to_camel_dict(dict_1)
        list_0 = [str_6, str_3, str_3]
        var_2 = module_0.snake_dict_to_camel_dict(dict_0)
        var_3 = module_0.camel_dict_to_snake_dict(dict_1, list_0, str_7)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'A'
        str_1 = 'a'
        set_0 = None
        var_0 = module_0.snake_dict_to_camel_dict(set_0)
        str_2 = '$"'
        str_3 = 'c'
        str_4 = "%xwi7:?Y='@E_\n8iZ"
        dict_0 = {str_4: str_2, str_3: str_3}
        var_1 = module_0.snake_dict_to_camel_dict(dict_0)
        str_5 = [str_1, str_2, str_3]
        str_6 = '6'
        dict_1 = {str_0: var_1, str_6: str_5, str_2: str_3}
        var_2 = module_0.snake_dict_to_camel_dict(set_0)
        list_0 = [str_5, str_2, str_2]
        var_3 = module_0.camel_dict_to_snake_dict(dict_1, list_0, str_6)
    except BaseException:
        pass