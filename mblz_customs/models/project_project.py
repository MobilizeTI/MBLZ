# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProjectProject(models.Model):
    _inherit = 'project.project'

    label_tickets = fields.Char(string='Use Tickets as', default='Tickets',
                                help="Label used for the tickets of the project.", translate=True)
    tickets_count = fields.Integer(compute='_compute_ticket_count', string="Tickets Count")

    def _compute_ticket_count(self):
        for project in self:
            project.tickets_count = project.env['helpdesk.ticket'].sudo().search_count(
                [('project_ids', 'in', [project.id])])

    def action_view_tickets(self):
        action = self.with_context(active_id=self.id, active_ids=self.ids) \
            .env.ref('mblz_customs.mblz_helpdesk_ticket_action_project') \
            .sudo().read()[0]
        action['display_name'] = self.name
        return action
