from models import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///cats.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def create_cat(name):
    cat_object = Cat(name=name)
    session.add(cat_object)
    session.commit()

def get_cat(id):
	cat=session.query(Cat).filter_by(id=id).one()
	return cat

def get_all_cats():
    cats = session.query(Cat).all()
    return cats