#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class """

    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id', ondelete="CASCADE"),
                      nullable=False)
    places = relationship("Place", backref="cities",
                          cascade="all, delete",
                          passive_deletes=True)
