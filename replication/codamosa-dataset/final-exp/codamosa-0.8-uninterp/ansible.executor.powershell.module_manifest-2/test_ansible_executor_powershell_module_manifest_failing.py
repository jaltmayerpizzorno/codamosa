# Automatically generated by Pynguin.
import ansible.executor.powershell.module_manifest as module_0

def test_case_0():
    try:
        str_0 = '/dev/xencons'
        p_s_module_dep_finder_0 = module_0.PSModuleDepFinder()
        var_0 = p_s_module_dep_finder_0.scan_exec_script(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'W\x1b.\xa1\xf4['
        str_0 = '\n        Example contents /sys/class/fc_host/*/port_name:\n\n        0x21000014ff52a9bb\n\n        '
        complex_0 = None
        p_s_module_dep_finder_0 = module_0.PSModuleDepFinder()
        var_0 = p_s_module_dep_finder_0.scan_module(bytes_0, str_0, str_0, complex_0)
        str_1 = 'async_wrapper'
        p_s_module_dep_finder_1 = module_0.PSModuleDepFinder()
        var_1 = p_s_module_dep_finder_1.scan_exec_script(str_1)
        dict_0 = {str_1: var_1}
        var_2 = p_s_module_dep_finder_1.scan_exec_script(dict_0)
    except BaseException:
        pass