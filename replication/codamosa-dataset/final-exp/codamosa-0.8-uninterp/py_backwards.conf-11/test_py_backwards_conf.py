# Automatically generated by Pynguin.
import py_backwards.conf as module_0
import argparse as module_1

def test_case_0():
    settings_0 = module_0.Settings()

def test_case_1():
    namespace_0 = module_1.Namespace()
    str_0 = 'debug'
    bool_0 = True
    var_0 = setattr(namespace_0, str_0, bool_0)
    module_0.init_settings(namespace_0)

def test_case_2():
    namespace_0 = module_1.Namespace()
    str_0 = 'debug'
    settings_0 = module_0.Settings()
    bool_0 = False
    var_0 = namespace_0.__eq__(bool_0)
    var_1 = setattr(namespace_0, str_0, bool_0)
    module_0.init_settings(namespace_0)