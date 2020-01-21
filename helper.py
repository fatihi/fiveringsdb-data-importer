def create_comma_separated_string(lst):
    return ", ".join(lst)


def create_update_on_conflict_statement(columns):
    replace_statements = []
    for column in columns:
        replace_statements.append(column + " = excluded." + column)

    return create_comma_separated_string(replace_statements)


def transform_string(s):
    return s.replace("'", "''")


def get_nullable_string_value(entry, field):
    return 'NULL' if entry[field] is None else "\'" + transform_string(entry[field]) + "\'"


def get_nullable_number_value(entry, field):
    return 'NULL' if entry[field] is None else str(entry[field])
