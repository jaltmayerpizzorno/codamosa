# Automatically generated by Pynguin.
import mimesis.schema as module_0
import builtins as module_1

def test_case_0():
    abstract_field_0 = module_0.AbstractField()

def test_case_1():
    bytearray_0 = module_1.bytearray()
    abstract_field_0 = module_0.AbstractField(bytearray_0, bytearray_0)
    var_0 = abstract_field_0.__str__()

def test_case_2():
    abstract_field_0 = module_0.AbstractField()
    schema_0 = module_0.Schema(abstract_field_0)
    int_0 = -1490
    list_0 = schema_0.create(int_0)
    list_1 = schema_0.create(int_0)