def test_sum_double():
    assert sum_double(1, 2) == 3

def test_diff21():
    assert diff21(19) == 2

def test_near_hundred():
    assert near_hundred(93) == True

def test_pos_neg():
    assert pos_neg(1, -1, False) == True

def test_not_string():
    assert not_string("not bad") == "not bad"

def test_missing_char():
    assert missing_char("kitten", 1) == "ktten"

def test_front_back():
    assert front_back("code") == "eodc"

def test_front3():
    assert front3("Java") == "JavJavJav"

def test_string_times():
    assert string_times("Hi", 2) == "HiHi"

def test_front_times():
    assert front_times("Chocolate", 2) == "ChoCho"

def test_string_bits():
    assert string_bits("Hello") == "Hlo"

def test_string_splosion():
    assert string_splosion("Code") == "CCoCodCode"

def test_last2():
    assert last2("hixxhi") == 1

def test_array_count9():
    assert array_count9([1, 2, 9]) == 1

def test_array_front9():
    assert array_front9([1, 2, 9, 3, 4]) == True
