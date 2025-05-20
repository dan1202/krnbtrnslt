import pytest
from src.run import get_flag


def test_flag_known_russian():
    assert get_flag('grey_zone') == '🇷🇺'


def test_flag_known_ukrainian():
    assert get_flag('ukraina_novosti') == '🇺🇦'


def test_flag_unknown_user():
    # Should return neutral flag and not raise any errors
    assert get_flag('some_unknown_user') == '🏳️'

