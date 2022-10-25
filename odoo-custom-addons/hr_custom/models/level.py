from odoo import api, fields, models
#create field
class LevelModel(models.Model):
    _name = 'hr.employee.level'

    name = fields.Char(string="Level")

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Level already exists !"),
    ]
    