from odoo import api, fields, models

class CustomInherit(models.Model):
    _inherit = "hr.employee"
    
    project_custom = fields.Char(string='Project Custom' , tracking=True)
    references_job = fields.Many2one('project.custom', string="References")
    level_id = fields.Many2one('employee.level', store=True, string='Level')