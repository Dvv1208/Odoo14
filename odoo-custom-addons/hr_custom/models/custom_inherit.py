from odoo import api, fields, models

class CustomInherit(models.Model):
    _inherit = "hr.employee"
    
    project_custom = fields.Char(string='Project Custom' , tracking=True)
    references_job = fields.Many2one('project.custom', string="References")
    # create field employee level & select option from hr.employee.level
    level_id = fields.Many2one(comodel_name='hr.employee.level', store=True, string='Employee Level')
    # upload file employee
    cv_id = fields.Binary(string='Resumé' )
    file_name = fields.Char('File Name')
    