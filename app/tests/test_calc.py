from app.calc import calc_moa, calc_mil, get_adjustments
import pytest


@pytest.mark.asyncio()
async def test_calc_moa_low() -> None:
    assert await calc_moa(-10, system='imperial', distance=100) == -9.55
    assert await calc_moa(-10, system='metric', distance=100) == -3.44


@pytest.mark.asyncio()
async def test_calc_moa_high() -> None:
    assert await calc_moa(5, system='imperial', distance=100) == 4.78
    assert await calc_moa(5, system='metric', distance=100) == 1.72


@pytest.mark.asyncio()
async def test_calc_moa_alt_distance() -> None:
    assert await calc_moa(5, system='imperial', distance=150) == 3.18
    assert await calc_moa(5, system='metric', distance=150) == 1.15


@pytest.mark.asyncio()
async def test_calc_mil_low() -> None:
    assert await calc_mil(-10, system='imperial', distance=100) == -2.78
    assert await calc_mil(-10, system='metric', distance=100) == -1.0


@pytest.mark.asyncio()
async def test_calc_mil_high() -> None:
    assert await calc_mil(5, system='imperial', distance=100) == 1.39
    assert await calc_mil(5, system='metric', distance=100) == 0.5


@pytest.mark.asyncio()
async def test_calc_mil_alt_distance() -> None:
    assert await calc_mil(5, system='imperial', distance=150) == 0.93
    assert await calc_mil(5, system='metric', distance=150) == 0.33


@pytest.mark.asyncio()
async def test_get_adjustments_high() -> None:
    assert await get_adjustments(5, 10, 'MOA', system='metric') == {'sight-type': 'MOA', 'x': 1.72, 'y': 3.44}
    assert await get_adjustments(5, 10, 'MOA', system='imperial') == {'sight-type': 'MOA', 'x': 4.78, 'y': 9.55}
    assert await get_adjustments(5, 10, 'MRAD', system='metric') == {'sight-type': 'MRAD', 'x': 0.5, 'y': 1.0}
    assert await get_adjustments(5, 10, 'MRAD', system='imperial') == {'sight-type': 'MRAD', 'x': 1.39, 'y': 2.78}


@pytest.mark.asyncio()
async def test_get_adjustments_low() -> None:
    assert await get_adjustments(-5, -10, 'MOA', system='metric') == {'sight-type': 'MOA', 'x': -1.72, 'y': -3.44}
    assert await get_adjustments(-5, -10, 'MOA', system='imperial') == {'sight-type': 'MOA', 'x': -4.78, 'y': -9.55}
    assert await get_adjustments(-5, -10, 'MRAD', system='metric') == {'sight-type': 'MRAD', 'x': -0.5, 'y': -1.0}
    assert await get_adjustments(-5, -10, 'MRAD', system='imperial') == {'sight-type': 'MRAD', 'x': -1.39, 'y': -2.78}
