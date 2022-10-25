from odoo import api, fields, models

class ProjectCustom(models.Model):
    _name = "project.custom"
    _description = "Project custom"
    _order = 'name'

    name = fields.Char(string='Name', required=True)
    age = fields.Char(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='')
    note = fields.Text(string='Description')