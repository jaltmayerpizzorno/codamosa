# Automatically generated by Pynguin.
import ansible.utils.unsafe_proxy as module_0

def test_case_0():
    try:
        ansible_unsafe_bytes_0 = module_0.AnsibleUnsafeBytes()
        var_0 = ansible_unsafe_bytes_0.decode()
        bytes_0 = b'\xf2\x02\x87\xa1\x9fFt\x85!\xdb\x8d\xda\x88'
        var_1 = module_0.wrap_var(bytes_0)
        var_2 = module_0.to_unsafe_text()
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'<\xdbN\x97\x83\x9c\xe0\xb3\xe6\xf0\x0e\xe3'
        list_0 = [bytes_0]
        ansible_unsafe_text_0 = module_0.AnsibleUnsafeText()
        var_0 = ansible_unsafe_text_0.encode(*list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        set_0 = None
        dict_0 = {}
        dict_1 = {}
        native_jinja_unsafe_text_0 = module_0.NativeJinjaUnsafeText()
        list_0 = [native_jinja_unsafe_text_0, native_jinja_unsafe_text_0]
        list_1 = [native_jinja_unsafe_text_0, native_jinja_unsafe_text_0, list_0, list_0]
        unsafe_proxy_0 = module_0.UnsafeProxy(*list_1)
        var_0 = unsafe_proxy_0.__new__(set_0, dict_0, **dict_1)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'\xf2\x02\x87\xa1\x9fFt\x85!\xdb\x8d\xda\x88'
        var_0 = module_0.wrap_var(bytes_0)
        dict_0 = None
        ansible_unsafe_bytes_0 = module_0.AnsibleUnsafeBytes(**dict_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'<\xdbN\x97\x83\x9c\xe0\xb3\xe6\xf0\x0e\xe3'
        list_0 = [bytes_0]
        unsafe_proxy_0 = module_0.UnsafeProxy(*list_0)
        var_0 = module_0.to_unsafe_bytes()
    except BaseException:
        pass

def test_case_5():
    try:
        var_0 = module_0.to_unsafe_text()
    except BaseException:
        pass

def test_case_6():
    try:
        set_0 = set()
        var_0 = module_0.wrap_var(set_0)
        list_0 = None
        ansible_unsafe_text_0 = module_0.AnsibleUnsafeText()
        ansible_unsafe_0 = module_0.AnsibleUnsafe()
        var_1 = ansible_unsafe_text_0.encode(*list_0)
    except BaseException:
        pass

def test_case_7():
    try:
        bool_0 = False
        str_0 = None
        dict_0 = {str_0: bool_0, str_0: bool_0, str_0: bool_0}
        var_0 = module_0.wrap_var(dict_0)
        var_1 = module_0.wrap_var(bool_0)
        ansible_unsafe_0 = module_0.AnsibleUnsafe()
        unsafe_proxy_0 = module_0.UnsafeProxy()
    except BaseException:
        pass

def test_case_8():
    try:
        bool_0 = True
        var_0 = module_0.wrap_var(bool_0)
        ansible_unsafe_bytes_0 = None
        ansible_unsafe_0 = module_0.AnsibleUnsafe()
        ansible_unsafe_1 = module_0.AnsibleUnsafe()
        str_0 = ''
        str_1 = "O1D=rUG/2xa*FA'7}x)\r"
        str_2 = '%s %s %s\n'
        set_0 = {str_1, ansible_unsafe_bytes_0}
        var_1 = module_0.wrap_var(set_0)
        dict_0 = {str_0: str_0, str_1: ansible_unsafe_bytes_0, str_2: var_0}
        ansible_unsafe_text_0 = module_0.AnsibleUnsafeText()
        var_2 = ansible_unsafe_text_0.encode(**dict_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '8#@'
        list_0 = [str_0, str_0, str_0, str_0]
        unsafe_proxy_0 = module_0.UnsafeProxy(*list_0)
        bytes_0 = b'<\xc9tgj\x0bf\x00P\xc8\x8d'
        list_1 = [unsafe_proxy_0, bytes_0]
        str_1 = 'who'
        dict_0 = {str_1: list_1, str_0: bytes_0, str_0: list_0}
        ansible_unsafe_text_0 = module_0.AnsibleUnsafeText(*list_1, **dict_0)
    except BaseException:
        pass