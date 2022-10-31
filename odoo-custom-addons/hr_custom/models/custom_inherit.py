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

    # create datetime for employee
    created_on = fields.Datetime(string = "Created on", required=True)
    
    # insert field for company technology
    joining_day = fields.Datetime(string = "Joining Day")
    project = fields.Char(string = "Project")
    program = fields.Char(string = "Program")
    year_of_experience = fields.Char(string = "Years of Exeperience")
    before_company = fields.Char(string = "Before Company")
    year_at_company = fields.Char(string = "Years at Company")

    # insert field for contact information
    current_address = fields.Char(string = "Current Address")
    permanent_address = fields.Char(string = "Permanent Address")
    private_email = fields.Char(string = "Private Email")
    personal_phone = fields.Char(string = "Personal Phone")
    skype = fields.Char(string = "Skype")

    # insert field for bank information
    bank_account = fields.Char(string = "Bank Account")
    number = fields.Char(string = "Number")
    bank_name = fields.Char(string = "Bank Name")
    bank_branch = fields.Char(string = "Bank Branch")
    bank_location = fields.Char(string = "Bank Location")

    #insert field for citizenship
    identification_issue_date = fields.Date(string = "Identification Issue Date")
    identification_issued = fields.Char(string = "Identification Issued By Police Department Of")
    passport_expired_date = fields.Date(string = "Passport Expired Date")
    sin_no = fields.Char(string = "SIN No")
    pit_code = fields.Char(string = "PIT code")


    #insert field for vehicle
    vehicle_number = fields.Char(string = "Vehicle Number")
    vehicle_type = fields.Char(string = "Vehicle Type")