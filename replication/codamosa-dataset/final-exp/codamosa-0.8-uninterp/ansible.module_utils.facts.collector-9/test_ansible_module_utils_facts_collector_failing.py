# Automatically generated by Pynguin.
import ansible.module_utils.facts.collector as module_0

def test_case_0():
    try:
        str_0 = 'TaskQueueManager'
        dict_0 = {}
        var_0 = module_0.find_unresolved_requires(str_0, dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = 1498.45
        set_0 = {float_0}
        bytes_0 = b'k\xa5\x0f\xa5\xddrx\x81yr\xbd\xe6V\x8fs\xcfU{'
        var_0 = module_0.resolve_requires(set_0, bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'q%xpBoVg'
        dict_0 = {}
        var_0 = module_0.resolve_requires(str_0, dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        base_fact_collector_0 = module_0.BaseFactCollector()
        tuple_0 = (base_fact_collector_0,)
        set_0 = {tuple_0, base_fact_collector_0, base_fact_collector_0}
        list_0 = [tuple_0, base_fact_collector_0, set_0]
        var_0 = module_0.get_collector_names(tuple_0, list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        base_fact_collector_0 = module_0.BaseFactCollector()
        tuple_0 = (base_fact_collector_0,)
        list_0 = [tuple_0]
        bool_0 = False
        var_0 = module_0.find_unresolved_requires(list_0, bool_0)
    except BaseException:
        pass

def test_case_5():
    try:
        dict_0 = None
        var_0 = module_0.collector_classes_from_gather_subset(dict_0)
        str_0 = '\\>vC+]b^@\\ zKYn'
        base_fact_collector_0 = module_0.BaseFactCollector(str_0)
        var_1 = base_fact_collector_0.collect()
        bool_0 = True
        var_2 = module_0.collector_classes_from_gather_subset(dict_0, base_fact_collector_0, bool_0)
    except BaseException:
        pass

def test_case_6():
    try:
        bool_0 = True
        dict_0 = {}
        var_0 = module_0.collector_classes_from_gather_subset(bool_0, dict_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'CBJp|~M'
        dict_0 = None
        var_0 = module_0.get_collector_names(str_0, dict_0, str_0)
        unresolved_fact_dep_0 = module_0.UnresolvedFactDep()
        var_1 = module_0.build_fact_id_to_collector_map(dict_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = ''
        var_0 = module_0.get_collector_names(str_0)
        unresolved_fact_dep_0 = module_0.UnresolvedFactDep()
        base_fact_collector_0 = module_0.BaseFactCollector()
        var_1 = base_fact_collector_0.collect()
        base_fact_collector_1 = module_0.BaseFactCollector()
        set_0 = {base_fact_collector_1}
        var_2 = module_0.collector_classes_from_gather_subset(set_0)
        int_0 = 419
        var_3 = base_fact_collector_1.collect()
        var_4 = module_0.get_collector_names(base_fact_collector_0, set_0, int_0, set_0)
    except BaseException:
        pass

def test_case_9():
    try:
        float_0 = 2312.0
        int_0 = 1196
        dict_0 = {}
        collector_not_found_error_0 = module_0.CollectorNotFoundError(**dict_0)
        base_fact_collector_0 = module_0.BaseFactCollector(int_0, collector_not_found_error_0)
        var_0 = base_fact_collector_0.collect_with_namespace(float_0)
        str_0 = ''
        var_1 = module_0.get_collector_names(str_0)
        bytes_0 = b'\x87\xc8\xee\xc9\x9e'
        unresolved_fact_dep_0 = module_0.UnresolvedFactDep()
        base_fact_collector_1 = module_0.BaseFactCollector()
        var_2 = base_fact_collector_1.collect_with_namespace()
        set_0 = {unresolved_fact_dep_0, collector_not_found_error_0, bytes_0}
        int_1 = 724
        var_3 = module_0.collector_classes_from_gather_subset(collector_not_found_error_0, dict_0, set_0, collector_not_found_error_0, int_1)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'CBJp|~M'
        dict_0 = None
        str_1 = 'Av!J]Z'
        var_0 = module_0.get_collector_names(str_0, dict_0, str_1)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'E>{3'
        str_1 = '7WTHoB2\\1)y@'
        dict_0 = {str_0: str_0, str_1: str_0}
        var_0 = module_0.tsort(dict_0)
        dict_1 = {}
        collector_not_found_error_0 = module_0.CollectorNotFoundError(**dict_1)
        str_2 = ''
        var_1 = module_0.get_collector_names(str_2)
        unresolved_fact_dep_0 = module_0.UnresolvedFactDep()
        base_fact_collector_0 = module_0.BaseFactCollector()
        set_0 = {base_fact_collector_0}
        var_2 = module_0.collector_classes_from_gather_subset(set_0)
        cycle_found_in_fact_deps_0 = module_0.CycleFoundInFactDeps(**dict_1)
        bytes_0 = b'\x12'
        base_fact_collector_1 = module_0.BaseFactCollector(var_2)
        var_3 = base_fact_collector_0.collect_with_namespace()
        str_3 = 'fs0>p+Y$,a+/'
        var_4 = module_0.get_collector_names(unresolved_fact_dep_0, bytes_0, str_3)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'E>{3'
        str_1 = '7WTHoB2\\1)y@'
        dict_0 = {str_0: str_0, str_1: str_0}
        var_0 = module_0.tsort(dict_0)
        float_0 = -123.0
        int_0 = 1196
        dict_1 = {}
        collector_not_found_error_0 = module_0.CollectorNotFoundError(**dict_1)
        base_fact_collector_0 = module_0.BaseFactCollector(int_0, collector_not_found_error_0)
        var_1 = base_fact_collector_0.collect_with_namespace(float_0)
        var_2 = module_0.get_collector_names(str_0)
        unresolved_fact_dep_0 = module_0.UnresolvedFactDep()
        base_fact_collector_1 = module_0.BaseFactCollector()
        var_3 = base_fact_collector_1.collect_with_namespace()
        var_4 = base_fact_collector_1.collect()
        base_fact_collector_2 = module_0.BaseFactCollector()
        set_0 = {base_fact_collector_1, base_fact_collector_2, base_fact_collector_0}
        var_5 = module_0.collector_classes_from_gather_subset(set_0)
        cycle_found_in_fact_deps_0 = module_0.CycleFoundInFactDeps(**dict_1)
        bytes_0 = b'\xea'
        base_fact_collector_3 = module_0.BaseFactCollector(bytes_0)
        var_6 = base_fact_collector_2.collect_with_namespace()
        var_7 = module_0.get_collector_names(unresolved_fact_dep_0, bytes_0, str_1)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'R'
        str_1 = '7WTHoB2\\1)y@'
        dict_0 = {str_0: str_0, str_1: str_0}
        var_0 = module_0.tsort(dict_0)
    except BaseException:
        pass

def test_case_14():
    try:
        dict_0 = None
        str_0 = 'Av!J]Z'
        var_0 = module_0.get_collector_names(str_0, dict_0, str_0)
        cycle_found_in_fact_deps_0 = module_0.CycleFoundInFactDeps(**dict_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = '\n    ^\n        (?P<major>0|[1-9]\\d*)\n        \\.\n        (?P<minor>0|[1-9]\\d*)\n        \\.\n        (?P<patch>0|[1-9]\\d*)\n        (?:\n            -\n            (?P<prerelease>\n                (?:0|[1-9]\\d*|\\d*[a-zA-Z-][0-9a-zA-Z-]*)\n                (?:\\.(?:0|[1-9]\\d*|\\d*[a-zA-Z-][0-9a-zA-Z-]*))*\n            )\n        )?\n        (?:\n            \\+\n            (?P<buildmetadata>[0-9a-zA-Z-]+(?:\\.[0-9a-zA-Z-]+)*)\n        )?\n    $\n    '
        str_1 = 'M'
        str_2 = 'ba^V &Zx~Q_4mv97B?]'
        dict_0 = {str_0: str_0, str_1: str_1, str_2: str_0, str_0: str_2}
        var_0 = module_0.tsort(dict_0)
    except BaseException:
        pass