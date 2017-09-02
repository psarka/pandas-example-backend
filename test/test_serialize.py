import pandas as pd

from backend.serialize import df_to_dict


def test_simple():

    df = pd.DataFrame({'a': [1, 2],
                       'b': ['a', 'b']})

    expected = {'columns': [{'name': 'a',
                             'values': ['1', '2'],
                             'type': 'int64'},
                            {'name': 'b',
                             'values': ['a', 'b'],
                             'type': 'object'}],
                'indices': [{'values': ['0', '1'],
                             'type': 'int64'}]}

    assert df_to_dict(df) == expected


