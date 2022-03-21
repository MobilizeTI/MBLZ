# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'MBLZ Project',
    'version': '1.0',
    'category': 'project',
    'summary': 'MBLZ Project',
    'depends': ['project', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'security/project_security.xml',
        'views/tus_project_inherit_view.xml',
        'views/tus_project_project_inherit.xml',
    ],
    'installable': True,
    'application': True,
}
