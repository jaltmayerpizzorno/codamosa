# Automatically generated by Pynguin.
import ansible.utils.unsafe_proxy as module_0
import ansible.utils.native_jinja as module_1

def test_case_0():
    try:
        ansible_unsafe_text_0 = None
        list_0 = [ansible_unsafe_text_0, ansible_unsafe_text_0]
        var_0 = module_0.wrap_var(list_0)
        ansible_unsafe_bytes_0 = module_0.AnsibleUnsafeBytes()
        var_1 = ansible_unsafe_bytes_0.decode(*list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        ansible_unsafe_text_0 = module_0.AnsibleUnsafeText()
        var_0 = ansible_unsafe_text_0.encode()
        bytes_0 = b"\xc8\xbd\x85\xe4\x04\xdc\xbc6\xb0'\x12\x8b"
        list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
        native_jinja_unsafe_text_0 = module_0.NativeJinjaUnsafeText()
        dict_0 = {}
        ansible_unsafe_bytes_0 = module_0.AnsibleUnsafeBytes(**dict_0)
        var_1 = ansible_unsafe_bytes_0.decode(**dict_0)
        var_2 = module_0.to_unsafe_bytes(*list_0)
        ansible_unsafe_bytes_1 = module_0.AnsibleUnsafeBytes(*list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'ju6x_i"\x0crT-;oLl~Jq\t6'
        list_0 = [str_0]
        unsafe_proxy_0 = module_0.UnsafeProxy(*list_0)
        unsafe_proxy_1 = module_0.UnsafeProxy()
    except BaseException:
        pass

def test_case_3():
    try:
        ansible_unsafe_bytes_0 = module_0.AnsibleUnsafeBytes()
        var_0 = ansible_unsafe_bytes_0.decode()
        var_1 = ansible_unsafe_bytes_0.decode()
        dict_0 = {}
        var_2 = module_0.wrap_var(dict_0)
        ansible_unsafe_0 = module_0.AnsibleUnsafe()
        var_3 = module_0.to_unsafe_bytes()
    except BaseException:
        pass

def test_case_4():
    try:
        native_jinja_unsafe_text_0 = module_0.NativeJinjaUnsafeText()
        list_0 = [native_jinja_unsafe_text_0]
        bytes_0 = b'\xfc\xd4R'
        ansible_unsafe_text_0 = module_0.AnsibleUnsafeText()
        unsafe_proxy_0 = module_0.UnsafeProxy(*list_0)
        var_0 = unsafe_proxy_0.__new__(bytes_0, ansible_unsafe_text_0, *list_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'Destination %s is not readable'
        str_1 = 'Twy'
        ansible_unsafe_bytes_0 = module_0.AnsibleUnsafeBytes()
        list_0 = [str_1, str_0, ansible_unsafe_bytes_0, ansible_unsafe_bytes_0]
        dict_0 = {str_1: ansible_unsafe_bytes_0, str_0: str_1}
        var_0 = module_0.wrap_var(dict_0)
        native_jinja_unsafe_text_0 = module_0.NativeJinjaUnsafeText(*list_0)
    except BaseException:
        pass

def test_case_6():
    try:
        ansible_unsafe_text_0 = None
        ansible_unsafe_bytes_0 = module_0.AnsibleUnsafeBytes()
        list_0 = [ansible_unsafe_text_0, ansible_unsafe_text_0]
        var_0 = ansible_unsafe_bytes_0.decode()
        var_1 = module_0.to_unsafe_text(*list_0)
        var_2 = module_0.wrap_var(list_0)
        dict_0 = {}
        unsafe_proxy_0 = module_0.UnsafeProxy(*list_0, **dict_0)
        str_0 = '~2u"2lo7JSz,Y<a5_'
        set_0 = {var_1}
        tuple_0 = (set_0,)
        tuple_1 = (tuple_0, unsafe_proxy_0)
        tuple_2 = (tuple_1, ansible_unsafe_bytes_0, tuple_0, dict_0)
        list_1 = [set_0]
        tuple_3 = (str_0, tuple_2, list_1, str_0)
        ansible_unsafe_0 = module_0.AnsibleUnsafe()
        var_3 = module_0.wrap_var(tuple_3)
        native_jinja_text_0 = module_1.NativeJinjaText()
        var_4 = module_0.wrap_var(native_jinja_text_0)
        var_5 = module_0.to_unsafe_bytes()
    except BaseException:
        pass