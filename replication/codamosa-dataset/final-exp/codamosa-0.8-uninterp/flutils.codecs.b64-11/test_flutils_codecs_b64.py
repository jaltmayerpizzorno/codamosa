# Automatically generated by Pynguin.
import flutils.codecs.b64 as module_0

def test_case_0():
    module_0.register()

def test_case_1():
    str_0 = ''
    tuple_0 = module_0.encode(str_0)

def test_case_2():
    bytes_0 = b''
    tuple_0 = module_0.decode(bytes_0)

def test_case_3():
    str_0 = 'RM\x0c/LAk95^'
    module_0.register()
    tuple_0 = module_0.encode(str_0)
    module_0.register()
    module_0.register()
    module_0.register()
    module_0.register()
    dict_0 = {}
    tuple_1 = module_0.decode(dict_0)
    tuple_2 = module_0.encode(str_0)