from src.app import get_moa, get_mil
from hypothesis import given, strategies as st

# @given(
#     delta=st.floats(min_value=-25, max_value=25),
#     system=st.sampled_from(options.SYSTEM)
#     )
# def test_get_moa(delta, system):
#     print(f'delta={delta}, system={system}')
#     result = get_moa(delta, system)
#     print('test1')
#     assert type(result) == float

def test_get_moa_low():
    assert get_moa(-10, system='imperial') == -10
    assert get_moa(-10, system='metric') == -4.31

def test_get_moa_high():
    assert get_moa(5, system='imperial') == 5
    assert get_moa(5, system='metric') == 2.15

def test_get_moa_alt_distance():
    assert get_moa(5, system='imperial', distance=150) == 7.5
    assert get_moa(5, system='metric', distance=150) == 3.23

def test_get_mil_low():
    assert get_mil(-10, system='imperial') == -2.78
    assert get_mil(-10, system='metric') == -1.2

def test_get_mil_high():
    assert get_mil(5, system='imperial') == 1.39
    assert get_mil(5, system='metric') == 0.6

def test_get_mil_alt_distance():
    assert get_mil(5, system='imperial', distance=150) == 2.08
    assert get_mil(5, system='metric', distance=150) == 0.9