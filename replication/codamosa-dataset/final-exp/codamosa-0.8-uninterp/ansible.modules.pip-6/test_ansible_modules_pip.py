# Automatically generated by Pynguin.
import ansible.modules.pip as module_0

def test_case_0():
    pass

def test_case_1():
    int_0 = -4562
    str_0 = '\r_'
    str_1 = 'UNc:'
    package_0 = module_0.Package(str_0, str_1)
    var_0 = package_0.is_satisfied_by(int_0)

def test_case_2():
    str_0 = 'Msslart'
    package_0 = module_0.Package(str_0)

def test_case_3():
    str_0 = 'sslcacert'
    package_0 = module_0.Package(str_0)
    var_0 = package_0.__str__()

def test_case_4():
    str_0 = 'sslcacert'
    package_0 = module_0.Package(str_0)
    str_1 = 'ansible.modules.pip'
    var_0 = package_0.is_satisfied_by(str_1)
    var_1 = package_0.__str__()
    var_2 = module_0.main()
    var_3 = package_0.canonicalize_name(package_0)

def test_case_5():
    str_0 = 'pkg'
    package_0 = module_0.Package(str_0)
    var_0 = package_0.package_name
    str_1 = '1.0'
    package_1 = module_0.Package(str_0, str_1)
    var_1 = package_1.package_name
    package_2 = module_0.Package(str_0, str_1)
    var_2 = package_2.has_version_specifier
    package_3 = module_0.Package(str_0, str_1)
    var_3 = module_0.main()
    var_4 = module_0.main()

def test_case_6():
    str_0 = 'pkg'
    package_0 = module_0.Package(str_0)
    var_0 = package_0.package_name
    str_1 = '\n2\ns\x0b[}\tXC4Dm_\n.('
    package_1 = module_0.Package(str_0, str_1)
    var_1 = package_1.package_name
    package_2 = module_0.Package(str_0, str_1)
    var_2 = package_2.has_version_specifier
    package_3 = module_0.Package(str_0, str_1)
    str_2 = '1.1'
    var_3 = package_3.is_satisfied_by(str_2)
    package_4 = module_0.Package(str_0, str_1)
    var_4 = package_4.is_satisfied_by(str_1)
    str_3 = '>=1.0'
    package_5 = module_0.Package(str_0, str_3)
    str_4 = '5\n{r'
    package_6 = module_0.Package(str_4)
    set_0 = {package_3}
    var_5 = package_3.is_satisfied_by(set_0)

def test_case_7():
    str_0 = 'slacert'
    package_0 = module_0.Package(str_0)
    var_0 = package_0.__str__()
    str_1 = 'distribute'
    package_1 = module_0.Package(str_1)