# Automatically generated by Pynguin.
import ansible.utils._junit_xml as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '&<>"\''
    test_error_0 = module_0.TestError(str_0)
    element_0 = test_error_0.get_xml_element()

def test_case_2():
    str_0 = 'k4'
    test_suites_0 = module_0.TestSuites()
    str_1 = test_suites_0.to_pretty_xml()
    test_failure_0 = module_0.TestFailure(str_0, str_0)

def test_case_3():
    str_0 = '^L,^pR!@OUm'
    test_case_0 = module_0.TestCase(str_0, str_0)
    element_0 = test_case_0.get_xml_element()

def test_case_4():
    str_0 = '"A&enzo37i7!9j\x0buC'
    test_suite_0 = module_0.TestSuite(str_0)
    element_0 = test_suite_0.get_xml_element()

def test_case_5():
    str_0 = 'test'
    int_0 = 1
    str_1 = 'success'
    float_0 = 0.1
    str_2 = 'test_error_output'
    test_error_0 = module_0.TestError(str_2)
    test_error_1 = [test_error_0]
    str_3 = 'test_failure_output'
    test_failure_0 = module_0.TestFailure(str_3)
    test_failure_1 = [test_failure_0]
    str_4 = 'test_skipped'
    str_5 = 'test_out'
    str_6 = 'test_err'
    test_case_0 = module_0.TestCase(str_0, int_0, str_1, str_1, float_0, test_error_1, test_failure_1, str_4, str_5, str_6)
    element_0 = test_case_0.get_xml_element()