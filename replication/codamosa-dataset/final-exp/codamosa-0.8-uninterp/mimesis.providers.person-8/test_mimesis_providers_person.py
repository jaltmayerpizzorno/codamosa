# Automatically generated by Pynguin.
import mimesis.providers.person as module_0
import mimesis.enums as module_1

def test_case_0():
    pass

def test_case_1():
    person_0 = module_0.Person()

def test_case_2():
    person_0 = module_0.Person()
    str_0 = person_0.full_name()

def test_case_3():
    person_0 = module_0.Person()
    str_0 = person_0.surname()

def test_case_4():
    person_0 = module_0.Person()
    str_0 = person_0.last_name()

def test_case_5():
    person_0 = module_0.Person()
    int_0 = person_0.age()
    person_1 = module_0.Person()
    str_0 = person_0.height()
    str_1 = person_1.full_name()
    str_2 = person_0.height()
    str_3 = person_1.identifier()
    int_1 = person_1.work_experience()
    gender_0 = module_1.Gender.MALE
    str_4 = person_0.name(gender_0)
    str_5 = person_0.title()
    int_2 = person_0.weight()
    var_0 = person_0.gender()
    str_6 = person_0.avatar()

def test_case_6():
    person_0 = module_0.Person()
    str_0 = person_0.social_media_profile()

def test_case_7():
    person_0 = module_0.Person()
    str_0 = person_0.social_media_profile()

def test_case_8():
    person_0 = module_0.Person()
    str_0 = person_0.social_media_profile()

def test_case_9():
    list_0 = []
    person_0 = module_0.Person(*list_0)
    str_0 = person_0.university()
    float_0 = -3721.0
    str_1 = person_0.password()
    person_1 = module_0.Person()
    str_2 = person_1.height(float_0, float_0)
    str_3 = person_0.social_media_profile()
    str_4 = person_1.username()
    str_5 = person_0.academic_degree()
    str_6 = person_1.language()

def test_case_10():
    person_0 = module_0.Person()
    str_0 = person_0.last_name()

def test_case_11():
    person_0 = module_0.Person()
    str_0 = ',W:( (ZT)FA'
    bool_0 = True
    str_1 = person_0.email(str_0, bool_0)

def test_case_12():
    person_0 = module_0.Person()
    var_0 = person_0.gender()

def test_case_13():
    person_0 = module_0.Person()
    str_0 = ',W:( (ZT)FA'
    bool_0 = True
    str_1 = person_0.email(str_0, bool_0)
    str_2 = person_0.height()

def test_case_14():
    person_0 = module_0.Person()
    str_0 = person_0.social_media_profile()
    int_0 = person_0.weight()

def test_case_15():
    person_0 = module_0.Person()
    str_0 = person_0.surname()
    str_1 = person_0.last_name()
    var_0 = person_0.first_name()
    var_1 = person_0.gender()
    var_2 = person_0.gender()
    var_3 = person_0.sex()
    str_2 = person_0.height()
    str_3 = person_0.telephone(str_1)
    str_4 = person_0.worldview()
    int_0 = person_0.age()
    str_5 = person_0.blood_type()
    str_6 = person_0.nationality()

def test_case_16():
    person_0 = module_0.Person()
    str_0 = person_0.occupation()
    int_0 = person_0.weight()
    bool_0 = True
    var_0 = person_0.gender(bool_0, bool_0)
    str_1 = person_0.last_name()

def test_case_17():
    list_0 = []
    person_0 = module_0.Person(*list_0)
    var_0 = person_0.sex()
    str_0 = person_0.name()
    person_1 = module_0.Person()
    str_1 = person_0.political_views()
    str_2 = person_1.identifier()
    bool_0 = True
    var_1 = person_1.gender(bool_0)
    str_3 = person_1.full_name()
    str_4 = person_1.academic_degree()
    var_2 = person_0.sex()

def test_case_18():
    person_0 = module_0.Person()
    str_0 = person_0.social_media_profile()
    str_1 = person_0.views_on()

def test_case_19():
    person_0 = module_0.Person()
    str_0 = person_0.nationality()

def test_case_20():
    person_0 = module_0.Person()
    str_0 = person_0.social_media_profile()

def test_case_21():
    dict_0 = {}
    person_0 = module_0.Person(**dict_0)
    int_0 = 33
    gender_0 = module_1.Gender.FEMALE
    person_1 = module_0.Person()
    str_0 = person_1.last_name(gender_0)
    str_1 = person_0.surname(int_0)
    str_2 = person_0.views_on()
    str_3 = person_0.height()
    bool_0 = False
    str_4 = person_0.email(bool_0)
    str_5 = person_0.email()
    person_2 = module_0.Person(**dict_0)
    str_6 = person_2.occupation()
    str_7 = person_0.nationality()
    str_8 = person_0.language()
    str_9 = person_0.surname()
    str_10 = person_0.avatar(int_0)
    str_11 = person_0.language()
    str_12 = person_1.surname(gender_0)
    str_13 = person_1.avatar()
    person_3 = module_0.Person()
    var_0 = person_3.sex()
    str_14 = None
    str_15 = person_3.telephone(str_14)
    str_16 = person_2.identifier(str_15)
    str_17 = person_0.political_views()
    bool_1 = True
    str_18 = person_0.full_name(gender_0, bool_1)