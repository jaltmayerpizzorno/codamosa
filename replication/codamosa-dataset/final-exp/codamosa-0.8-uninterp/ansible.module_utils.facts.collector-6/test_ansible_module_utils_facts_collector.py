# Automatically generated by Pynguin.
import ansible.module_utils.facts.collector as module_0

def test_case_0():
    base_fact_collector_0 = module_0.BaseFactCollector()

def test_case_1():
    base_fact_collector_0 = module_0.BaseFactCollector()
    var_0 = base_fact_collector_0.collect_with_namespace()

def test_case_2():
    var_0 = module_0.collector_classes_from_gather_subset()

def test_case_3():
    base_fact_collector_0 = module_0.BaseFactCollector()
    set_0 = {base_fact_collector_0, base_fact_collector_0, base_fact_collector_0, base_fact_collector_0}
    list_0 = [base_fact_collector_0]
    str_0 = '!D\x0bUsvc]\r\\c{D'
    var_0 = module_0.collector_classes_from_gather_subset(list_0, str_0, set_0)

def test_case_4():
    base_fact_collector_0 = module_0.BaseFactCollector()
    dict_0 = {base_fact_collector_0: base_fact_collector_0, base_fact_collector_0: base_fact_collector_0}
    var_0 = module_0.build_fact_id_to_collector_map(dict_0)

def test_case_5():
    base_fact_collector_0 = module_0.BaseFactCollector()
    str_0 = '<9\nm(>'
    base_fact_collector_1 = module_0.BaseFactCollector(str_0)
    var_0 = base_fact_collector_1.collect(base_fact_collector_0)

def test_case_6():
    str_0 = '[.Ako('
    var_0 = module_0.get_collector_names(str_0, str_0, str_0)

def test_case_7():
    unresolved_fact_dep_0 = module_0.UnresolvedFactDep()
    list_0 = [unresolved_fact_dep_0, unresolved_fact_dep_0, unresolved_fact_dep_0]
    bool_0 = True
    base_fact_collector_0 = module_0.BaseFactCollector(list_0, bool_0)
    var_0 = base_fact_collector_0.collect_with_namespace()

def test_case_8():
    var_0 = module_0.collector_classes_from_gather_subset()
    str_0 = '=R=#+|]Z%ZW.xI9D'
    list_0 = [var_0, var_0, var_0, var_0]
    base_fact_collector_0 = module_0.BaseFactCollector(list_0)
    var_1 = base_fact_collector_0.collect(str_0)
    str_1 = 's)T\rljj(\tX-|m01Dqg`'
    base_fact_collector_1 = module_0.BaseFactCollector(str_1)
    int_0 = None
    tuple_0 = (base_fact_collector_1, int_0)
    var_2 = module_0.resolve_requires(tuple_0, tuple_0)

def test_case_9():
    str_0 = 'Km+x.CnS_[2Hh*S=U1h'
    dict_0 = {str_0: str_0}
    var_0 = module_0.tsort(dict_0)
    dict_1 = {str_0: str_0}
    list_0 = None
    str_1 = "Vt8'ybE4Je\x0cXC+AW7yC"
    var_1 = module_0.collector_classes_from_gather_subset(list_0, str_1, dict_1)

def test_case_10():
    var_0 = module_0.collector_classes_from_gather_subset()
    str_0 = 'Np'
    dict_0 = {str_0: var_0, str_0: var_0}
    unresolved_fact_dep_0 = module_0.UnresolvedFactDep()
    var_1 = module_0.find_unresolved_requires(dict_0, dict_0)

def test_case_11():
    str_0 = '!\x0bUsvc]\r\\c{D'
    var_0 = module_0.get_collector_names(str_0, str_0, str_0)