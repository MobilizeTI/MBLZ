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
    'depends': ['project', 'helpdesk'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/helpdesk_ticket.xml',
        'views/view_project.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
