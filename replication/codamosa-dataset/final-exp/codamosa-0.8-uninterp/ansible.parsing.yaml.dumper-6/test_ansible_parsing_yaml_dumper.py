# Automatically generated by Pynguin.
import ansible.parsing.yaml.dumper as module_0
import ansible.utils.unsafe_proxy as module_1

def test_case_0():
    pass

def test_case_1():
    var_0 = None
    ansible_dumper_0 = module_0.AnsibleDumper(var_0)
    ansible_unsafe_bytes_0 = module_1.AnsibleUnsafeBytes()
    var_1 = ansible_dumper_0.represent_data(ansible_unsafe_bytes_0)

def test_case_2():
    bytes_0 = b'\x03\x0e1\xf1\xb6\x11\x85\x0f'
    ansible_unsafe_text_0 = module_1.AnsibleUnsafeText()
    list_0 = [bytes_0]
    ansible_unsafe_bytes_0 = module_1.AnsibleUnsafeBytes()
    list_1 = [ansible_unsafe_bytes_0]
    ansible_dumper_0 = module_0.AnsibleDumper(list_0, ansible_unsafe_bytes_0, list_1, list_0)
    var_0 = ansible_dumper_0.represent_data(ansible_unsafe_text_0)