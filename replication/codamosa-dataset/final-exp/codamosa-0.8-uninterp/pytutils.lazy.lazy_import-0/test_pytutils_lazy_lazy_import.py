# Automatically generated by Pynguin.
import pytutils.lazy.lazy_import as module_0

def test_case_0():
    pass

def test_case_1():
    dict_0 = {}
    bytes_0 = b'1\r'
    int_0 = 2595
    import_replacer_0 = module_0.ImportReplacer(dict_0, bytes_0, int_0)

def test_case_2():
    import_processor_0 = module_0.ImportProcessor()

def test_case_3():
    bytes_0 = b'$T,q\x1dq>\xc1\xbb\xd2*:'
    set_0 = {bytes_0}
    illegal_use_of_scope_replacer_0 = module_0.IllegalUseOfScopeReplacer(bytes_0, set_0, bytes_0)
    import_processor_0 = module_0.ImportProcessor()
    bool_0 = True
    float_0 = 3846.91
    illegal_use_of_scope_replacer_1 = module_0.IllegalUseOfScopeReplacer(bool_0, float_0)
    var_0 = illegal_use_of_scope_replacer_1.__eq__(illegal_use_of_scope_replacer_1)