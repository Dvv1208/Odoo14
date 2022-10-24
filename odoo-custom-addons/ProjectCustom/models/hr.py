from odoo import api, fields, models

class HrCustom(models.Model):
    
    _inherit = "hr.employee"
    
    project_custom = fields.Char(string='Project Custom' , tracking=True)
    references_job = fields.Many2one('project.custom', string="References")