# Automatically generated by Pynguin.
import ansible.executor.powershell.module_manifest as module_0

def test_case_0():
    p_s_module_dep_finder_0 = module_0.PSModuleDepFinder()

def test_case_1():
    p_s_module_dep_finder_0 = module_0.PSModuleDepFinder()
    bytes_0 = b'\xf7'
    var_0 = p_s_module_dep_finder_0.scan_module(bytes_0)

def test_case_2():
    p_s_module_dep_finder_0 = module_0.PSModuleDepFinder()
    bytes_0 = b'%\x8a\r'
    list_0 = [bytes_0, p_s_module_dep_finder_0]
    var_0 = p_s_module_dep_finder_0.scan_module(bytes_0, bytes_0, list_0)

def test_case_3():
    bytes_0 = b'S38j\xde\x13!\xfc\xb3'
    str_0 = 'o0;e\x0b#c5sB[Wt:?m\\K'
    tuple_0 = (str_0,)
    str_1 = 'k+n!{Z=)2G$6$s>8I'
    set_0 = set()
    p_s_module_dep_finder_0 = module_0.PSModuleDepFinder()
    var_0 = p_s_module_dep_finder_0.scan_module(bytes_0, tuple_0, str_1, set_0)