from models.user import User
from mimesis import Person, Datetime
import random
from werkzeug.security import generate_password_hash


def run():
    person = Person('en')
    date = Datetime()
    professions = ['Nutritionalist', 'Dietician',
                   'Personal Trainer', 'Weight Trainer', 'Coach']

    for _ in range(10):
        User.create(
            full_name=person.full_name(),
            username=person.username(),
            email=person.email(),
            phone_number=person.telephone(),
            date_of_birth=date.date(start=1980, end=2000),
            password=generate_password_hash('admin12345'),
            profession=random.choice(professions))
