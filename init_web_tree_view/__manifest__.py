# -*- coding: utf-8 -*-
{
    'name': 'Hierarchy Tree View',
    'version': '15.0.1.0.5',
    'category': 'Extra Tools',
    'summary': 'Hierarchy Tree View',
    'author': 'Init Co. Ltd',
    'description': """Hierarchy Tree View""",
    'depends': [
        'web',
        'project'
    ],
    'data': [
        'views/project_task.xml',
    ],
    'qweb': [],
    'demo': [],
    'test': [],
    'assets': {
        'web.assets_backend': [
            'init_web_tree_view/static/src/scss/tree_view.scss',
            'init_web_tree_view/static/src/js/tree_controller.js',
            'init_web_tree_view/static/src/js/tree_model.js',
            'init_web_tree_view/static/src/js/tree_renderer.js',
            'init_web_tree_view/static/src/js/tree_view.js',
        ],
        'web.assets_qweb': [
            'init_web_tree_view/static/src/xml/web_tree_view.xml',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': True,
}
