# Automatically generated by Pynguin.
import ansible.modules.pip as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'f'
    package_0 = module_0.Package(str_0)

def test_case_2():
    str_0 = 'Eyaw/QS'
    package_0 = module_0.Package(str_0)

def test_case_3():
    str_0 = 'pathist'
    package_0 = module_0.Package(str_0)
    var_0 = package_0.__str__()
    package_1 = module_0.Package(str_0, str_0)
    var_1 = module_0.main()

def test_case_4():
    str_0 = 'Eyaw/QS'
    package_0 = module_0.Package(str_0)
    int_0 = 255
    var_0 = package_0.is_satisfied_by(int_0)

def test_case_5():
    str_0 = 'patlist'
    package_0 = module_0.Package(str_0)
    var_0 = package_0.is_satisfied_by(str_0)
    float_0 = -1482.4454623641
    str_1 = '__main__'
    package_1 = module_0.Package(str_1)
    var_1 = package_1.is_satisfied_by(float_0)
    str_2 = ' v8"M<'
    dict_0 = {}
    package_2 = module_0.Package(dict_0)
    var_2 = package_2.is_satisfied_by(str_2)
    var_3 = package_2.__str__()

def test_case_6():
    str_0 = 'pathist'
    package_0 = module_0.Package(str_0)
    var_0 = package_0.__str__()
    var_1 = module_0.main()

def test_case_7():
    var_0 = module_0.main()

def test_case_8():
    str_0 = 'setuptools'
    str_1 = 'setuptools==1.2.3'
    package_0 = module_0.Package(str_1)
    var_0 = package_0.package_name
    package_1 = module_0.Package(str_0)
    var_1 = package_1.has_version_specifier
    package_2 = module_0.Package(str_1)
    var_2 = package_2.has_version_specifier
    package_3 = module_0.Package(str_0)
    str_2 = '1.2.3'
    package_4 = module_0.Package(str_1)
    var_3 = package_4.is_satisfied_by(str_2)
    str_3 = '==1.2.3'
    package_5 = module_0.Package(str_0, str_3)
    var_4 = package_5.is_satisfied_by(str_2)
    package_6 = module_0.Package(str_0)
    str_4 = '1.2.4'
    var_5 = package_6.is_satisfied_by(str_4)

def test_case_9():
    str_0 = 'setupo[ls'
    package_0 = module_0.Package(str_0)
    var_0 = package_0.package_name
    package_1 = module_0.Package(str_0)
    package_2 = module_0.Package(str_0)
    var_1 = package_2.has_version_specifier
    package_3 = module_0.Package(str_0)
    var_2 = package_3.has_version_specifier
    package_4 = module_0.Package(str_0)
    str_1 = '1.2.3'
    bool_0 = False
    var_3 = package_4.is_satisfied_by(bool_0)
    var_4 = package_4.is_satisfied_by(str_1)
    package_5 = module_0.Package(str_1)
    var_5 = package_5.is_satisfied_by(str_1)
    bytes_0 = None
    list_0 = [bytes_0, bytes_0, str_0]
    var_6 = package_3.is_satisfied_by(list_0)
    int_0 = -1816
    var_7 = module_0.main()
    var_8 = package_3.is_satisfied_by(int_0)