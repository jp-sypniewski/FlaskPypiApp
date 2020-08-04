import mongoengine


def global_init(db_name='pypi'):
    mongoengine.register_connection('core', name=db_name)
