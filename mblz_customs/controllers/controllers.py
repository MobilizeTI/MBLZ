# -*- coding: utf-8 -*-
# from odoo import http


# class MblzCustoms(http.Controller):
#     @http.route('/mblz_customs/mblz_customs/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mblz_customs/mblz_customs/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mblz_customs.listing', {
#             'root': '/mblz_customs/mblz_customs',
#             'objects': http.request.env['mblz_customs.mblz_customs'].search([]),
#         })

#     @http.route('/mblz_customs/mblz_customs/objects/<model("mblz_customs.mblz_customs"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mblz_customs.object', {
#             'object': obj
#         })
