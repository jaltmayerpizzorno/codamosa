# Automatically generated by Pynguin.
import py_backwards.conf as module_0
import argparse as module_1

def test_case_0():
    settings_0 = module_0.Settings()

def test_case_1():
    str_0 = 'debug'
    bool_0 = True
    bool_1 = {str_0: bool_0}
    namespace_0 = module_1.Namespace(**bool_1)
    module_0.init_settings(namespace_0)

def test_case_2():
    str_0 = 'debug'
    settings_0 = module_0.Settings()
    bool_0 = False
    bool_1 = {str_0: bool_0}
    namespace_0 = module_1.Namespace(**bool_1)
    module_0.init_settings(namespace_0)