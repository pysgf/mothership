from mongoalchemy.session import Session
from mongoalchemy.document import Document, Index, DocumentField
from mongoalchemy.fields import *

# Subclasses of Document both provide the mapping needed for
# queries as well as the classes for loading/saving objects.
class User(Document):
    config_collection_name = 'users'

    # Setting the possible values by using fields
    first_name = StringField()
    last_name = StringField()
    age = IntField(min_value=0, required=False)

    # db_field allows a different DB field name than the one on the
    # python object
    email = StringField(db_field='email_address')
    bio = StringField(max_length=1000, required=False)

    # A computed field decorator allows values
    @computed_field(SetField(StringField()), deps=[bio])
    def keywords(obj):
        return set(obj.get('bio','').split(' '))

    kw_index = Index().ascending('keywords')
    name_index = Index().descending('first_name').ascending('last_name')
    email_index = Index().descending('email').unique()

    def __eq__(self, other):
        return self.email == other.email

    def __repr__(self):
        return 'User(email="%s")' % self.email

session = Session.connect('mothership')
session.clear_collection(User)
