# Automatically generated by Pynguin.
import ansible.utils._junit_xml as module_0

def test_case_0():
    pass

def test_case_1():
    test_error_0 = module_0.TestError()
    element_0 = test_error_0.get_xml_element()
    var_0 = element_0.tag

def test_case_2():
    str_0 = ')B&"H"2\x0c'
    bool_0 = False
    test_case_0 = module_0.TestCase(str_0, str_0, str_0, bool_0)
    element_0 = test_case_0.get_xml_element()

def test_case_3():
    str_0 = " }7SSGYxo0e'?]2rff"
    test_suite_0 = module_0.TestSuite(str_0, str_0, str_0)
    dict_0 = test_suite_0.get_attributes()

def test_case_4():
    str_0 = 'login'
    test_suite_0 = module_0.TestSuite(str_0)
    element_0 = test_suite_0.get_xml_element()

def test_case_5():
    str_0 = "\n        :param role_names: A tuple of one or more role names.\n        :param role_paths: A tuple of one or more role paths.\n        :param entry_point: A role entry point name for filtering.\n\n        :returns: A dict indexed by role name, with 'collection', 'entry_points', and 'path' keys per role.\n        "
    list_0 = [str_0, str_0]
    str_1 = 'Q/n+-V13vP1'
    list_1 = []
    test_suite_0 = module_0.TestSuite(str_1, list_1)
    var_0 = test_suite_0.__eq__(list_0)
    test_suites_0 = module_0.TestSuites(str_0)
    str_2 = test_suites_0.to_pretty_xml()

def test_case_6():
    str_0 = 'LINES'
    test_case_0 = module_0.TestCase(str_0, str_0, str_0)
    str_1 = '6lB\rM?'
    test_suite_0 = module_0.TestSuite(str_1, str_0, str_0, str_1)
    var_0 = test_suite_0.__repr__()
    element_0 = test_suite_0.get_xml_element()
    element_1 = test_case_0.get_xml_element()
    test_error_0 = module_0.TestError(str_0, str_0)
    str_2 = '--user'
    list_0 = [test_suite_0]
    test_suites_0 = module_0.TestSuites(list_0)
    test_suites_1 = module_0.TestSuites(list_0)
    str_3 = test_suites_1.to_pretty_xml()
    dict_0 = test_suites_1.get_attributes()
    dict_1 = test_suite_0.get_attributes()
    test_failure_0 = module_0.TestFailure()
    var_1 = test_failure_0.__repr__()
    var_2 = test_error_0.__repr__()
    test_error_1 = module_0.TestError(str_2)
    test_suites_2 = module_0.TestSuites(str_2)
    test_suites_3 = module_0.TestSuites(str_2, list_0)
    element_2 = test_suites_3.get_xml_element()

def test_case_7():
    int_0 = 42
    str_0 = 'class_name'
    str_1 = 'name'
    str_2 = 'PASSED'
    float_0 = 1.23
    str_3 = 'Error message'
    str_4 = 'Error output'
    str_5 = 'Error type'
    test_error_0 = module_0.TestError(str_4, str_3, str_5)
    test_error_1 = [test_error_0]
    str_6 = 'Failure message'
    str_7 = 'Failure output'
    str_8 = 'Failure type'
    test_failure_0 = module_0.TestFailure(str_7, str_6, str_8)
    test_failure_1 = [test_failure_0]
    str_9 = 'Skipped reason'
    str_10 = 'System out'
    str_11 = 'System err'
    test_case_0 = module_0.TestCase(str_1, int_0, str_0, str_2, float_0, test_error_1, test_failure_1, str_9, str_10, str_11)
    element_0 = test_case_0.get_xml_element()