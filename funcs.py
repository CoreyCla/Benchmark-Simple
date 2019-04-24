# Don't forget to add any new functions to your funcs dict in user_input.py


# 1
def row_by_len(test_data):
    rows = []
    for row in test_data.iterrows():
        rows.append(len(row))
    return rows


# 2
def row_by_char(test_data):
    rows = []
    for row in test_data.iterrows():
        rows.append(row[0])
    return rows
