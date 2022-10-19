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
        
    ],
    'depends': [
        'hr'
    ],
    'data': [
        'views/custom.xml',
        'views/hr_custom.xml',
        'security/ir.model.access.csv'
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
