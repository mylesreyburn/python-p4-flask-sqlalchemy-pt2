#!/usr/bin/env python3

from random import choice as rc

from faker import Faker

fake = Faker()

from app import app
from models import db, Owner, Pet

with app.app_context():

    Pet.query.delete()
    Owner.query.delete()

    owners = []
    for n in range(50):
        owner = Owner(name = fake.name())
        owners.append(owner)

    db.session.add_all(owners)
    db.session.commit()

    pets = []
    species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']
    for n in range(100):
        pet = Pet(name = fake.name(), species = rc(species), owner = rc(owners))
        pets.append(pet)

    db.session.add_all(pets)
    db.session.commit()