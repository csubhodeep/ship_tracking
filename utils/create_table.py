from lib.table_schema import metadata


def create_all_tables(engine):
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
