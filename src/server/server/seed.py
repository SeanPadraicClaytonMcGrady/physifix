from .models import Diagnostic, Region, User
from django.contrib.auth.hashers import make_password

def seed_data():
    #Password for all test users.
    hashed_password = make_password('12345')

    #test users
    john = User.objects.create(
        username='john',
        email='john@john.com',
        password=hashed_password,
        bookmarks=[],
    )

    jane = User.objects.create(
        username='jane',
        email='jane@jane.com',
        password=hashed_password,
        bookmarks=[],
    )


    lower_back_region = Region.objects.create(name='Lower Back')

    diagnostic_load_intolerance = Diagnostic.objects.create(
        name='Load Intolerance',
        video='https://youtu.be/PV4pUmkbXzc?si=HkBi6HWHJm7mOOch&t=35',
        description='This test assesses your exposure to pain under spinal load.'
        region=lower_back_region
    )

    jane.bookmarks.add(diagnostic_load_intolerance)


seed_data()