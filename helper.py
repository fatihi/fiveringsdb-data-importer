def create_comma_separated_string(lst):
    return ", ".join(lst)


def create_update_on_conflict_statement(columns):
    replace_statements = []
    for column in columns:
        replace_statements.append(column + " = excluded." + column)

    return create_comma_separated_string(replace_statements)
