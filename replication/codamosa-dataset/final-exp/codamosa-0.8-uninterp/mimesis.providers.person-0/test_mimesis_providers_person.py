# Automatically generated by Pynguin.
import mimesis.providers.person as module_0
import mimesis.enums as module_1

def test_case_0():
    pass

def test_case_1():
    person_0 = module_0.Person()

def test_case_2():
    person_0 = module_0.Person()
    bytes_0 = b'\xd8\x0e\xab/\x85"\xb4\x04}L;/\xc5\x06=\xf8\x8f\xbb\xd1'
    str_0 = person_0.nationality(bytes_0)
    int_0 = person_0.age()
    gender_0 = None
    str_1 = person_0.surname(gender_0)

def test_case_3():
    person_0 = module_0.Person()
    int_0 = person_0.work_experience()
    str_0 = person_0.social_media_profile()
    str_1 = person_0.blood_type()
    str_2 = person_0.language()

def test_case_4():
    person_0 = module_0.Person()
    str_0 = person_0.name()

def test_case_5():
    person_0 = module_0.Person()
    str_0 = person_0.surname()

def test_case_6():
    person_0 = module_0.Person()
    str_0 = person_0.last_name()

def test_case_7():
    person_0 = module_0.Person()
    str_0 = person_0.height()
    gender_0 = None
    var_0 = person_0.first_name(gender_0)
    str_1 = person_0.blood_type()
    var_1 = person_0.first_name()
    person_1 = module_0.Person()
    str_2 = person_1.last_name()
    int_0 = person_0.weight()
    str_3 = person_0.email()
    person_2 = module_0.Person()
    str_4 = person_1.title()

def test_case_8():
    person_0 = module_0.Person()
    gender_0 = module_1.Gender.MALE
    bool_0 = False
    str_0 = person_0.full_name(gender_0, bool_0)
    str_1 = person_0.university()

def test_case_9():
    person_0 = module_0.Person()
    str_0 = person_0.social_media_profile()

def test_case_10():
    person_0 = module_0.Person()
    str_0 = person_0.social_media_profile()

def test_case_11():
    person_0 = module_0.Person()
    str_0 = person_0.name()
    bool_0 = False
    str_1 = person_0.password(bool_0)
    var_0 = person_0.sex()

def test_case_12():
    person_0 = module_0.Person()
    str_0 = person_0.email()

def test_case_13():
    list_0 = []
    person_0 = module_0.Person(*list_0)
    tuple_0 = ()
    person_1 = module_0.Person()
    int_0 = person_1.weight()
    str_0 = person_1.email(tuple_0)
    str_1 = person_1.occupation()
    str_2 = ''
    tuple_1 = (str_2,)
    str_3 = person_1.email(tuple_1)
    str_4 = person_1.occupation()
    var_0 = person_1.sex()
    str_5 = person_1.views_on()
    int_1 = person_1.work_experience()
    str_6 = person_1.avatar()
    str_7 = person_1.nationality()
    float_0 = 10.0
    str_8 = person_1.height(float_0, float_0)
    str_9 = person_1.full_name()
    str_10 = person_1.telephone()
    str_11 = person_1.worldview()
    str_12 = person_1.worldview()
    str_13 = person_0.height()

def test_case_14():
    person_0 = module_0.Person()
    var_0 = person_0.gender()

def test_case_15():
    list_0 = []
    person_0 = module_0.Person(*list_0)
    str_0 = person_0.height()
    person_1 = module_0.Person(*list_0)
    str_1 = person_1.social_media_profile()

def test_case_16():
    person_0 = module_0.Person()
    str_0 = person_0.blood_type()

def test_case_17():
    list_0 = []
    person_0 = module_0.Person(*list_0)
    str_0 = person_0.title()
    tuple_0 = ()
    int_0 = person_0.weight()
    str_1 = person_0.email(tuple_0)
    str_2 = person_0.occupation()
    str_3 = person_0.blood_type()
    str_4 = person_0.occupation()
    var_0 = person_0.sex()
    str_5 = person_0.sexual_orientation()
    str_6 = person_0.social_media_profile()
    bool_0 = True
    str_7 = person_0.email(tuple_0, bool_0)

def test_case_18():
    person_0 = module_0.Person()
    str_0 = person_0.full_name()
    str_1 = person_0.views_on()
    str_2 = person_0.last_name()
    str_3 = person_0.avatar()
    person_1 = module_0.Person()
    gender_0 = module_1.Gender.MALE
    str_4 = person_0.worldview()
    str_5 = person_1.academic_degree()
    str_6 = person_1.avatar()
    str_7 = 'asleep'
    var_0 = person_1.first_name()
    str_8 = person_0.full_name()
    float_0 = 1.5
    str_9 = person_1.height(float_0)
    dict_0 = {}
    person_2 = module_0.Person(**dict_0)
    str_10 = person_1.username()
    person_3 = module_0.Person()
    str_11 = person_3.identifier(str_7)
    str_12 = person_1.full_name(gender_0)

def test_case_19():
    person_0 = module_0.Person()
    str_0 = person_0.nationality()

def test_case_20():
    person_0 = module_0.Person()
    str_0 = person_0.university()

def test_case_21():
    person_0 = module_0.Person()
    str_0 = person_0.language()

def test_case_22():
    person_0 = module_0.Person()
    str_0 = person_0.nationality()
    none_type_0 = None
    bool_0 = True
    str_1 = person_0.email(none_type_0, bool_0)

def test_case_23():
    list_0 = []
    person_0 = module_0.Person(*list_0)
    str_0 = person_0.title()
    tuple_0 = ()
    int_0 = person_0.weight()
    str_1 = person_0.email(tuple_0)
    str_2 = person_0.views_on()
    str_3 = person_0.occupation()
    str_4 = person_0.blood_type()
    str_5 = person_0.occupation()
    str_6 = person_0.sexual_orientation()
    str_7 = person_0.social_media_profile()
    str_8 = person_0.views_on()
    int_1 = person_0.work_experience()
    str_9 = person_0.avatar()
    str_10 = person_0.nationality()
    str_11 = person_0.full_name()
    str_12 = person_0.nationality()
    str_13 = person_0.telephone()
    str_14 = person_0.worldview()
    float_0 = 1000.0
    list_1 = []
    social_network_0 = module_1.SocialNetwork.TWITTER
    int_2 = person_0.work_experience(int_1)
    tuple_1 = (str_13, list_1, social_network_0)
    bool_0 = True
    str_15 = person_0.email(tuple_1, bool_0)
    str_16 = person_0.height(float_0)

def test_case_24():
    bool_0 = True
    gender_0 = module_1.Gender.MALE
    bool_1 = True
    person_0 = module_0.Person()
    str_0 = person_0.full_name(gender_0, bool_1)
    person_1 = module_0.Person()
    str_1 = person_1.full_name()
    person_2 = module_0.Person()
    str_2 = '\\Zle" 8mw\t&enpdO?I.i'
    str_3 = person_2.views_on()
    var_0 = person_2.sex()
    str_4 = person_2.identifier(str_2)
    str_5 = person_2.blood_type()
    var_1 = person_2.sex()
    str_6 = person_2.name()
    str_7 = person_1.worldview()
    str_8 = person_2.worldview()
    person_3 = module_0.Person()
    str_9 = person_3.password(bool_0)
    str_10 = person_3.academic_degree()
    str_11 = person_3.surname()
    str_12 = person_1.university()
    person_4 = module_0.Person()
    str_13 = person_3.occupation()
    str_14 = person_3.avatar()

def test_case_25():
    list_0 = []
    person_0 = module_0.Person(*list_0)
    str_0 = person_0.title()
    tuple_0 = ()
    int_0 = person_0.weight()
    str_1 = person_0.email(tuple_0)
    str_2 = person_0.occupation()
    str_3 = person_0.blood_type()
    str_4 = person_0.occupation()
    var_0 = person_0.sex()
    str_5 = person_0.sexual_orientation()
    int_1 = person_0.work_experience()
    str_6 = person_0.avatar()
    str_7 = person_0.nationality()
    float_0 = 10.0
    str_8 = person_0.height(float_0, float_0)
    str_9 = person_0.full_name()
    str_10 = person_0.telephone()
    str_11 = 'hK!UigyT33\n2?Kh\n'
    str_12 = person_0.telephone(str_11)
    str_13 = person_0.worldview()
    str_14 = person_0.password()
    str_15 = person_0.political_views()
    person_1 = module_0.Person()
    str_16 = person_0.worldview()
    bool_0 = None
    bool_1 = True
    var_1 = person_1.gender(bool_0, bool_1)
    str_17 = person_0.height()