# Automatically generated by Pynguin.
import pytutils.lazy.simple_import as module_0

def test_case_0():
    try:
        str_0 = 'tmp.lazy_module'
        var_0 = module_0.make_lazy(str_0)
        var_1 = __import__(str_0)
    except BaseException:
        pass