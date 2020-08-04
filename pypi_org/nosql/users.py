import datetime
import mongoengine


class User(mongoengine.Document):
    name = mongoengine.StringField()
    email = mongoengine.StringField(unique=True)  # index=True
    hashed_password = mongoengine.StringField()  # index=True
    created_date = mongoengine.DateTimeField(default=datetime.datetime.now)  # index=True

    meta = {
        'collection': 'users',
        'db_alias': 'core',
        'indexes': [
            'email,'
            'hashed_password',
            'created_date'
        ]
    }