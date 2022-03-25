# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    project_ids = fields.Many2many(
        comodel_name='project.project',
        check_company=True,
        string='Projects')
