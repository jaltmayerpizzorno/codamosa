# Automatically generated by Pynguin.
import ansible.plugins.lookup.vars as module_0

def test_case_0():
    try:
        dict_0 = None
        lookup_module_0 = module_0.LookupModule(dict_0)
        str_0 = ',Y@!\r\n3('
        dict_1 = {str_0: str_0}
        lookup_module_1 = module_0.LookupModule()
        lookup_module_2 = module_0.LookupModule()
        var_0 = lookup_module_1.run(str_0, dict_1)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\xce\xd7\xf3\xa6\xac]\xbbf@\xc2L\xfd\xd1'
        set_0 = {bytes_0, bytes_0}
        str_0 = "~\njzC$iV~'2"
        lookup_module_0 = module_0.LookupModule(str_0)
        var_0 = lookup_module_0.run(set_0)
    except BaseException:
        pass