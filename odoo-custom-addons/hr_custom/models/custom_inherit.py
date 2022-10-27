from odoo import api, fields, models

class CustomInherit(models.Model):
    _inherit = "hr.employee"
    
    project_custom = fields.Char(string='Project Custom' , tracking=True)
    references_job = fields.Many2one('project.custom', string="References")

    # create field employee level & select option from hr.employee.level
    level_id = fields.Many2one(comodel_name='hr.employee.level', store=True, string='Employee Level')
    
    # upload file employee
    cv_id = fields.Binary(string='Resumé')
    file_name = fields.Char('File Name')

    # priority for employee
    priority = fields.Selection([
        ('0', 'Normal'), ('1', 'Good'),
        ('2', 'Verygood'), ('3', 'Excellent')],
        'Appreciation', required=True, default='1')

    #create date for employee
    created_on = fields.Datetime(string = "Created on", required=True)
    