# Automatically generated by Pynguin.
import blib2to3.pgen2.grammar as module_0

def test_case_0():
    try:
        grammar_0 = module_0.Grammar()
        str_0 = 'a*#|o};Qj3\rFq\ny5'
        grammar_0.dump(str_0)
        grammar_1 = module_0.Grammar()
        str_1 = "r(\\X'##,b1"
        grammar_0.load(str_1)
    except BaseException:
        pass

def test_case_1():
    try:
        grammar_0 = module_0.Grammar()
        bytes_0 = b'+\xc3z%E\xc23s\xa5E\xcbP\xb8\x84\x12[{\xa4x\xbc'
        grammar_0.loads(bytes_0)
    except BaseException:
        pass