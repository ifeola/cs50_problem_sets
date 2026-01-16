from final_project import is_name_valid, is_student_id_valid, is_new

def test_is_name_valid():
    assert is_name_valid("Arogunmasa Abayomi")
    assert is_name_valid("Olanrewaju Abayomi")
    assert is_name_valid("Ifeola Olumide")

def test_is_student_id_valid():
    assert is_student_id_valid("SS0001")
    assert is_student_id_valid("SS0100")
    assert is_student_id_valid("SS0198")

def test_is_new():
    assert is_new("SS0001") == False
    assert is_new("SS0002") == False
    assert is_new("SS0100") == True