
def catch_columns(columns, frame):
    list_column = []
    dict_columns = {}
    for column in columns:
        for tecs in frame[column]:
            for tec in tecs:
                list_column.append(tec)
        dict_columns[column] = np.array(list(set(list_column)))
    import ipdb; ipdb.set_trace()
    return dict_columns
