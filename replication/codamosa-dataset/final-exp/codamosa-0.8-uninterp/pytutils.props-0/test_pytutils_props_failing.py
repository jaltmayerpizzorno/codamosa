# Automatically generated by Pynguin.
import pytutils.props as module_0

def test_case_0():
    try:
        str_0 = '\x0c|&hZlP'
        roclassproperty_0 = module_0.roclassproperty(str_0)
        bool_0 = False
        var_0 = roclassproperty_0.__get__(str_0, bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        list_0 = None
        bytes_0 = b'\xb0AOh*(\x0c~&\x8d\x91\xb4\x91{'
        setterproperty_0 = module_0.setterproperty(bytes_0)
        var_0 = setterproperty_0.__set__(list_0, list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\xad\xfc\x99%\xb04\x82R\xfdJ[\xb8k'
        var_0 = module_0.lazyclassproperty(bytes_0)
    except BaseException:
        pass