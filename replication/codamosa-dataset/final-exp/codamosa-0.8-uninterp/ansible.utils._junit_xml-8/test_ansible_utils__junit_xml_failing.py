# Automatically generated by Pynguin.
import decimal as module_0
import ansible.utils._junit_xml as module_1

def test_case_0():
    try:
        str_0 = 'pnq@t0EF*j)D4V'
        decimal_0 = module_0.Decimal()
        test_error_0 = module_1.TestError()
        list_0 = [test_error_0, test_error_0, test_error_0, test_error_0]
        test_failure_0 = module_1.TestFailure()
        list_1 = [test_failure_0]
        test_case_0 = module_1.TestCase(str_0, str_0, str_0, decimal_0, list_0, list_1, str_0, str_0)
        element_0 = test_case_0.get_xml_element()
    except BaseException:
        pass

def test_case_1():
    try:
        test_suites_0 = module_1.TestSuites()
        test_error_0 = module_1.TestError()
        var_0 = test_error_0.__eq__(test_suites_0)
        element_0 = test_suites_0.get_xml_element()
        str_0 = 'svAtKSo"'
        str_1 = 'L_#!KrL'
        str_2 = 'I8'
        dict_0 = {str_1: str_2}
        str_3 = None
        int_0 = 604800
        test_failure_0 = module_1.TestFailure(str_2, str_2)
        list_0 = [test_failure_0]
        test_case_0 = module_1.TestCase(str_3, int_0, list_0)
        list_1 = [test_case_0]
        str_4 = 'Z;lL@T4t['
        test_suite_0 = module_1.TestSuite(str_0, str_0, dict_0, list_1, str_4)
        element_1 = test_suite_0.get_xml_element()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = "Uh8^\nZ#OBY7W[8~'y"
        str_1 = 'q|{Dex\x0cMD5%23UIwxb'
        int_0 = None
        test_case_0 = module_1.TestCase(str_0, int_0, str_0, str_1)
        list_0 = None
        test_suite_0 = module_1.TestSuite(str_1, str_0, list_0, str_0)
        list_1 = [str_0, test_suite_0, str_1, str_0]
        var_0 = test_case_0.__repr__()
        test_suite_1 = module_1.TestSuite(str_1, list_1, str_1)
        test_suites_0 = module_1.TestSuites(str_0)
        element_0 = test_case_0.get_xml_element()
        list_2 = [test_suite_0, test_suite_0, test_suite_1, test_suite_1]
        test_suites_1 = module_1.TestSuites(str_0, list_2)
        str_2 = test_suites_1.to_pretty_xml()
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'U/'
        test_suites_0 = module_1.TestSuites()
        str_1 = test_suites_0.to_pretty_xml()
        dict_0 = {}
        test_failure_0 = module_1.TestFailure(str_0)
        var_0 = test_failure_0.__repr__()
        list_0 = []
        bool_0 = True
        test_case_0 = module_1.TestCase(str_0, bool_0)
        element_0 = test_case_0.get_xml_element()
        test_case_1 = module_1.TestCase(str_0, str_0, list_0)
        element_1 = test_case_1.get_xml_element()
        tuple_0 = (element_1,)
        test_failure_1 = module_1.TestFailure(str_0)
        var_1 = test_failure_1.__eq__(tuple_0)
        test_suites_1 = module_1.TestSuites(str_0)
        element_2 = test_suites_1.get_xml_element()
        str_2 = 'Sorry, try again.'
        list_1 = [test_suites_1, element_2, var_0]
        str_3 = 'JFmf&4I5K*")'
        bool_1 = True
        test_suite_0 = module_1.TestSuite(str_3, str_2, bool_1, str_2)
        test_suite_1 = module_1.TestSuite(str_0, str_0, str_2, list_1, dict_0, str_2)
        element_3 = test_suite_1.get_xml_element()
    except BaseException:
        pass