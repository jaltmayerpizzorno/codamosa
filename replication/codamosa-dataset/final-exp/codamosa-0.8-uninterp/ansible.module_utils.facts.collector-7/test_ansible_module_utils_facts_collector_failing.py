# Automatically generated by Pynguin.
import ansible.module_utils.facts.collector as module_0

def test_case_0():
    try:
        var_0 = module_0.collector_classes_from_gather_subset()
        str_0 = '}$`4d4Ua5\t\x0b$q)2s\x0cp'
        collector_not_found_error_0 = module_0.CollectorNotFoundError()
        base_fact_collector_0 = module_0.BaseFactCollector(str_0, collector_not_found_error_0)
        str_1 = '('
        int_0 = 1580
        var_1 = module_0.collector_classes_from_gather_subset(str_1, int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '^szk`:!ixLA_"'
        dict_0 = {str_0: str_0}
        list_0 = [dict_0, str_0]
        base_fact_collector_0 = module_0.BaseFactCollector(list_0)
        int_0 = -1533
        dict_1 = {}
        list_1 = [base_fact_collector_0, int_0, dict_1]
        var_0 = module_0.build_fact_id_to_collector_map(list_1)
    except BaseException:
        pass

def test_case_2():
    try:
        unresolved_fact_dep_0 = module_0.UnresolvedFactDep()
        str_0 = 'pD8mhx=2%4ZHV//_V*0D'
        dict_0 = {str_0: unresolved_fact_dep_0}
        list_0 = [dict_0]
        str_1 = 'h lyEI%uUyS17$+'
        dict_1 = {}
        tuple_0 = (str_1, dict_1)
        tuple_1 = (list_0, tuple_0)
        var_0 = module_0.find_unresolved_requires(dict_0, tuple_1)
    except BaseException:
        pass

def test_case_3():
    try:
        unresolved_fact_dep_0 = None
        list_0 = [unresolved_fact_dep_0, unresolved_fact_dep_0, unresolved_fact_dep_0]
        bytes_0 = b'\x1bC\xc6^\xa1\xac\xb4\xd4\x87\x9f\xcaYl\xe2@\x9aP\t'
        var_0 = module_0.resolve_requires(list_0, bytes_0)
    except BaseException:
        pass

def test_case_4():
    try:
        base_fact_collector_0 = module_0.BaseFactCollector()
        dict_0 = {}
        var_0 = module_0.get_collector_names(base_fact_collector_0, dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        collector_not_found_error_0 = module_0.CollectorNotFoundError()
        bool_0 = None
        var_0 = module_0.collector_classes_from_gather_subset(collector_not_found_error_0, bool_0)
    except BaseException:
        pass

def test_case_6():
    try:
        list_0 = []
        collector_not_found_error_0 = module_0.CollectorNotFoundError(*list_0)
        base_fact_collector_0 = module_0.BaseFactCollector()
        str_0 = "0\r`.b'u"
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        var_0 = module_0.find_unresolved_requires(str_0, dict_0)
    except BaseException:
        pass

def test_case_7():
    try:
        bytes_0 = b'\x1bC\xc6^\xa1\xac\xb4\xd4\x87\x9f\xcaYl\xe2@\x9aP\t'
        str_0 = 'P@,Nm\r9^'
        var_0 = module_0.build_dep_data(bytes_0, str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        bool_0 = False
        base_fact_collector_0 = module_0.BaseFactCollector()
        cycle_found_in_fact_deps_0 = module_0.CycleFoundInFactDeps()
        var_0 = module_0.collector_classes_from_gather_subset(bool_0)
        set_0 = {bool_0}
        list_0 = [set_0]
        var_1 = module_0.resolve_requires(set_0, list_0)
    except BaseException:
        pass

def test_case_9():
    try:
        bool_0 = False
        base_fact_collector_0 = module_0.BaseFactCollector()
        cycle_found_in_fact_deps_0 = module_0.CycleFoundInFactDeps()
        var_0 = module_0.collector_classes_from_gather_subset(bool_0)
        float_0 = -2023.215
        list_0 = [float_0, float_0, float_0]
        tuple_0 = (float_0, list_0)
        base_fact_collector_1 = module_0.BaseFactCollector(float_0)
        base_fact_collector_2 = module_0.BaseFactCollector(tuple_0, list_0)
        unresolved_fact_dep_0 = None
        bool_1 = False
        list_1 = [unresolved_fact_dep_0]
        str_0 = 'B>].Gb0WSx4 @/v2>I>-'
        var_1 = module_0.collector_classes_from_gather_subset(unresolved_fact_dep_0, unresolved_fact_dep_0, bool_1, list_1, str_0)
    except BaseException:
        pass

def test_case_10():
    try:
        bool_0 = False
        dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
        list_0 = None
        var_0 = module_0.get_collector_names(dict_0, list_0)
        base_fact_collector_0 = module_0.BaseFactCollector()
        set_0 = {base_fact_collector_0}
        var_1 = module_0.build_fact_id_to_collector_map(set_0)
        collector_not_found_error_0 = module_0.CollectorNotFoundError()
        var_2 = module_0.collector_classes_from_gather_subset(set_0, collector_not_found_error_0)
        var_3 = base_fact_collector_0.collect_with_namespace()
        dict_1 = {bool_0: var_3}
        base_fact_collector_1 = module_0.BaseFactCollector(base_fact_collector_0)
        bool_1 = False
        var_4 = module_0.collector_classes_from_gather_subset(dict_1, bool_1)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'insertbefore'
        str_1 = ';m'
        str_2 = [str_0, str_1]
        str_3 = [str_0]
        var_0 = module_0.get_collector_names(str_1, str_2, str_3)
    except BaseException:
        pass

def test_case_12():
    try:
        collector_not_found_error_0 = module_0.CollectorNotFoundError()
        list_0 = [collector_not_found_error_0, collector_not_found_error_0, collector_not_found_error_0]
        str_0 = '"<C\tv{>\\28!sn\'_S\n'
        int_0 = None
        var_0 = module_0.get_collector_names(int_0)
        bytes_0 = b'\xdf\xb6)\xb9\xf8X\xe3<\xb5\x16\xf2D\x03\x86\xdfv\xe0n2'
        var_1 = module_0.get_collector_names(list_0, str_0, collector_not_found_error_0, bytes_0)
    except BaseException:
        pass

def test_case_13():
    try:
        base_fact_collector_0 = module_0.BaseFactCollector()
        collector_not_found_error_0 = module_0.CollectorNotFoundError()
        var_0 = base_fact_collector_0.collect_with_namespace(collector_not_found_error_0)
        var_1 = base_fact_collector_0.collect_with_namespace()
        base_fact_collector_1 = module_0.BaseFactCollector()
        str_0 = '{'
        dict_0 = {str_0: str_0}
        var_2 = module_0.tsort(dict_0)
    except BaseException:
        pass