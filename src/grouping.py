import numpy as np
import numpy.typing as npt
from .config import MIN_DATAPOINTS_GROUP


class Group:

    def __init__(self, shots: list[list[float, float]] = None) -> None:
        self._min_datapoints = MIN_DATAPOINTS_GROUP
        self.shots = []
        if shots is None:
            self.shots = []
        else:
            for shot in shots:
                self.shots.append(shot)

    def add_shot(self, shot: list[float, float]) -> None:
        self.shots.append(shot)

    def score_group(self) -> None:  # TODO: finish implementation
        if self.shots_count > self._min_datapoints:
            return 0
        else:
            raise AssertionError(f'Your group is too small. Shoot at least {self._min_datapoints} times')

    @property
    def shots_count(self) -> None:
        return len(self.shots)

    def __str__(self) -> None:
        return f'{self.shots_count} shots in group: {self.shots}'

    def get_modified_zscore(self, data: npt.ArrayLike) -> list:
        '''
        formula: 0.6745*(x_data - median)/median_absolute_deviation
        threshold: -3.5/3.5
        '''
        median = np.median(data)
        abs_diff = abs(data-median)    
        median_abs_diff = np.median(abs_diff)
        return list(0.6745 * (data - median) / median_abs_diff)

    @property
    def outliers(self) -> list:
        '''functions returns index of outliers in original data list'''
        if self.shots_count < self._min_datapoints:
            raise ValueError(f'Group too small: must contain at least {self._min_datapoints} shots.')
        else:
            x, y = np.array([i[0] for i in self.shots]), np.array([i[1] for i in self.shots])

            zscores = [self.get_modified_zscore(x), self.get_modified_zscore(y)]

            outliers = [j for i in zscores for j in range(len(i)) if i[j] > 3.5 or i[j] < -3.5]

            return list(dict.fromkeys(outliers))


class Session:

    def __init__(self, groupings=list[Group]) -> None:
        if groupings is None:
            self.groupings = []
        else:
            for group in groupings:
                self.groupings.append(group)

    def add_group(self, group: Group) -> None:
        pass

    @property
    def groupings_count(self) -> None:
        pass
