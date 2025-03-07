from full_name import add, fullName, multiple


def test_normal_case():
    assert fullName("John", "Doe") == "My Full Name is John Doe"


def test_empty_strings():
    assert fullName("", "") == "My Full Name is  "


def test_numbers_as_strings():
    assert fullName("123", "456") == "My Full Name is 123 456"


def test_special_characters():
    assert fullName("@John", "#Doe") == "My Full Name is @John #Doe"


def test_add_numbers():
    assert add(1, 2) == 3


def test_mul_numbers():
    assert multiple(2, 2) == 4