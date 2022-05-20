# -*- coding: utf-8 -*-
from tkinter import S


{
    'name': "Customización en pedidos de compra (Prueba)",


    'description': """
        BOTON DE CONSULTA AGREGADO AL FORMULARIO DE PEDIDO DE COMPRA
    """,

    'author': "Christopher García gutierrez.cg33@gmail.com",

    'category': 'purchase',
    'version': '14.0.1',

    'depends': [
        'purchase',
        'stock' # TODO
        ],

    # always loaded
    'data': [
        'views/purchase_order.xml',
    ],
    # only loaded in demonstration mode
#     'demo': [
#         'demo/demo.xml',
#     ],
}
