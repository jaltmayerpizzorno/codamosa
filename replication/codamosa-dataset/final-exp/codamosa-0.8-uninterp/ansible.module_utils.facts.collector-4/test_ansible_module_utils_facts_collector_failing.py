# Automatically generated by Pynguin.
import ansible.module_utils.facts.collector as module_0
import collections as module_1

def test_case_0():
    try:
        base_fact_collector_0 = module_0.BaseFactCollector()
        var_0 = base_fact_collector_0.collect_with_namespace()
        dict_0 = {base_fact_collector_0: base_fact_collector_0, base_fact_collector_0: base_fact_collector_0, base_fact_collector_0: base_fact_collector_0, base_fact_collector_0: base_fact_collector_0}
        var_1 = module_0.find_collectors_for_platform(base_fact_collector_0, dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '$*Xq.z>lmy#'
        float_0 = -973.0
        var_0 = module_0.resolve_requires(str_0, float_0)
    except BaseException:
        pass

def test_case_2():
    try:
        collector_not_found_error_0 = module_0.CollectorNotFoundError()
        dict_0 = {}
        str_0 = '\n    - name: Show configured default become user\n      debug: msg="{{ lookup(\'config\', \'DEFAULT_BECOME_USER\')}}"\n\n    - name: print out role paths\n      debug:\n        msg: "These are the configured role paths: {{lookup(\'config\', \'DEFAULT_ROLES_PATH\')}}"\n\n    - name: find retry files, skip if missing that key\n      find:\n        paths: "{{lookup(\'config\', \'RETRY_FILES_SAVE_PATH\')|default(playbook_dir, True)}}"\n        patterns: "*.retry"\n\n    - name: see the colors\n      debug: msg="{{item}}"\n      loop: "{{lookup(\'config\', \'COLOR_OK\', \'COLOR_CHANGED\', \'COLOR_SKIP\', wantlist=True)}}"\n\n    - name: skip if bad value in var\n      debug: msg="{{ lookup(\'config\', config_in_var, on_missing=\'skip\')}}"\n      var:\n        config_in_var: UNKNOWN\n\n    - name: show remote user and port for ssh connection\n      debug: msg={{q("config", "remote_user", "port", plugin_type="connection", plugin_name="ssh", on_missing=\'skip\')}}\n\n    - name: show remote_tmp setting for shell (sh) plugin\n      debug: msg={{q("config", "remote_tmp", plugin_type="shell", plugin_name="sh")}}\n'
        bool_0 = None
        str_1 = 'T?'
        base_fact_collector_0 = module_0.BaseFactCollector(str_1)
        var_0 = base_fact_collector_0.collect_with_namespace(bool_0)
        base_fact_collector_1 = module_0.BaseFactCollector()
        var_1 = base_fact_collector_1.collect_with_namespace(dict_0, str_0)
        var_2 = module_0.resolve_requires(str_1, str_1)
        unresolved_fact_dep_0 = module_0.UnresolvedFactDep()
        var_3 = module_0.get_collector_names(unresolved_fact_dep_0)
    except BaseException:
        pass

def test_case_3():
    try:
        list_0 = []
        bytes_0 = b'\x0c/b\xc8V\xc6\xb4\xda'
        var_0 = module_0.resolve_requires(list_0, bytes_0)
        unresolved_fact_dep_0 = module_0.UnresolvedFactDep()
        float_0 = -1537.4
        base_fact_collector_0 = module_0.BaseFactCollector(float_0)
        var_1 = base_fact_collector_0.collect()
        var_2 = module_0.build_dep_data(unresolved_fact_dep_0, list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'I'
        base_fact_collector_0 = module_0.BaseFactCollector()
        base_fact_collector_1 = module_0.BaseFactCollector(str_0, base_fact_collector_0)
        var_0 = base_fact_collector_0.collect_with_namespace(base_fact_collector_1)
        var_1 = module_0.tsort(base_fact_collector_1)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = ',[8%Zb5a~-?=2}iUr%9k'
        list_0 = [str_0, str_0, str_0, str_0]
        unresolved_fact_dep_0 = module_0.UnresolvedFactDep(*list_0)
        base_fact_collector_0 = module_0.BaseFactCollector()
        tuple_0 = (base_fact_collector_0,)
        collector_not_found_error_0 = module_0.CollectorNotFoundError()
        var_0 = module_0.collector_classes_from_gather_subset(list_0, list_0, unresolved_fact_dep_0, tuple_0, collector_not_found_error_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '@'
        dict_0 = {}
        base_fact_collector_0 = module_0.BaseFactCollector(dict_0)
        base_fact_collector_1 = module_0.BaseFactCollector()
        var_0 = module_0.collector_classes_from_gather_subset()
        base_fact_collector_2 = module_0.BaseFactCollector(str_0, base_fact_collector_1)
        var_1 = base_fact_collector_0.collect_with_namespace()
        float_0 = None
        var_2 = module_0.find_unresolved_requires(str_0, float_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'a'
        str_1 = 'b'
        str_2 = 'c'
        var_0 = set()
        str_3 = [str_2]
        var_1 = set(str_3)
        str_4 = [str_0]
        var_2 = set(str_4)
        var_3 = {str_0: var_0, str_1: var_1, str_2: var_2}
        var_4 = module_0.tsort(var_3)
        str_5 = [str_1]
        var_5 = set(str_5)
        str_6 = [str_0]
        var_6 = set(str_6)
        var_7 = {str_0: var_5, str_1: var_6}
        var_8 = module_0.tsort(var_7)
    except BaseException:
        pass

def test_case_8():
    try:
        list_0 = []
        collector_not_found_error_0 = module_0.CollectorNotFoundError()
        defaultdict_0 = module_1.defaultdict()
        str_0 = '(A!VfQa[yktA=2\n?|@'
        var_0 = module_0.get_collector_names(list_0, defaultdict_0, str_0, defaultdict_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'I'
        base_fact_collector_0 = module_0.BaseFactCollector()
        float_0 = -753.6
        base_fact_collector_1 = module_0.BaseFactCollector(float_0)
        var_0 = base_fact_collector_0.collect()
        str_1 = '(Jz>N]=7_\x0c7'
        dict_0 = {str_0: str_0}
        var_1 = module_0.find_unresolved_requires(str_1, dict_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = ''
        base_fact_collector_0 = module_0.BaseFactCollector()
        base_fact_collector_1 = module_0.BaseFactCollector(str_0, base_fact_collector_0)
        tuple_0 = (base_fact_collector_0,)
        str_1 = 'ansible.legacy.assemble'
        dict_0 = {str_0: base_fact_collector_0, str_1: str_1}
        set_0 = {base_fact_collector_0, tuple_0}
        var_0 = module_0.resolve_requires(dict_0, set_0)
    except BaseException:
        pass

def test_case_11():
    try:
        cycle_found_in_fact_deps_0 = module_0.CycleFoundInFactDeps()
        defaultdict_0 = module_1.defaultdict()
        set_0 = {cycle_found_in_fact_deps_0, cycle_found_in_fact_deps_0}
        bytes_0 = b'\xca\xef\x88\xad]N\xe3\xa26\xf8\x9d\x9adq\xb1/w'
        base_fact_collector_0 = module_0.BaseFactCollector(set_0, bytes_0)
        dict_0 = {}
        float_0 = 4.9318
        var_0 = module_0.get_collector_names(set_0, dict_0, float_0, cycle_found_in_fact_deps_0)
    except BaseException:
        pass