# Automatically generated by Pynguin.
import pytutils.lazy.lazy_import as module_0

def test_case_0():
    pass

def test_case_1():
    bytes_0 = b'>!\x87(\x08\xf0\x17\xadG\xbc\x98\xde\xccs\xec?\x9a\x8f'
    str_0 = 'LINEMODE'
    set_0 = {bytes_0, bytes_0, bytes_0, bytes_0}
    list_0 = [set_0, set_0, bytes_0, bytes_0]
    bytes_1 = b'"\xf5\xcb'
    illegal_use_of_scope_replacer_0 = module_0.IllegalUseOfScopeReplacer(set_0, list_0, bytes_1)
    var_0 = illegal_use_of_scope_replacer_0.__eq__(str_0)

def test_case_2():
    var_0 = module_0.disallow_proxying()

def test_case_3():
    int_0 = 2697
    import_processor_0 = module_0.ImportProcessor(int_0)

def test_case_4():
    import_processor_0 = module_0.ImportProcessor()