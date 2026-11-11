import pytest
from finite_automata.validators import validate, pin_dfa

def test_pin():
    assert validate('pin','1234')
    assert not validate('pin','123')
    assert not validate('pin','12345')
    assert not validate('pin','12a4')

def test_password():
    assert validate('password','Example@123')
    assert not validate('password','example123')

def test_email_like():
    assert validate('email','student@example.com')
    assert not validate('email','studentexample.com')
    assert not validate('email','a@@b.com')
    assert not validate('email','a@b')

def test_unknown_kind():
    with pytest.raises(ValueError): validate('phone','123')

def test_dfa_rejects_unknown_symbol():
    assert not pin_dfa().accepts('12x4')
