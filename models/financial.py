from wtforms import *

from config import db

import json
import random
import string

class Financial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    name = db.Column(db.String(100))

    def __init__(self, year=0,name=''):
        self.year = year
        self.name = name

    def jsonify(self):
        return json.dumps({'id':self.id,'year':self.year,
                           'name':self.name,'size':self.size})

    @staticmethod
    def all():
        return Financial.query.all()

    @staticmethod
    def get(fileID):
        return Financial.query.get(fileID)

    @staticmethod
    def get_year(year):
        return Financial.query.filter_by(year=year).one()

class FinancialForm(Form):
    statement = FileField('Financial Statement',default='')
