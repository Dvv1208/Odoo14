from odoo import fields, models, api

class LevelModel(models.Model):
    _name = 'employee.level'

    lv_empl = fields.Char(string="Level")
    