from measurement.measures import Distance
import asyncio

async def calc_mil(delta: float, system: str, distance: int) -> float:
    #BASE_RULE: 1 mil == 3.6 inch (on 100 yards)
    BASE_RULE_DIST = 100
    BASE_RULE_DEVI = 3.6

    if system == 'imperial':
        diff_factor = BASE_RULE_DIST / distance
        return round(delta / BASE_RULE_DEVI * diff_factor, 2)
    else: 
        delta = Distance(centimeter=delta)
        distance = Distance(meter=distance)

        diff_factor = BASE_RULE_DIST / distance.yd
        return round(delta.inch / BASE_RULE_DEVI * diff_factor, 2)

async def calc_moa(delta: float, system: str, distance: int) -> float:
    # BASE_RULE: 1 moa == 1 inch (on 100 yards)
    BASE_RULE_DIST = 100
    BASE_RULE_DEVI = 1
    if system == 'imperial':
        diff_factor = BASE_RULE_DIST / distance
        return round(delta / BASE_RULE_DEVI* diff_factor, 2)
    else: 
        delta = Distance(centimeter=delta)
        distance = Distance(meter=distance)

        diff_factor = BASE_RULE_DIST / distance.yd
        return round(delta.inch /BASE_RULE_DEVI * diff_factor, 2)

async def get_adjustments(x_deviation: float, y_deviation: float, output: str, distance: int = 100, system='metric') -> dict:
    if system != 'metric' and system != 'imperial':
        raise ValueError("system has to be either 'metric' or 'imperial'")

    if output == 'MOA':
        x = await calc_moa(x_deviation, system, distance)
        y = await calc_moa(y_deviation, system, distance)
    elif output == 'MRAD':
        x = await calc_mil(x_deviation, system, distance)
        y = await calc_mil(y_deviation, system, distance)
    else:
        raise ValueError("Output must be either 'MOA' or 'MRAD'")

    print({'sight-type':output, 'x':x, 'y':y})
    return {'sight-type':output, 'x':x, 'y':y}

asyncio.run(get_adjustments(-5, -10, 'MOA', system='metric'))
asyncio.run(get_adjustments(-5, -10, 'MOA', system='imperial'))
asyncio.run(get_adjustments(-5, -10, 'MRAD', system='metric'))
asyncio.run(get_adjustments(-5, -10, 'MRAD', system='imperial'))