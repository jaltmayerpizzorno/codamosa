# Automatically generated by Pynguin.
import ansible.module_utils.facts.collector as module_0

def test_case_0():
    try:
        var_0 = module_0.collector_classes_from_gather_subset()
        str_0 = 'l6ti~8.(g]a&W6Fjl'
        collector_not_found_error_0 = module_0.CollectorNotFoundError()
        var_1 = module_0.find_unresolved_requires(str_0, collector_not_found_error_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = True
        set_0 = {bool_0, bool_0}
        base_fact_collector_0 = module_0.BaseFactCollector(set_0)
        var_0 = module_0.resolve_requires(base_fact_collector_0, base_fact_collector_0)
    except BaseException:
        pass

def test_case_2():
    try:
        var_0 = module_0.collector_classes_from_gather_subset()
        str_0 = 'sc|7`.ZW)8g5/'
        tuple_0 = ()
        var_1 = module_0.resolve_requires(str_0, tuple_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '((,&[10mFipVhdaw\\&>'
        dict_0 = {str_0: str_0}
        var_0 = module_0.tsort(dict_0)
        unresolved_fact_dep_0 = module_0.UnresolvedFactDep()
        var_1 = module_0.collector_classes_from_gather_subset(str_0, unresolved_fact_dep_0)
    except BaseException:
        pass

def test_case_4():
    try:
        var_0 = module_0.collector_classes_from_gather_subset()
        str_0 = 'f(@x-u{P'
        dict_0 = {}
        var_1 = module_0.resolve_requires(dict_0, dict_0)
        defaultdict_0 = None
        unresolved_fact_dep_0 = module_0.UnresolvedFactDep()
        base_fact_collector_0 = module_0.BaseFactCollector(unresolved_fact_dep_0, str_0)
        var_2 = base_fact_collector_0.collect_with_namespace()
        bytes_0 = b'\xfa\xb5K\xed\xb1n'
        list_0 = [str_0]
        var_3 = module_0.get_collector_names(defaultdict_0, bytes_0, list_0)
    except BaseException:
        pass

def test_case_5():
    try:
        cycle_found_in_fact_deps_0 = module_0.CycleFoundInFactDeps()
        var_0 = module_0.collector_classes_from_gather_subset()
        var_1 = module_0.get_collector_names()
        bool_0 = False
        str_0 = 'l6ti~8.(g]a&W6Fjl'
        list_0 = [bool_0]
        dict_0 = {str_0: str_0}
        var_2 = module_0.find_unresolved_requires(list_0, dict_0)
    except BaseException:
        pass

def test_case_6():
    try:
        base_fact_collector_0 = module_0.BaseFactCollector()
        bool_0 = None
        list_0 = []
        str_0 = "cT\x0b}SEi>5L<mj?'M"
        dict_0 = {str_0: str_0, str_0: base_fact_collector_0}
        var_0 = module_0.get_collector_names(bool_0, list_0, dict_0)
    except BaseException:
        pass

def test_case_7():
    try:
        collector_not_found_error_0 = module_0.CollectorNotFoundError()
        dict_0 = {collector_not_found_error_0: collector_not_found_error_0}
        var_0 = module_0.resolve_requires(dict_0, dict_0)
        cycle_found_in_fact_deps_0 = None
        tuple_0 = (cycle_found_in_fact_deps_0,)
        str_0 = None
        var_1 = module_0.find_unresolved_requires(tuple_0, str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        base_fact_collector_0 = None
        bool_0 = False
        dict_0 = {}
        bytes_0 = b'\x8d$d^8\x1d\xec\x00\xbc\xfb\xe8E\x84\x80\xfbd\x83<'
        var_0 = module_0.get_collector_names(bool_0, dict_0, base_fact_collector_0, bytes_0)
        base_fact_collector_1 = module_0.BaseFactCollector()
        list_0 = [base_fact_collector_1, base_fact_collector_1]
        var_1 = module_0.collector_classes_from_gather_subset(list_0)
        var_2 = base_fact_collector_1.collect()
        str_0 = ''
        var_3 = module_0.find_collectors_for_platform(str_0, list_0)
        str_1 = 'c9Rk&gS-(u[^_'
        dict_1 = {str_1: str_1}
        var_4 = module_0.select_collector_classes(dict_1, dict_1)
        str_2 = '+.&2XCfF'
        float_0 = 2542.619
        var_5 = module_0.find_unresolved_requires(str_2, float_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '`U+37Q\t>&]AF>!z'
        bytes_0 = b'iN\xd30\xa1{q\xbdR\x94\xde#\xcc^\x90?&\xc7\x04\xf9'
        base_fact_collector_0 = module_0.BaseFactCollector()
        var_0 = base_fact_collector_0.collect(bytes_0)
        str_1 = '^2(T\x0cV%K:F~gIk1'
        str_2 = "\t\t-}hb2-'$M\tIB"
        dict_0 = {str_0: str_0, str_0: str_0, str_1: str_0, str_2: str_1}
        var_1 = module_0.select_collector_classes(dict_0, dict_0)
        str_3 = 'o0(`Rm%K'
        str_4 = 'f8bH>'
        bytes_1 = b'\xb0d'
        set_0 = {bytes_1, str_3}
        var_2 = module_0.get_collector_names(str_4, set_0)
        base_fact_collector_1 = module_0.BaseFactCollector()
        var_3 = module_0.tsort(base_fact_collector_1)
    except BaseException:
        pass

def test_case_10():
    try:
        base_fact_collector_0 = module_0.BaseFactCollector()
        list_0 = [base_fact_collector_0, base_fact_collector_0]
        var_0 = module_0.collector_classes_from_gather_subset(list_0)
        str_0 = 'n:1eK}JrUW[^9]D]>'
        collector_not_found_error_0 = module_0.CollectorNotFoundError()
        str_1 = 'z'
        dict_0 = {str_0: list_0, str_1: str_1}
        var_1 = module_0.tsort(dict_0)
    except BaseException:
        pass

def test_case_11():
    try:
        float_0 = 636.60752
        bytes_0 = b'\x9aBF"y\xb0M\xce\x9dM\x88g\x02'
        str_0 = 'GlM=SDf>/'
        cycle_found_in_fact_deps_0 = module_0.CycleFoundInFactDeps()
        str_1 = '13][8YAHdFe8.l.^^6-'
        var_0 = module_0.collector_classes_from_gather_subset(float_0, bytes_0, str_0, cycle_found_in_fact_deps_0, str_1)
    except BaseException:
        pass

def test_case_12():
    try:
        var_0 = module_0.collector_classes_from_gather_subset()
        unresolved_fact_dep_0 = module_0.UnresolvedFactDep()
        str_0 = 'dgIY;_v'
        base_fact_collector_0 = module_0.BaseFactCollector(unresolved_fact_dep_0, str_0)
        list_0 = [str_0]
        dict_0 = {}
        var_1 = module_0.get_collector_names(str_0, dict_0, list_0)
        base_fact_collector_1 = module_0.BaseFactCollector()
    except BaseException:
        pass