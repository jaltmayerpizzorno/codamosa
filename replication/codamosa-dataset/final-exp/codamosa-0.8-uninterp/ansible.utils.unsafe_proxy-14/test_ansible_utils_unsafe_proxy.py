# Automatically generated by Pynguin.
import ansible.utils.unsafe_proxy as module_0
import ansible.utils.native_jinja as module_1

def test_case_0():
    ansible_unsafe_0 = module_0.AnsibleUnsafe()

def test_case_1():
    str_0 = '?x1@gq{M0'
    dict_0 = {str_0: str_0}
    list_0 = [dict_0, str_0, str_0, dict_0]
    unsafe_proxy_0 = module_0.UnsafeProxy(*list_0)
    ansible_unsafe_text_0 = module_0.AnsibleUnsafeText()

def test_case_2():
    dict_0 = None
    var_0 = module_0.wrap_var(dict_0)

def test_case_3():
    float_0 = -179.097768
    var_0 = module_0.wrap_var(float_0)

def test_case_4():
    native_jinja_unsafe_text_0 = module_0.NativeJinjaUnsafeText()
    ansible_unsafe_bytes_0 = module_0.AnsibleUnsafeBytes()
    ansible_unsafe_0 = module_0.AnsibleUnsafe()
    var_0 = module_0.wrap_var(ansible_unsafe_0)

def test_case_5():
    float_0 = -179.097768
    dict_0 = None
    var_0 = module_0.wrap_var(dict_0)
    list_0 = [float_0, float_0, dict_0]
    var_1 = module_0.wrap_var(list_0)

def test_case_6():
    list_0 = []
    ansible_unsafe_bytes_0 = module_0.AnsibleUnsafeBytes()
    bytes_0 = b'\x8d\xca\x99\xca'
    int_0 = 304
    tuple_0 = (list_0, bytes_0, int_0)
    var_0 = module_0.wrap_var(tuple_0)

def test_case_7():
    dict_0 = None
    var_0 = module_0.wrap_var(dict_0)
    str_0 = 'ojGbe>SdFz&B^C\x0bEq}K'
    var_1 = module_0.wrap_var(str_0)

def test_case_8():
    float_0 = -179.097768
    ansible_unsafe_0 = module_0.AnsibleUnsafe()
    str_0 = '\\>xEi, Rxt'
    dict_0 = {str_0: float_0}
    var_0 = module_0.wrap_var(dict_0)

def test_case_9():
    str_0 = 'test'
    var_0 = module_0.wrap_var(str_0)
    int_0 = 123
    var_1 = module_0.wrap_var(int_0)
    str_1 = 'k1'
    str_2 = 'k2'
    str_3 = {str_1: str_0, str_2: str_0}
    var_2 = module_0.wrap_var(str_3)
    native_jinja_text_0 = module_1.NativeJinjaText()
    var_3 = module_0.wrap_var(native_jinja_text_0)