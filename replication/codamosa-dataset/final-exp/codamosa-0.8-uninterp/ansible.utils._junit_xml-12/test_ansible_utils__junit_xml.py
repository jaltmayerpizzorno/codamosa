# Automatically generated by Pynguin.
import ansible.utils._junit_xml as module_0
import decimal as module_1
import xml.etree.ElementTree as module_2

def test_case_0():
    pass

def test_case_1():
    test_failure_0 = module_0.TestFailure()

def test_case_2():
    str_0 = '\nattributes:\n    action:\n      details: While this action executes locally on the controller it is not governed by an action plugin\n      support: none\n    bypass_host_loop:\n      support: none\n    bypass_task_loop:\n      support: none\n    delegation:\n      details: Since there are no connection nor facts, there is no sense in delegating includes\n      support: none\n    tags:\n      details: Tags are interpreted by this action but are not automatically inherited by the include tasks, see C(apply)\n      support: partial\n'
    test_error_0 = module_0.TestError(str_0)

def test_case_3():
    str_0 = 'test'
    str_1 = 'unicode'
    test_case_0 = module_0.TestCase(str_0, str_1)
    element_0 = test_case_0.get_xml_element()

def test_case_4():
    str_0 = 'test'
    test_suite_0 = module_0.TestSuite(str_0)
    element_0 = test_suite_0.get_xml_element()

def test_case_5():
    test_suites_0 = module_0.TestSuites()
    dict_0 = test_suites_0.get_attributes()

def test_case_6():
    test_suites_0 = module_0.TestSuites()
    str_0 = 'M7w'
    int_0 = 5985
    decimal_0 = module_1.Decimal()
    bool_0 = True
    test_case_0 = module_0.TestCase(str_0, int_0, str_0, decimal_0, str_0, bool_0)
    var_0 = test_case_0.__repr__()
    str_1 = test_suites_0.to_pretty_xml()

def test_case_7():
    str_0 = 'test_case'
    int_0 = 1
    str_1 = 'test'
    float_0 = 2.2
    str_2 = 'test error'
    str_3 = 'some error output'
    test_error_0 = module_0.TestError(str_3, str_2)
    test_error_1 = [test_error_0]
    str_4 = 'test failure'
    str_5 = 'soe falure output'
    test_failure_0 = module_0.TestFailure(str_5, str_4)
    test_failure_1 = [test_failure_0]
    str_6 = 'A test has been marked as skipped.\nThis usually means that the test has failed to load or there is an incompatibility between the test and the environment.'
    str_7 = 'system out output'
    str_8 = 'system err output'
    bool_0 = True
    test_case_0 = module_0.TestCase(str_0, int_0, str_1, str_0, float_0, test_error_1, test_failure_1, str_6, str_7, str_8, bool_0)
    element_0 = test_case_0.get_xml_element()
    str_9 = 'unicode'
    var_0 = module_2.tostring(element_0, str_9)
    var_1 = print(var_0)

def test_case_8():
    str_0 = 'tst'
    none_type_0 = None
    str_1 = '%H:%M:%S'
    str_2 = 'vK]7bvAn'
    str_3 = '\\3eeRo/(KCL#o'
    dict_0 = {str_3: str_0, str_1: str_2, str_3: str_3}
    test_suite_0 = module_0.TestSuite(str_0, str_0, str_0, str_0, none_type_0, dict_0)
    element_0 = test_suite_0.get_xml_element()

def test_case_9():
    test_error_0 = module_0.TestError()
    float_0 = 975.46
    var_0 = test_error_0.__eq__(float_0)
    var_1 = test_error_0.__repr__()
    str_0 = 'Qp@,r#gx;@a9B='
    str_1 = '-(Je{08R_LU38'
    test_suite_0 = module_0.TestSuite(str_1)
    element_0 = test_suite_0.get_xml_element()
    str_2 = 'v '
    str_3 = None
    var_2 = test_suite_0.__repr__()
    dict_0 = {}
    decimal_0 = None
    test_error_1 = module_0.TestError()
    list_0 = [test_error_1]
    test_case_0 = module_0.TestCase(str_0, str_3, decimal_0, list_0)
    list_1 = [test_case_0]
    test_suite_1 = module_0.TestSuite(str_1, str_0, str_1, str_0, dict_0, dict_0, list_1)
    list_2 = [str_0]
    test_failure_0 = module_0.TestFailure(str_3, str_2)
    var_3 = test_failure_0.__eq__(list_2)
    element_1 = test_suite_1.get_xml_element()