from measurement.measures import Distance

async def get_mil(delta: float, system: str, distance: int) -> float:
    #BASE_RULE: 1 mil == 3.6 inch (on 100 yards)
    BASE_RULE_DIST = 100
    BASE_RULE_DEVI = 3.6

    if system == 'imperial':
        diff_factor = distance / BASE_RULE_DIST
        return round(delta / BASE_RULE_DEVI * diff_factor, 2)
    else: 
        delta = Distance(centimeter=delta)
        distance = Distance(meter=distance)

        diff_factor = distance.yd / BASE_RULE_DIST
        return round(delta.inch / BASE_RULE_DEVI * diff_factor, 2)

async def get_moa(delta: float, system: str, distance: int) -> float:
    # BASE_RULE: 1 moa == 1 inch (on 100 yards)
    BASE_RULE_DIST = 100
    BASE_RULE_DEVI = 1
    if system == 'imperial':
        diff_factor = distance / BASE_RULE_DIST
        return round(delta / BASE_RULE_DEVI* diff_factor, 2)
    else: 
        delta = Distance(centimeter=delta)
        distance = Distance(meter=distance)

        diff_factor = distance.yd / BASE_RULE_DIST
        return round(delta.inch /BASE_RULE_DEVI * diff_factor, 2)

async def get_adjustments(x_deviation: float, y_deviation: float, output: str, distance: int = 100, system='metric') -> dict:
    if system != 'metric' and system != 'imperial':
        raise ValueError("system has to be either 'metric' or 'imperial'")

    if output == 'MOA':
        x = await get_moa(x_deviation, system, distance)
        y = await get_moa(y_deviation, system, distance)
    elif output == 'MRAD':
        x = await get_mil(x_deviation, system, distance)
        y = await get_mil(y_deviation, system, distance)
    else:
        raise ValueError("Output must be either 'MOA' or 'MRAD'")

    return {'sight-type':output, 'x':x, 'y':y}