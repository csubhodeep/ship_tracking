from lib.table_schema import metadata


def create_all_tables(engine) -> bool:
    """This function creates-or-replaces all tables in the DB
    :param engine: the SQLAlchemy._engine.Engine object used to connect to the DB
    :return: a boolean flag denoting success/failure while creating tables
    """
    try:
        for table in metadata.sorted_tables:
            if table.exists(bind=engine):
                table.drop(bind=engine)
            table.create(bind=engine,
                         checkfirst=False)
    except Exception as ex:
        print(ex)
        return False

    return True
