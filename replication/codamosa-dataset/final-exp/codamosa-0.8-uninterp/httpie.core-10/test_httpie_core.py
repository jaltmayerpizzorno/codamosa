# Automatically generated by Pynguin.
import httpie.core as module_0
import httpie.context as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = '\n    Mock environment for unit test for function main\n\n    '
    list_0 = [str_0, str_0]
    exit_status_0 = module_0.main(list_0)

def test_case_2():
    exit_status_0 = module_0.main()

def test_case_3():
    str_0 = 'ox-'
    str_1 = None
    str_2 = '{S;XX+Sd<v3'
    list_0 = [str_0, str_1, str_2]
    exit_status_0 = module_0.main(list_0)

def test_case_4():
    environment_0 = module_1.Environment()
    str_0 = 'httpie'
    str_1 = '--debug'
    str_2 = [str_0, str_1]
    exit_status_0 = module_0.main(str_2, environment_0)

def test_case_5():
    str_0 = '/0`\x0c\x0c_0>>~A\x0c"%|Z^JG'
    list_0 = [str_0, str_0]
    exit_status_0 = module_0.main(list_0)
    exit_status_1 = module_0.main()

def test_case_6():
    str_0 = 'http'
    str_1 = 'example.com'
    str_2 = [str_0, str_1]
    exit_status_0 = module_0.main(str_2)
    str_3 = '--download'
    str_4 = [str_0, str_3, str_1]
    exit_status_1 = module_0.main(str_4)

def test_case_7():
    str_0 = 'httpie'
    str_1 = '--headers'
    str_2 = 'www.baidu.com'
    str_3 = [str_0, str_1, str_2]
    exit_status_0 = module_0.main(str_3)
    str_4 = '--body'
    str_5 = [str_0, str_4, str_2]
    exit_status_1 = module_0.main(str_5)
    str_6 = '--output'
    str_7 = '/Users/lisong/ba.html'
    str_8 = [str_0, str_7, str_2, str_6, str_7]
    exit_status_2 = module_0.main(str_8)
    str_9 = '--check-status'
    str_10 = [str_0, str_9, str_2]
    exit_status_3 = module_0.main(str_10)
    str_11 = '--quideL'
    str_12 = [str_0, str_11, str_2]
    exit_status_4 = module_0.main(str_12)
    exit_status_5 = module_0.main(str_10)
    exit_status_6 = module_0.main(str_6)
    exit_status_7 = module_0.main()

def test_case_8():
    str_0 = 'httpie'
    str_1 = '--headers'
    str_2 = 'www.baidu.com'
    exit_status_0 = module_0.main(str_1)
    exit_status_1 = module_0.main(str_0)
    str_3 = '--download'
    str_4 = [str_0, str_3, str_2]
    exit_status_2 = module_0.main(str_4)
    str_5 = '--output-options'
    str_6 = [str_0, str_5, str_2]
    exit_status_3 = module_0.main(str_6)

def test_case_9():
    str_0 = 'httpie'
    str_1 = '--body'
    str_2 = [str_0, str_1, str_0]
    exit_status_0 = module_0.main(str_2)
    str_3 = '--download'
    str_4 = '/Users/lisong/ba.html'
    exit_status_1 = module_0.main(str_2)
    str_5 = [str_0, str_3, str_4]
    exit_status_2 = module_0.main(str_5)