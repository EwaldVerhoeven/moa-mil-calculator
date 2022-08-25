from measurement.measures import Distance
# distance = Distance(yd=100)
# print(distance)

def get_mil(delta, system='metric', distance=100):
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

print(get_mil(5, system='imperial', distance=150))
print(get_mil(5, system='metric', distance=150))
# print(get_mil(3.6, 100, system='imperial'))


def get_moa(delta, system='metric', distance=100):
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

# print(get_moa(5, distance=150))

def get_zero_adjustments(x_deviation: float, y_deviation: float, output: str, distance: int = 100, system='metric'):
    if system != 'metric' and system != 'imperial':
        raise ValueError("system has to be either 'metric' or 'imperial'")

    if output == 'MOA':
        x = get_moa(x_deviation, distance, system)
        y = get_moa(y_deviation, distance, system)
    elif output == 'MRAD':
        x = get_mil(x_deviation, distance, system)
        y = get_mil(y_deviation, distance, system)
    else:
        raise ValueError("Output must be either 'MOA' or 'MRAD'")

    return {'sight-type':output, 'x':x, 'y':y}