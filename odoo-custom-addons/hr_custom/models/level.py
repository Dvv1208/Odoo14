from odoo import api, fields, models
#create model level, add name model =  hr.employee.level
class LevelModel(models.Model):
    _name = 'hr.employee.level'
    #create field for level with id = name
    name = fields.Char(string="Level")
    #sql constraints for level
    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Level already exists !"),
    ]
    