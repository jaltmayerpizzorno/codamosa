# Automatically generated by Pynguin.
import ansible.template.native_helpers as module_0
import jinja2.runtime as module_1
import ansible.utils.native_jinja as module_2

def test_case_0():
    try:
        int_0 = 867
        var_0 = module_0.ansible_native_concat(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'P'
        list_0 = [bytes_0]
        var_0 = module_0.ansible_native_concat(list_0)
        tuple_0 = None
        float_0 = -676.519409
        list_1 = [float_0]
        tuple_1 = (tuple_0, list_1)
        var_1 = module_0.ansible_native_concat(tuple_1)
    except BaseException:
        pass

def test_case_2():
    try:
        strict_undefined_0 = module_1.StrictUndefined()
        strict_undefined_1 = module_1.StrictUndefined()
        strict_undefined_2 = [strict_undefined_0, strict_undefined_1]
        var_0 = module_0.ansible_native_concat(strict_undefined_2)
    except BaseException:
        pass

def test_case_3():
    try:
        set_0 = set()
        var_0 = module_0.ansible_native_concat(set_0)
        str_0 = '2wz4*k_g%'
        var_1 = module_0.ansible_native_concat(str_0)
        native_jinja_text_0 = module_2.NativeJinjaText()
        dict_0 = {native_jinja_text_0: var_1}
        var_2 = module_0.ansible_native_concat(str_0)
        var_3 = module_0.ansible_native_concat(dict_0)
        list_0 = [set_0, var_1]
        strict_undefined_0 = module_1.StrictUndefined(str_0, list_0)
        async_iterator_0 = strict_undefined_0.__aiter__()
        var_4 = module_0.ansible_native_concat(async_iterator_0)
    except BaseException:
        pass