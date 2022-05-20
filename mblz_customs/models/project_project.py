# -*- coding: utf-8 -*-

from odoo import models, fields, api
import secrets
from odoo.exceptions import UserError
from ..utils.utils import Api

import logging
_logger = logging.getLogger(__name__)


class ProjectProject(models.Model):
    _inherit = 'project.project'

    label_tickets = fields.Char(string='Use Tickets as', default='Tickets',
                                help="Label used for the tickets of the project.", translate=True)
    tickets_count = fields.Integer(compute='_compute_ticket_count', string="Tickets Count")
    
    # mblz_api_info_id = fields.Many2one('mblz.api.info', strong='Información Api')
    
    active_in_api = fields.Boolean('Activo')
    api_token = fields.Char('Token')
    
    def generate_token(self):
        for rec in self:
            if self.partner_id:
                rec.partner_token = secrets.token_urlsafe(22)
                data = {
                    'message': 'Create Partner Info',
                    'partner_token': self.partner_id.partner_token,
                    'partner_id': self.partner_id.id,
                    'name': self.partner_id.name,
                    'users': [user.slack_id for user in self.dev_team_employee_ids],
                    'endpoint': 'partner',
                    'jira_project_key': self.jira_project_id.jira_key,
                    'db_ids': [{
                        'name': db.name,
                        'uuid': db.db_uuid,
                        'active': db.active
                    } for db in self.db_ids]
                }
                Api.send_to_api(self, data)
            else:
                raise UserError('Must select a partner for token generation')

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
