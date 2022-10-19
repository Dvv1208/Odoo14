
from odoo import api, fields, models

class DuongCustom(models.Model):
    
    _inherit = "hr.employee"
    

    # name = fields.Char(string='Name', required=True)
    # age = fields.Integer(string='Age')
    # gender = fields.Selection([
    #     ('male', 'Male'),
    #     ('female', 'Female'),
    #     ('other', 'Other'),
    # ], required=True, default='male')
    DuongCustom = fields.Text(string='Description')

