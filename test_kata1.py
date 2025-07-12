from main import RomanNumberError, roman_to_int
import pytest


def test_prueba():
    assert 10 == 20

def prueba_2():
    assert 10 !=20  

def prueba_3():
    assert 4 < 5       

def test_romano_a_entero_no_repetir():
    with pytest.raises(RomanNumberError) as exceptionInfo:
        roman_to_int("IIII")
    assert str(exceptionInfo.value) == "No se puede repetir mas de tres veces"    



