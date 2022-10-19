from odoo import api, fields, models

class DuongCustom(models.Model):
    _name = "duong.custom"
    _description = "Duong custom"
    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male')
    note = fields.Text(string='Description')