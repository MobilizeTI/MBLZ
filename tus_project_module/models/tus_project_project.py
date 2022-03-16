# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class Project(models.Model):
    _inherit = 'project.project'

    email_id = fields.Char(string="Email Id")
    website = fields.Char(string="Website")
