from odoo import api, fields, models

class HrCustom(models.Model):
    
    _inherit = "hr.employee"
    
    hr_custom = fields.Char(string='Dương Custom')