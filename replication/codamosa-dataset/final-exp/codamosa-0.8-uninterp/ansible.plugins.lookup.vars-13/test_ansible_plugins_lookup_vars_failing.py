# Automatically generated by Pynguin.
import ansible.plugins.lookup.vars as module_0

def test_case_0():
    try:
        str_0 = '}'
        lookup_module_0 = module_0.LookupModule(str_0)
        bytes_0 = b'\x1b\xf0\xf6\xa1\x9a\xeb\xa9=\xb1\xa7\x050'
        dict_0 = {}
        var_0 = lookup_module_0.run(bytes_0, **dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'n]fHW~f6}f/*by,4`!D\r'
        str_1 = '1'
        float_0 = 528.337
        dict_0 = {str_0: str_0, str_1: float_0}
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.run(str_0, dict_0)
    except BaseException:
        pass