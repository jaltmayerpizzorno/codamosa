# Automatically generated by Pynguin.
import ansible.utils.unsafe_proxy as module_0

def test_case_0():
    ansible_unsafe_bytes_0 = module_0.AnsibleUnsafeBytes()

def test_case_1():
    ansible_unsafe_text_0 = None
    list_0 = [ansible_unsafe_text_0, ansible_unsafe_text_0]
    var_0 = module_0.wrap_var(list_0)
    dict_0 = {}
    unsafe_proxy_0 = module_0.UnsafeProxy(*list_0, **dict_0)

def test_case_2():
    ansible_unsafe_text_0 = None
    list_0 = [ansible_unsafe_text_0, ansible_unsafe_text_0]
    var_0 = module_0.wrap_var(list_0)
    ansible_unsafe_bytes_0 = module_0.AnsibleUnsafeBytes()

def test_case_3():
    bytes_0 = b'\xb3@|k\xcf\x85\xc0\x0b)5\xab\x87f\xa9\xb1\xc7'
    var_0 = module_0.wrap_var(bytes_0)

def test_case_4():
    ansible_unsafe_text_0 = None
    ansible_unsafe_bytes_0 = module_0.AnsibleUnsafeBytes()
    list_0 = [ansible_unsafe_text_0, ansible_unsafe_text_0]
    var_0 = module_0.to_unsafe_text(*list_0)
    var_1 = module_0.wrap_var(list_0)
    unsafe_proxy_0 = module_0.UnsafeProxy(*list_0)

def test_case_5():
    ansible_unsafe_bytes_0 = module_0.AnsibleUnsafeBytes()
    int_0 = 1324
    ansible_unsafe_bytes_1 = module_0.AnsibleUnsafeBytes()
    ansible_unsafe_text_0 = module_0.AnsibleUnsafeText()
    var_0 = module_0.wrap_var(int_0)

def test_case_6():
    ansible_unsafe_text_0 = None
    ansible_unsafe_bytes_0 = module_0.AnsibleUnsafeBytes()
    list_0 = [ansible_unsafe_text_0, ansible_unsafe_text_0]
    var_0 = module_0.wrap_var(list_0)
    dict_0 = {}
    unsafe_proxy_0 = module_0.UnsafeProxy(*list_0, **dict_0)
    str_0 = 'A2u"2\to7JSz,Y<a5_'
    set_0 = {ansible_unsafe_bytes_0}
    tuple_0 = (set_0,)
    tuple_1 = (tuple_0, unsafe_proxy_0)
    tuple_2 = (tuple_1, ansible_unsafe_bytes_0, tuple_0, dict_0)
    list_1 = [ansible_unsafe_text_0, ansible_unsafe_bytes_0, set_0]
    tuple_3 = (str_0, tuple_2, list_1, str_0)
    var_1 = module_0.wrap_var(tuple_3)