def create_comma_separated_string(lst):
    return ", ".join(lst)


def create_update_on_conflict_statement(columns):
    replace_statements = []
    for column in columns:
        replace_statements.append(column + " = excluded." + column)

    return create_comma_separated_string(replace_statements)


def transform_string(s):
    return s.replace("'", "''")


def get_nullable_value(entry, field):
    result = 'NULL'
    if (field in entry) and (entry[field] is not None):
        value = entry[field]
        if type(value) is int or type(value) is bool:
            result = str(entry[field])
        else:
            result = "\'" + transform_string(entry[field]) + "\'"
    return result
