# Automatically generated by Pynguin.
import ansible.utils.unsafe_proxy as module_0

def test_case_0():
    try:
        dict_0 = {}
        var_0 = module_0.wrap_var(dict_0)
        ansible_unsafe_text_0 = module_0.AnsibleUnsafeText(**dict_0)
        list_0 = []
        ansible_unsafe_bytes_0 = module_0.AnsibleUnsafeBytes()
        var_1 = ansible_unsafe_bytes_0.decode(*list_0)
        var_2 = module_0.to_unsafe_bytes()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '<kWb)r(tbsNR>/zXfOv'
        int_0 = -2756
        dict_0 = {str_0: int_0}
        ansible_unsafe_text_0 = module_0.AnsibleUnsafeText()
        var_0 = ansible_unsafe_text_0.encode()
        var_1 = module_0.wrap_var(dict_0)
        unsafe_proxy_0 = module_0.UnsafeProxy()
    except BaseException:
        pass

def test_case_2():
    try:
        var_0 = module_0.to_unsafe_bytes()
    except BaseException:
        pass

def test_case_3():
    try:
        var_0 = module_0.to_unsafe_text()
    except BaseException:
        pass

def test_case_4():
    try:
        complex_0 = None
        ansible_unsafe_bytes_0 = module_0.AnsibleUnsafeBytes()
        var_0 = module_0.wrap_var(ansible_unsafe_bytes_0)
        list_0 = [complex_0, complex_0, complex_0]
        ansible_unsafe_text_0 = module_0.AnsibleUnsafeText(*list_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '];6~#:R3n=DZ=t*>!'
        list_0 = [str_0, str_0, str_0]
        unsafe_proxy_0 = module_0.UnsafeProxy(*list_0)
        list_1 = []
        unsafe_proxy_1 = module_0.UnsafeProxy(*list_1)
    except BaseException:
        pass