# Automatically generated by Pynguin.
import ansible.utils._junit_xml as module_0

def test_case_0():
    pass

def test_case_1():
    test_failure_0 = module_0.TestFailure()

def test_case_2():
    str_0 = 'Output text'
    str_1 = 'Custom message type'
    test_error_0 = module_0.TestError(str_0, str_0, str_1)
    element_0 = test_error_0.get_xml_element()

def test_case_3():
    str_0 = 'name'
    test_case_0 = module_0.TestCase(str_0)
    element_0 = test_case_0.get_xml_element()

def test_case_4():
    str_0 = '~-ER\x0b_I}[\\~;^ {b'
    test_suite_0 = module_0.TestSuite(str_0, str_0, str_0)
    dict_0 = test_suite_0.get_attributes()

def test_case_5():
    str_0 = '3/mPyJ--:E0;=*Mf/Bi'
    list_0 = []
    test_suite_0 = module_0.TestSuite(str_0, str_0, str_0, list_0)
    element_0 = test_suite_0.get_xml_element()

def test_case_6():
    list_0 = []
    list_1 = []
    test_suites_0 = module_0.TestSuites(list_0, list_1)
    element_0 = test_suites_0.get_xml_element()

def test_case_7():
    test_suites_0 = module_0.TestSuites()
    str_0 = test_suites_0.to_pretty_xml()
    test_error_0 = module_0.TestError()
    element_0 = test_error_0.get_xml_element()

def test_case_8():
    str_0 = 'Custom message type'
    test_error_0 = module_0.TestError(str_0, str_0, str_0)

def test_case_9():
    str_0 = '$YLIb-k1//|z)6}p'
    str_1 = 'yu(?7t'
    str_2 = None
    dict_0 = {str_1: str_1, str_2: str_0}
    str_3 = 'ac\x0c:{_YRX,*QG$,T'
    bool_0 = False
    test_case_0 = module_0.TestCase(str_3, bool_0, str_0, str_3)
    list_0 = [test_case_0, test_case_0, test_case_0]
    test_suite_0 = module_0.TestSuite(str_1, str_1, dict_0, list_0)
    list_1 = [test_suite_0, test_suite_0, test_suite_0]
    test_suites_0 = module_0.TestSuites(str_0, list_1)
    str_4 = test_suites_0.to_pretty_xml()