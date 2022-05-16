from peewee import *
db = PostgresqlDatabase('my_projects', 
	user = 'muhamadamin',
	password = '11',
	host = 'localhost',
	port = 5432
)
class BaseModel(Model):
	class Meta:
		database = db