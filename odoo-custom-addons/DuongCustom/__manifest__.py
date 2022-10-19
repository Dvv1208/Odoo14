# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Duong Custom',
    'version': '1.1',
    'category': 'Human Resources/Employees',
    'sequence': -100,
    'summary': 'Centralize employee custom information',
    'description': "",
    'website': 'https://www.odoo.com/page/employees_custom',
    'images': [
        'images/hr_department.jpeg',
        'images/hr_employee.jpeg',
        'images/hr_job_position.jpeg',
        'static/src/img/default_image.png',
    ],
    'depends': [
        'base_setup',
        'mail',
        'resource',
        'web',
    ],
    'data': [
        
    ],
    'demo': [
        
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [
        
    ],
    'license': 'LGPL-3',
    
}
