# Automatically generated by Pynguin.
import ansible.parsing.utils.yaml as module_0

def test_case_0():
    try:
        bytes_0 = b'wUS\xa3\xbe_\xee-\xc3[s,\xdfi'
        var_0 = module_0.from_yaml(bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '\n    - name: inventory-test\n      host: "localhost"\n      tasks:\n      - debug: \n            msg: "Hello"\n        - debug: \n            msg:"Test"\n    '
        var_0 = module_0.from_yaml(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = False
        var_0 = module_0.from_yaml(bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '='
        complex_0 = None
        int_0 = None
        tuple_0 = (str_0, complex_0, int_0)
        list_0 = [tuple_0]
        int_1 = 3631
        set_0 = {int_1, int_0}
        var_0 = module_0.from_yaml(list_0, list_0, int_1, list_0, set_0)
    except BaseException:
        pass