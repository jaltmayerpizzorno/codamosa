# Automatically generated by Pynguin.
import ansible.utils.unsafe_proxy as module_0
import ansible.utils.native_jinja as module_1

def test_case_0():
    pass

def test_case_1():
    dict_0 = {}
    ansible_unsafe_text_0 = module_0.AnsibleUnsafeText()
    list_0 = [dict_0, dict_0]
    unsafe_proxy_0 = module_0.UnsafeProxy(*list_0)
    var_0 = ansible_unsafe_text_0.encode(**dict_0)
    ansible_unsafe_text_1 = module_0.AnsibleUnsafeText()
    var_1 = module_0.wrap_var(ansible_unsafe_text_1)
    ansible_unsafe_text_2 = module_0.AnsibleUnsafeText()
    ansible_unsafe_bytes_0 = module_0.AnsibleUnsafeBytes()
    var_2 = ansible_unsafe_bytes_0.decode()

def test_case_2():
    ansible_unsafe_text_0 = module_0.AnsibleUnsafeText()
    var_0 = ansible_unsafe_text_0.encode()
    var_1 = ansible_unsafe_text_0.encode()

def test_case_3():
    ansible_unsafe_text_0 = module_0.AnsibleUnsafeText()
    str_0 = 'HkC!HF[f+9]&F`(\x0c_'
    var_0 = ansible_unsafe_text_0.encode()
    list_0 = [var_0, str_0]
    var_1 = module_0.wrap_var(list_0)

def test_case_4():
    str_0 = 'm'
    var_0 = module_0.wrap_var(str_0)

def test_case_5():
    str_0 = 'HkC!HF[f+9]&F`(\x0c_'
    ansible_unsafe_text_0 = module_0.AnsibleUnsafeText()
    var_0 = ansible_unsafe_text_0.encode()
    var_1 = ansible_unsafe_text_0.encode()
    list_0 = [var_1, str_0]
    var_2 = module_0.wrap_var(list_0)
    ansible_unsafe_text_1 = module_0.AnsibleUnsafeText()
    list_1 = [ansible_unsafe_text_1, ansible_unsafe_text_1, ansible_unsafe_text_1]
    unsafe_proxy_0 = module_0.UnsafeProxy(*list_1)

def test_case_6():
    var_0 = None
    var_1 = module_0.wrap_var(var_0)
    str_0 = ''
    var_2 = module_0.wrap_var(str_0)
    str_1 = 'test'
    var_3 = module_0.wrap_var(str_1)
    var_4 = module_0.wrap_var(str_1)
    int_0 = 1
    var_5 = module_0.wrap_var(int_0)
    var_6 = module_0.wrap_var(int_0)
    var_7 = []
    var_8 = module_0.wrap_var(var_7)
    int_1 = 2
    int_2 = [int_0, int_1]
    var_9 = module_0.wrap_var(int_2)
    var_10 = tuple()
    var_11 = module_0.wrap_var(var_10)
    int_3 = (int_0, int_1)
    var_12 = module_0.wrap_var(int_3)
    var_13 = set()
    var_14 = module_0.wrap_var(var_13)
    int_4 = {int_0, int_1}
    var_15 = module_0.wrap_var(int_4)

def test_case_7():
    native_jinja_text_0 = module_1.NativeJinjaText()
    var_0 = module_0.wrap_var(native_jinja_text_0)