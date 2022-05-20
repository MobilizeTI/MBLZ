# -*- coding: utf-8 -*-

from odoo import models, fields, api
import secrets
from odoo.exceptions import UserError
from ..utils.utils import Api

import logging
_logger = logging.getLogger(__name__)


class MblzApiInfo(models.Model):
    _name = 'mblz.api.info'
    _description = 'Conexión a Api Mobilize'
    
    active = fields.Boolean('Activo')
    token = fields.Char('Token')
    
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
