# Automatically generated by Pynguin.
import blib2to3.pgen2.literals as module_0
import re as module_1

def test_case_0():
    try:
        str_0 = "w0cqP6!aFVEZR'Nz"
        str_1 = module_0.evalString(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        module_0.test()
        str_0 = '"'
        str_1 = module_0.evalString(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        module_0.test()
        str_0 = '"[^\\n"\\\\]*(?:\\\\.[^\\n"\\\\]*)*'
        str_1 = module_0.evalString(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = "'\\x01\\x02\\x03\\04x05\\x6\\x07'"
        str_1 = module_0.evalString(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        module_0.test()
        str_0 = '"""'
        str_1 = module_0.evalString(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = "'\\x01\\x02\\x03\\x04x05\\x6\\x07'"
        str_1 = module_0.evalString(str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '(.*)\\\\a(.*)'
        str_1 = 'foo\\abar'
        var_0 = module_1.match(str_0, str_1)
        str_2 = module_0.escape(var_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = "'\\x61\\x62\\x6'"
        str_1 = module_0.evalString(str_0)
    except BaseException:
        pass