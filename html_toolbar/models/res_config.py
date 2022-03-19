# -*- coding: utf-8 -*-
#################################################################################
# Author      : Acespritech Solutions Pvt. Ltd. (<www.acespritech.com>)
# Copyright(c): 2012-Present Acespritech Solutions Pvt. Ltd.
# All Rights Reserved.
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#################################################################################

from odoo import models, fields, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    is_tinymce = fields.Boolean(string="Enable HTML Editor")

    def get_values(self):
        res = super(ResConfigSettings, self).get_values()

        # res.update(
        #     is_tinymce=self.env['ir.config_parameter'].sudo().get_param(
        #         'html_toolbar.is_tinymce'),
        # )
        self.env['ir.config_parameter'].sudo().set_param('html_toolbar.is_tinymce',
                                                         True)
        return res

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('html_toolbar.is_tinymce',
                                                         self.is_tinymce)



class Partner(models.Model):
    _inherit = 'res.partner'

    test = fields.Html(string="test")




# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: