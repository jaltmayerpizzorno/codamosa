# Automatically generated by Pynguin.
import blib2to3.pgen2.grammar as module_0
import os as module_1

def test_case_0():
    try:
        grammar_0 = module_0.Grammar()
        path_like_0 = None
        grammar_0.dump(path_like_0)
    except BaseException:
        pass

def test_case_1():
    try:
        grammar_0 = module_0.Grammar()
        grammar_0.report()
        int_0 = 7
        str_0 = ':'
        grammar_0.dump(str_0)
        grammar_0.load(str_0)
        grammar_0.load(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        grammar_0 = module_0.Grammar()
        int_0 = 10
        grammar_0.load(int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'^9b\xca\xaf!c\xd3\xb9\x9d\x89\x9e\xb6L'
        grammar_0 = module_0.Grammar()
        grammar_0.loads(bytes_0)
    except BaseException:
        pass

def test_case_4():
    try:
        grammar_0 = module_0.Grammar()
        grammar_0.report()
        path_like_0 = module_1.PathLike()
    except BaseException:
        pass