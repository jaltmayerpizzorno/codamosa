# Automatically generated by Pynguin.
import ansible.inventory.manager as module_0

def test_case_0():
    try:
        float_0 = 2603.7788824643394
        str_0 = "\x0c#<D8'%S)\rb%cT&[1,"
        inventory_manager_0 = module_0.InventoryManager(str_0)
        var_0 = inventory_manager_0.get_host(float_0)
        var_1 = inventory_manager_0.remove_restriction()
        str_1 = '&V{LS2:'
        var_2 = inventory_manager_0.get_hosts(str_1, inventory_manager_0)
        var_3 = inventory_manager_0.list_hosts()
        str_2 = '_>u1\x0b,\x0b@x@.\r*sZ]#2#'
        int_0 = 569
        var_4 = inventory_manager_0.list_hosts(int_0)
        var_5 = inventory_manager_0.subset(str_2)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = -2245
        bytes_0 = b''
        inventory_manager_0 = module_0.InventoryManager(int_0, bytes_0)
        var_0 = inventory_manager_0.restrict_to_hosts(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'mV]43i,V!(+]}y}'
        dict_0 = {}
        var_0 = module_0.order_patterns(dict_0)
        set_0 = {str_0, str_0}
        dict_1 = {}
        inventory_manager_0 = module_0.InventoryManager(dict_1, set_0)
        var_1 = inventory_manager_0.remove_restriction()
        inventory_manager_1 = module_0.InventoryManager(str_0, set_0)
        var_2 = inventory_manager_1.get_hosts()
        int_0 = -430
        var_3 = inventory_manager_0.add_host(int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '\rwOt`vd29\x0b9,|x{nbz'
        bool_0 = False
        inventory_manager_0 = module_0.InventoryManager(bool_0)
        var_0 = inventory_manager_0.parse_source(str_0)
        var_1 = inventory_manager_0.add_group(bool_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '\rwOt`vd29\x0b9,|x{nbz'
        inventory_manager_0 = module_0.InventoryManager(str_0)
        var_0 = inventory_manager_0.reconcile_inventory()
        bool_0 = False
        var_1 = inventory_manager_0.refresh_inventory()
        inventory_manager_1 = module_0.InventoryManager(bool_0)
        var_2 = inventory_manager_1.parse_source(str_0)
        var_3 = inventory_manager_0.add_group(bool_0)
    except BaseException:
        pass

def test_case_5():
    try:
        float_0 = None
        str_0 = 'warning'
        dict_0 = {str_0: float_0}
        inventory_manager_0 = module_0.InventoryManager(str_0, dict_0)
        float_1 = 512.0
        var_0 = inventory_manager_0.list_hosts(float_1)
        var_1 = inventory_manager_0.reconcile_inventory()
        dict_1 = {float_0: float_0, float_0: float_0}
        list_0 = [dict_1, float_0, dict_1]
        var_2 = inventory_manager_0.list_groups()
        var_3 = inventory_manager_0.add_host(list_0)
    except BaseException:
        pass

def test_case_6():
    try:
        float_0 = 784.0
        bytes_0 = b'4\xe1b\x13\xf5U\xff\x07\xd4\xfa5d\xcc\xf9'
        str_0 = ''
        inventory_manager_0 = module_0.InventoryManager(float_0, bytes_0, str_0)
        var_0 = inventory_manager_0.remove_restriction()
        bytes_1 = b'\x96v\x0e\xceI\xe1'
        var_1 = module_0.split_host_pattern(bytes_1)
        str_1 = 'TkO*jE(v+FBN>0p//@\tr'
        dict_0 = {}
        tuple_0 = (dict_0, dict_0)
        inventory_manager_1 = module_0.InventoryManager(str_1, tuple_0)
    except BaseException:
        pass

def test_case_7():
    try:
        float_0 = None
        str_0 = 'warning'
        dict_0 = {str_0: float_0}
        inventory_manager_0 = module_0.InventoryManager(str_0, dict_0)
        var_0 = inventory_manager_0.list_hosts(float_0)
        list_0 = None
        var_1 = inventory_manager_0.get_hosts(list_0, dict_0)
        var_2 = inventory_manager_0.reconcile_inventory()
        list_1 = [dict_0, float_0, dict_0]
        int_0 = -2879
        inventory_manager_1 = module_0.InventoryManager(int_0)
        var_3 = inventory_manager_0.refresh_inventory()
        var_4 = inventory_manager_1.subset(list_1)
        float_1 = -1911.1811
        var_5 = inventory_manager_0.get_groups_dict()
        var_6 = inventory_manager_1.restrict_to_hosts(float_1)
    except BaseException:
        pass

def test_case_8():
    try:
        float_0 = None
        dict_0 = {float_0: float_0, float_0: float_0, float_0: float_0, float_0: float_0}
        list_0 = [dict_0, float_0]
        float_1 = -766.09
        int_0 = 158
        set_0 = {float_1, int_0}
        str_0 = "'d&5q-wx>J"
        inventory_manager_0 = module_0.InventoryManager(str_0)
        var_0 = inventory_manager_0.subset(str_0)
        var_1 = inventory_manager_0.parse_source(set_0)
        var_2 = inventory_manager_0.list_hosts()
        var_3 = inventory_manager_0.parse_source(float_0)
        var_4 = inventory_manager_0.restrict_to_hosts(list_0)
    except BaseException:
        pass

def test_case_9():
    try:
        float_0 = None
        int_0 = 0
        int_1 = 4319
        bool_0 = True
        str_0 = 'E\x0c_\r#kwc'
        set_0 = {str_0}
        inventory_manager_0 = module_0.InventoryManager(str_0, set_0)
        var_0 = inventory_manager_0.get_hosts(float_0, int_0, int_1, bool_0)
    except BaseException:
        pass

def test_case_10():
    try:
        list_0 = []
        list_1 = []
        inventory_manager_0 = module_0.InventoryManager(list_1)
        var_0 = inventory_manager_0.parse_sources()
        var_1 = inventory_manager_0.list_hosts(list_1)
        bytes_0 = b'M<\xfd*\xb0\xa1'
        var_2 = inventory_manager_0.list_hosts(bytes_0)
        int_0 = None
        var_3 = inventory_manager_0.reconcile_inventory()
        str_0 = '18'
        inventory_manager_1 = module_0.InventoryManager(int_0, str_0)
        bool_0 = False
        inventory_manager_2 = module_0.InventoryManager(list_0)
        tuple_0 = (inventory_manager_1, inventory_manager_2, inventory_manager_1)
        inventory_manager_3 = module_0.InventoryManager(bool_0, tuple_0)
    except BaseException:
        pass

def test_case_11():
    try:
        tuple_0 = None
        set_0 = {tuple_0, tuple_0, tuple_0, tuple_0}
        int_0 = -1467
        bool_0 = True
        tuple_1 = (tuple_0, set_0, int_0, bool_0)
        var_0 = module_0.order_patterns(tuple_1)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = '\nansible_facts:\n  description: Facts to add to ansible_facts.\n  returned: always\n  type: complex\n  contains:\n    packages:\n      description:\n        - Maps the package name to a non-empty list of dicts with package information.\n        - Every dict in the list corresponds to one installed version of the package.\n        - The fields described below are present for all package managers. Depending on the\n          package manager, there might be more fields for a package.\n      returned: when operating system level package manager is specified or auto detected manager\n      type: dict\n      contains:\n        name:\n          description: The package\'s name.\n          returned: always\n          type: str\n        version:\n          description: The package\'s version.\n          returned: always\n          type: str\n        source:\n          description: Where information on the package came from.\n          returned: always\n          type: str\n      sample: |-\n        {\n          "packages": {\n            "kernel": [\n              {\n                "name": "kernel",\n                "source": "rpm",\n                "version": "3.10.0",\n                ...\n              },\n              {\n                "name": "kernel",\n                "source": "rpm",\n                "version": "3.10.0",\n                ...\n              },\n              ...\n            ],\n            "kernel-tools": [\n              {\n                "name": "kernel-tools",\n                "source": "rpm",\n                "version": "3.10.0",\n                ...\n              }\n            ],\n            ...\n          }\n        }\n        # Sample rpm\n        {\n          "packages": {\n            "kernel": [\n              {\n                "arch": "x86_64",\n                "epoch": null,\n                "name": "kernel",\n                "release": "514.26.2.el7",\n                "source": "rpm",\n                "version": "3.10.0"\n              },\n              {\n                "arch": "x86_64",\n                "epoch": null,\n                "name": "kernel",\n                "release": "514.16.1.el7",\n                "source": "rpm",\n                "version": "3.10.0"\n              },\n              {\n                "arch": "x86_64",\n                "epoch": null,\n                "name": "kernel",\n                "release": "514.10.2.el7",\n                "source": "rpm",\n                "version": "3.10.0"\n              },\n              {\n                "arch": "x86_64",\n                "epoch": null,\n                "name": "kernel",\n                "release": "514.21.1.el7",\n                "source": "rpm",\n                "version": "3.10.0"\n              },\n              {\n                "arch": "x86_64",\n                "epoch": null,\n                "name": "kernel",\n                "release": "693.2.2.el7",\n                "source": "rpm",\n                "version": "3.10.0"\n              }\n            ],\n            "kernel-tools": [\n              {\n                "arch": "x86_64",\n                "epoch": null,\n                "name": "kernel-tools",\n                "release": "693.2.2.el7",\n                "source": "rpm",\n                "version": "3.10.0"\n              }\n            ],\n            "kernel-tools-libs": [\n              {\n                "arch": "x86_64",\n                "epoch": null,\n                "name": "kernel-tools-libs",\n                "release": "693.2.2.el7",\n                "source": "rpm",\n                "version": "3.10.0"\n              }\n            ],\n          }\n        }\n        # Sample deb\n        {\n          "packages": {\n            "libbz2-1.0": [\n              {\n                "version": "1.0.6-5",\n                "source": "apt",\n                "arch": "amd64",\n                "name": "libbz2-1.0"\n              }\n            ],\n            "patch": [\n              {\n                "version": "2.7.1-4ubuntu1",\n                "source": "apt",\n                "arch": "amd64",\n                "name": "patch"\n              }\n            ],\n          }\n        }\n'
        bool_0 = False
        list_0 = [str_0, str_0, str_0, bool_0]
        dict_0 = {str_0: bool_0}
        float_0 = 1.0
        inventory_manager_0 = module_0.InventoryManager(float_0)
        var_0 = inventory_manager_0.parse_sources(dict_0)
        inventory_manager_1 = module_0.InventoryManager(bool_0, list_0)
    except BaseException:
        pass

def test_case_13():
    try:
        float_0 = None
        str_0 = '\rWGc]t_!LDI\x0cb_n=\t9I'
        inventory_manager_0 = module_0.InventoryManager(str_0, str_0)
        inventory_manager_1 = module_0.InventoryManager(inventory_manager_0)
        var_0 = inventory_manager_1.refresh_inventory()
        dict_0 = {float_0: float_0, float_0: float_0, float_0: float_0, float_0: float_0}
        list_0 = [dict_0, float_0]
        bool_0 = True
        inventory_manager_2 = module_0.InventoryManager(bool_0, dict_0)
        var_1 = inventory_manager_2.reconcile_inventory()
        int_0 = 591
        inventory_manager_3 = module_0.InventoryManager(list_0)
        float_1 = -766.09
        set_0 = {float_1, int_0}
        str_1 = '\x0c~nQ'
        var_2 = inventory_manager_3.clear_pattern_cache()
        inventory_manager_4 = module_0.InventoryManager(str_1)
        var_3 = inventory_manager_4.subset(str_1)
        var_4 = inventory_manager_4.parse_source(set_0)
        var_5 = inventory_manager_4.list_hosts(inventory_manager_4)
        var_6 = inventory_manager_4.list_hosts()
        var_7 = inventory_manager_4.list_hosts()
        var_8 = inventory_manager_1.refresh_inventory()
        var_9 = inventory_manager_4.restrict_to_hosts(list_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = 'mV]43i,V!(+]}y}'
        dict_0 = {}
        var_0 = module_0.order_patterns(dict_0)
        set_0 = {str_0, str_0}
        dict_1 = {}
        inventory_manager_0 = module_0.InventoryManager(dict_1, set_0)
        var_1 = inventory_manager_0.reconcile_inventory()
        inventory_manager_1 = module_0.InventoryManager(str_0, set_0)
        var_2 = inventory_manager_1.get_hosts()
        var_3 = inventory_manager_1.subset(set_0)
        var_4 = inventory_manager_0.list_hosts()
        int_0 = 569
        var_5 = inventory_manager_1.restrict_to_hosts(int_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'mV]43i,V!(+]}y}'
        float_0 = 2603.7788824643394
        str_1 = "\x0c#<D8'%S)\rb%cT&[1,"
        inventory_manager_0 = module_0.InventoryManager(str_1)
        var_0 = inventory_manager_0.get_host(float_0)
        var_1 = inventory_manager_0.remove_restriction()
        set_0 = {str_0, str_0}
        var_2 = inventory_manager_0.list_hosts()
        dict_0 = {}
        inventory_manager_1 = module_0.InventoryManager(dict_0, set_0)
        var_3 = inventory_manager_1.remove_restriction()
        inventory_manager_2 = module_0.InventoryManager(str_0, set_0)
        tuple_0 = ()
        var_4 = inventory_manager_1.get_host(tuple_0)
        str_2 = '_>u1\x0b,\x0b@x@.\r*sZ]#2#'
        var_5 = inventory_manager_2.subset(set_0)
        var_6 = inventory_manager_1.list_hosts()
        int_0 = 569
        var_7 = inventory_manager_2.subset(dict_0)
        var_8 = inventory_manager_2.list_hosts(int_0)
        list_0 = []
        var_9 = inventory_manager_1.restrict_to_hosts(list_0)
        var_10 = inventory_manager_2.subset(str_2)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = 'mV]43i,V!(+]}y}'
        float_0 = 2603.7788824643394
        str_1 = "\x0c#<D8'%S)\rb%cT&[1,"
        inventory_manager_0 = module_0.InventoryManager(str_1)
        var_0 = inventory_manager_0.get_host(float_0)
        var_1 = inventory_manager_0.remove_restriction()
        dict_0 = {}
        var_2 = module_0.order_patterns(dict_0)
        set_0 = {str_0, str_0, var_0}
        var_3 = inventory_manager_0.list_hosts()
        dict_1 = {}
        inventory_manager_1 = module_0.InventoryManager(dict_1, set_0)
        var_4 = inventory_manager_1.remove_restriction()
        inventory_manager_2 = module_0.InventoryManager(str_0, set_0)
        tuple_0 = ()
        var_5 = inventory_manager_1.get_host(tuple_0)
        var_6 = inventory_manager_2.get_hosts()
        bool_0 = None
        int_0 = 67
        inventory_manager_3 = module_0.InventoryManager(int_0)
        var_7 = inventory_manager_3.parse_source(int_0)
        var_8 = inventory_manager_2.subset(set_0)
        inventory_manager_4 = module_0.InventoryManager(set_0)
        var_9 = inventory_manager_1.subset(set_0)
        var_10 = inventory_manager_1.list_hosts()
        bool_1 = None
        var_11 = inventory_manager_4.subset(float_0)
        list_0 = [bool_1, bool_0, str_0, inventory_manager_1]
        var_12 = inventory_manager_1.list_hosts(list_0)
        bool_2 = False
        var_13 = inventory_manager_0.restrict_to_hosts(bool_2)
    except BaseException:
        pass