# Automatically generated by Pynguin.
import ansible.module_utils.facts.virtual.linux as module_0

def test_case_0():
    try:
        bytes_0 = b'\xa2\x95$C\xb6\xe1\x1c7X'
        linux_virtual_0 = module_0.LinuxVirtual(bytes_0)
        var_0 = linux_virtual_0.get_virtual_facts()
    except BaseException:
        pass