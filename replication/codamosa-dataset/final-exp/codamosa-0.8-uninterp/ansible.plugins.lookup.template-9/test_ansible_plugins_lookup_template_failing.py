# Automatically generated by Pynguin.
import ansible.plugins.lookup.template as module_0

def test_case_0():
    try:
        bool_0 = False
        bytes_0 = b'\x8a$\xe2\xf3y\x7f\x02\x96<\x7ff\xedi\xcc\xc0'
        dict_0 = {}
        lookup_module_0 = module_0.LookupModule(**dict_0)
        var_0 = lookup_module_0.run(bool_0, bytes_0)
    except BaseException:
        pass