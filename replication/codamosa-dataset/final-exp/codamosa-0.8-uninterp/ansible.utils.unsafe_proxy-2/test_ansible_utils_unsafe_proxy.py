# Automatically generated by Pynguin.
import ansible.utils.unsafe_proxy as module_0
import ansible.utils.native_jinja as module_1

def test_case_0():
    dict_0 = {}
    ansible_unsafe_bytes_0 = module_0.AnsibleUnsafeBytes(**dict_0)
    var_0 = ansible_unsafe_bytes_0.decode()

def test_case_1():
    ansible_unsafe_0 = module_0.AnsibleUnsafe()
    bytes_0 = None
    var_0 = module_0.wrap_var(bytes_0)

def test_case_2():
    str_0 = '\n<|"\'YdA$w#(+>_r4J'
    var_0 = module_0.wrap_var(str_0)

def test_case_3():
    bool_0 = True
    var_0 = module_0.wrap_var(bool_0)

def test_case_4():
    dict_0 = None
    var_0 = module_0.wrap_var(dict_0)
    ansible_unsafe_text_0 = module_0.AnsibleUnsafeText()
    tuple_0 = None
    var_1 = module_0.wrap_var(tuple_0)
    float_0 = 1619.417
    var_2 = module_0.wrap_var(float_0)
    set_0 = set()
    var_3 = module_0.wrap_var(set_0)
    var_4 = module_0.wrap_var(set_0)
    native_jinja_text_0 = module_1.NativeJinjaText()
    var_5 = module_0.wrap_var(native_jinja_text_0)
    var_6 = module_0.wrap_var(native_jinja_text_0)
    list_0 = [var_0, tuple_0, var_5]
    var_7 = module_0.wrap_var(list_0)