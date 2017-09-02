import json


def df_to_dict(df):

    dict_ = {'columns': [],
             'indices': []}

    for column in df.columns:

        dict_['columns'].append({'name': str(column),
                                 'values': [str(val) for val in df[column]],
                                 'type': str(df.dtypes[column])})

    if df.index.nlevels == 1:
        dict_['indices'].append({'values': [str(val) for val in df.index],
                                 'type': str(df.index.dtype)})

    else:
        index_frame = df.index.as_frame()
        for index_name in index_frame.columns:
            dict_['indices'].append({'values': [str(val) for val in index_frame[index_name]],
                                     'type': index_frame.dtypes[index_name]})

    return dict_


def df_to_json(df):

    return json.dumps(df_to_dict(df))

