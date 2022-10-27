# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Hr Custom',
    'version': '1.1',
    'category': 'Human Resources/Employees',
    'sequence': -100,
    'summary': 'Centralize employee custom information',
    'description': "",
    'website': 'https://www.odoo.com/page/employees_custom',
    'images': [
        
    ],
    'depends': [
        'hr',
        'base_setup',
    ],
    'data': [
        'views/custom.xml',
        'views/hr_custom_form_views.xml',
        'security/ir.model.access.csv',
        'views/custom_level.xml',
        'views/hr_custom_kanban_views.xml',
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
