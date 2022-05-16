from db import base
from peewee import (
	CharField, 
	IntegerField
)
class FilmModel(base.BaseModel):
	order = IntegerField()
	value = CharField(max_length=50)
	title = CharField(max_length=50)

