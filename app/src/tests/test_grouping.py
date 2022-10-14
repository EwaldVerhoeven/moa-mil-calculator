import pytest
from grouping import Group
from contextlib import nullcontext as does_not_raise


test_1 = [
            [-0.7, -0.5], [0.4, -0.7], [0.6, 0.09],
            [-0.1, 0.6], [0.4, -0.2], [-3.6, 3.9]
        ]
test_2 = [[0.1, 0.1], [0.3, -0.1]]
test_3 = []
testdata = [test_1, test_2, test_3]


@pytest.mark.parametrize('data', testdata)
def test_group_add_shot(data) -> None:
    '''coverage: test add_shot method'''
    group = Group(data)
    group.add_shot([0.0, 0.1])
    assert group.shots_in_group == len(data) + 1


@pytest.mark.parametrize('data', testdata)
def test_group_shots_in_group(data) -> None:
    '''coverage: test shots_in_group method'''
    group = Group(data)
    assert group.shots_in_group == len(data)


@pytest.mark.parametrize('data', testdata)
def test_group_str(data) -> None:
    '''coverage: test __str__ method'''
    group = Group(data)
    assert group.__str__() == f'{len(data)} shots in group: {group.shots}'


@pytest.mark.parametrize(
    'data, expectation',
    [
        [test_1, does_not_raise()],
        [test_2, pytest.raises(ValueError)],
        [test_3, pytest.raises(ValueError)]
    ]
)
def test_group_scrore_group(data, expectation) -> None:
    '''coverage: expection in score_group method'''
    group = Group(data)
    with expectation:
        assert group.score_group() is not None


@pytest.mark.parametrize('data', [test_1])
def test_group_get_modified_zscore(data) -> None:
    '''coverage: test get_modified_zscore method'''
    import numpy as np
    group = Group(data)
    x = np.array([i[0] for i in group.shots])
    assert group.get_modified_zscore(x) == [-1.6380714285714286,
                                            0.4817857142857143,
                                            0.8672142857142857,
                                            -0.4817857142857143,
                                            0.4817857142857143,
                                            -7.226785714285715
                                            ]


@pytest.mark.parametrize('data', [test_1])
def test_group_outliers(data) -> None:
    '''coverage: outliers property
    by call to get_modified_zscore'''
    group = Group(data)
    assert group.outliers == [5]


if __name__ == '__main__':
    pytest.main()
