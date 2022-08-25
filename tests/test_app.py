from src.app import get_moa, get_mil, get_adjustments
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
    assert get_moa(-10, system='imperial', distance=100) == -10
    assert get_moa(-10, system='metric', distance=100) == -4.31

def test_get_moa_high():
    assert get_moa(5, system='imperial', distance=100) == 5
    assert get_moa(5, system='metric', distance=100) == 2.15

def test_get_moa_alt_distance():
    assert get_moa(5, system='imperial', distance=150) == 7.5
    assert get_moa(5, system='metric', distance=150) == 3.23

def test_get_mil_low():
    assert get_mil(-10, system='imperial', distance=100) == -2.78
    assert get_mil(-10, system='metric', distance=100) == -1.2

def test_get_mil_high():
    assert get_mil(5, system='imperial', distance=100) == 1.39
    assert get_mil(5, system='metric', distance=100) == 0.6

def test_get_mil_alt_distance():
    assert get_mil(5, system='imperial', distance=150) == 2.08
    assert get_mil(5, system='metric', distance=150) == 0.9

def test_get_adjustments_high():
    assert get_adjustments(5, 10, 'MOA', system='metric') == {'sight-type': 'MOA', 'x': 2.15, 'y': 4.31}
    assert get_adjustments(5, 10, 'MOA', system='imperial') == {'sight-type': 'MOA', 'x': 5.0, 'y': 10.0}
    assert get_adjustments(5, 10, 'MRAD', system='metric') == {'sight-type': 'MRAD', 'x': 0.6, 'y': 1.2}
    assert get_adjustments(5, 10, 'MRAD', system='imperial') == {'sight-type': 'MRAD', 'x': 1.39, 'y': 2.78}

def test_get_adjustments_low():
    assert get_adjustments(-5, -10, 'MOA', system='metric') == {'sight-type': 'MOA', 'x': -2.15, 'y': -4.31}
    assert get_adjustments(-5, -10, 'MOA', system='imperial') == {'sight-type': 'MOA', 'x': -5.0, 'y': -10.0}
    assert get_adjustments(-5, -10, 'MRAD', system='metric') == {'sight-type': 'MRAD', 'x': -0.6, 'y': -1.2}
    assert get_adjustments(-5, -10, 'MRAD', system='imperial') == {'sight-type': 'MRAD', 'x': -1.39, 'y': -2.78}