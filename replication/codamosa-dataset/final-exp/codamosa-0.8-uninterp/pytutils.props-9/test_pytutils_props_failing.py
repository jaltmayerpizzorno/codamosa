# Automatically generated by Pynguin.
import pytutils.props as module_0

def test_case_0():
    try:
        list_0 = []
        setterproperty_0 = module_0.setterproperty(list_0)
        str_0 = 'Convert the given text into a bunch of lazy import objects.\n\n        This takes a text string, which should be similar to normal python\n        import markup.\n        '
        str_1 = '4\tu?"|H_sF\r^-QT|\x0cu9'
        tuple_0 = (str_1,)
        roclassproperty_0 = module_0.roclassproperty(tuple_0)
        roclassproperty_1 = module_0.roclassproperty(roclassproperty_0)
        var_0 = roclassproperty_1.__get__(setterproperty_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = ')'
        bool_0 = False
        tuple_0 = ()
        float_0 = -3307.11
        setterproperty_0 = module_0.setterproperty(tuple_0, float_0)
        var_0 = setterproperty_0.__set__(str_0, bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = -1210.80909
        var_0 = module_0.lazyclassproperty(float_0)
    except BaseException:
        pass