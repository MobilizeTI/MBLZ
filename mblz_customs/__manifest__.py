# -*- coding: utf-8 -*-
{
    'name': "MBLZ: Customizaciones Generales",

    'summary': """
        1.- Relación del modulo de tickets con proyectos
        
        """,

    'description': """
    """,

    'website': "https://www.mobilize.cl",
    'category': 'Mobilize/Apps',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'project', 
        'helpdesk',
        'base',
        'contacts'
        ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/helpdesk_ticket.xml',
        'views/view_project.xml',
        'views/res_config_settings_views.xml',
        'views/res_partner_views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'license': 'LGPL-3',
}
