# Automatically generated by Pynguin.
import ansible.utils._junit_xml as module_0
import decimal as module_1

def test_case_0():
    try:
        test_suites_0 = module_0.TestSuites()
        str_0 = test_suites_0.to_pretty_xml()
        str_1 = 'IF$fHx\\:.JRLY_Z'
        dict_0 = {}
        var_0 = test_suites_0.__eq__(dict_0)
        test_result_0 = module_0.TestResult(str_1)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '28~U8Ip_}/\t'
        test_suites_0 = module_0.TestSuites()
        str_1 = test_suites_0.to_pretty_xml()
        test_suite_0 = module_0.TestSuite(str_0, str_0, str_0)
        test_failure_0 = module_0.TestFailure()
        str_2 = '3ySZ>^>yTn"\tp'
        test_error_0 = module_0.TestError(str_2, str_2)
        dict_0 = test_suites_0.get_attributes()
        list_0 = [test_error_0, test_error_0]
        test_case_0 = module_0.TestCase(str_2, str_2, list_0)
        var_0 = test_failure_0.__repr__()
        str_3 = 'chown is not implemented for Powershell'
        str_4 = None
        dict_1 = {str_4: str_4, str_3: str_3, str_4: str_4}
        test_suites_1 = module_0.TestSuites()
        test_suite_1 = module_0.TestSuite(str_4, str_2)
        element_0 = test_case_0.get_xml_element()
        var_1 = test_suite_1.__repr__()
        dict_2 = test_suite_1.get_attributes()
        test_error_1 = module_0.TestError()
        int_0 = 423
        bool_0 = None
        test_case_1 = module_0.TestCase(str_0, int_0, bool_0)
        str_5 = 'oKEQ_'
        list_1 = [test_case_1]
        test_suite_2 = module_0.TestSuite(str_5, str_3, str_5, dict_1, list_1)
        element_1 = test_suite_2.get_xml_element()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '})YRnYW`#nwC'
        test_failure_0 = module_0.TestFailure(str_0)
        var_0 = test_failure_0.__repr__()
        test_error_0 = module_0.TestError(str_0, str_0)
        list_0 = [test_error_0, test_error_0, test_error_0]
        test_suite_0 = module_0.TestSuite(str_0)
        test_failure_1 = module_0.TestFailure(str_0)
        list_1 = [test_failure_1]
        test_case_0 = module_0.TestCase(str_0, str_0, str_0, list_0, list_1, str_0, str_0, str_0)
        element_0 = test_case_0.get_xml_element()
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '28~U8Ip_}/\t'
        test_suites_0 = module_0.TestSuites()
        str_1 = test_suites_0.to_pretty_xml()
        test_suite_0 = module_0.TestSuite(str_0, str_0, str_0)
        test_failure_0 = module_0.TestFailure()
        str_2 = '3ySZ>>^>yTn"\tp'
        test_error_0 = module_0.TestError(str_2, str_2)
        dict_0 = test_suites_0.get_attributes()
        list_0 = [test_error_0, test_error_0]
        test_case_0 = module_0.TestCase(str_2, str_2, list_0)
        var_0 = test_failure_0.__repr__()
        str_3 = 'chown is not implemented for Powershell'
        str_4 = None
        test_suite_1 = module_0.TestSuite(str_4, str_2)
        element_0 = test_case_0.get_xml_element()
        var_1 = test_suite_1.__repr__()
        list_1 = [test_case_0, test_case_0]
        test_suite_2 = module_0.TestSuite(str_0, str_3, str_2, dict_0, list_1, str_0, str_2)
        dict_1 = test_suite_2.get_attributes()
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '28~U8Ip_}/\t'
        test_suites_0 = module_0.TestSuites()
        str_1 = test_suites_0.to_pretty_xml()
        str_2 = test_suites_0.to_pretty_xml()
        test_suite_0 = module_0.TestSuite(str_0, str_0, str_0)
        test_failure_0 = module_0.TestFailure()
        str_3 = '3ySZ>>^>yTn"\tp'
        test_error_0 = module_0.TestError(str_3, str_3)
        dict_0 = test_suites_0.get_attributes()
        list_0 = [test_error_0, test_error_0]
        test_case_0 = module_0.TestCase(str_3, str_3, list_0)
        var_0 = test_failure_0.__repr__()
        str_4 = 'chown is not implemented for Powershell'
        str_5 = None
        dict_1 = {str_5: str_5, str_4: str_4, str_5: str_5}
        test_suite_1 = module_0.TestSuite(str_5, str_3)
        element_0 = test_failure_0.get_xml_element()
        var_1 = test_suite_1.__repr__()
        test_error_1 = module_0.TestError()
        element_1 = test_case_0.get_xml_element()
        str_6 = 'Y9`pCWW(nyI6B'
        str_7 = '\n        Method for options validation to use in \'load_data\' for TaskInclude and HandlerTaskInclude\n        since they share the same validations. It is not named \'validate_options\' on purpose\n        to prevent confusion with \'_validate_*" methods. Note that the task passed might be changed\n        as a side-effect of this method.\n        '
        str_8 = test_suites_0.to_pretty_xml()
        dict_2 = {}
        decimal_0 = module_1.Decimal(**dict_2)
        str_9 = 'Invalid color supplied to display: %s'
        bool_0 = True
        test_case_1 = module_0.TestCase(str_7, decimal_0, list_0, str_5, str_9, bool_0)
        list_1 = [test_case_1]
        test_suite_2 = module_0.TestSuite(str_6, str_4, dict_1, list_1, str_5, str_4)
        element_2 = test_suite_2.get_xml_element()
    except BaseException:
        pass