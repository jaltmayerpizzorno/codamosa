# Automatically generated by Pynguin.
import pytutils.path as module_0

def test_case_0():
    float_0 = 2639.985915
    str_0 = "\n\n    >>> log = logging.getLogger(__name__)\n    >>> configure()\n    >>> log.info('test')\n\n    "
    var_0 = module_0.join_each(float_0, str_0)

def test_case_1():
    str_0 = './a/b/c'
    str_1 = 'd'
    str_2 = 'e'
    str_3 = [str_1, str_2]
    var_0 = module_0.join_each(str_0, str_3)
    var_1 = tuple(var_0)