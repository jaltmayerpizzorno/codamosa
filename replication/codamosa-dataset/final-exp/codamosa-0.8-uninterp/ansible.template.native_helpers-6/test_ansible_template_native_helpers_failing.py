# Automatically generated by Pynguin.
import ansible.template.native_helpers as module_0
import ansible.utils.native_jinja as module_1
import jinja2.runtime as module_2

def test_case_0():
    try:
        tuple_0 = None
        var_0 = module_0.ansible_native_concat(tuple_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        dict_0 = {bool_0: bool_0}
        list_0 = [dict_0]
        tuple_0 = (list_0,)
        var_0 = module_0.ansible_native_concat(tuple_0)
        int_0 = 1571
        var_1 = module_0.ansible_native_concat(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'scp_if_ssh needs to be one of [smart|True|False]'
        str_1 = 'pb_'
        dict_0 = {}
        var_0 = module_0.ansible_native_concat(dict_0)
        set_0 = {str_1, str_1, str_1, str_1}
        str_2 = ''
        set_1 = {var_0}
        str_3 = None
        dict_1 = {str_2: set_1, str_3: str_2}
        var_1 = module_0.ansible_native_concat(dict_1)
        dict_2 = {str_0: str_0, str_1: set_0}
        var_2 = module_0.ansible_native_concat(dict_2)
        native_jinja_text_0 = module_1.NativeJinjaText()
        bytes_0 = b'\xfc\xf8\xa6\xf4'
        var_3 = module_0.ansible_native_concat(bytes_0)
        tuple_0 = ()
        var_4 = module_0.ansible_native_concat(tuple_0)
        list_0 = [native_jinja_text_0]
        bool_0 = False
        var_5 = module_0.ansible_native_concat(list_0)
        var_6 = module_0.ansible_native_concat(tuple_0)
        var_7 = module_0.ansible_native_concat(bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'foo'
        bool_0 = True
        bool_1 = [bool_0]
        var_0 = module_0.ansible_native_concat(bool_1)
        var_1 = module_0.ansible_native_concat(str_0)
        strict_undefined_0 = module_2.StrictUndefined()
        strict_undefined_1 = module_2.StrictUndefined()
        var_2 = [strict_undefined_1, bool_0]
        var_3 = module_0.ansible_native_concat(var_2)
    except BaseException:
        pass