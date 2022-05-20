from email.policy import default
from odoo import models, fields, api
from odoo.exceptions import UserError
import secrets
from ..utils.utils import Api

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    partner_token = fields.Char('Partner Token', help='Token to connect to mblz api interface')
    db_ids = fields.One2many('res.partner.db', 'partner_id', string='Partner Databases')
    mblz_services_ids = fields.One2many('mobilize.api.service', 'partner_id', string='Servicios Mobilize')
    sync_state = fields.Selection([('synchronized', 'Sincronizado'), ('draft', 'No Sincronizado')], string='Estado en Api', default='draft')
    
    def generate_token(self):
        for rec in self:
            rec.partner_token = secrets.token_urlsafe(22)
            
    def api_sync(self, params=False):
        for rec in self:
            if rec.partner_token:
                data = {
                    'message': 'Create Partner Info',
                    'partner_token': self.partner_token,
                    'partner_id': self.id,
                    'name': self.name,
                    # 'users': [user.slack_id for user in self.dev_team_employee_ids],
                    'endpoint': 'partner',
                    # 'jira_project_key': self.jira_project_id.jira_key,
                    'service_ids': [{
                        'name': ms.name,
                        'service_type_id': ms.service_type_id.id,
                        'active': ms.api_active if ms.id not in params.get('deactivate_service_id') else False,
                        'odoo_id': ms.id
                    } for ms in self.mblz_services_ids],
                    'db_ids': [{
                        'name': db.name,
                        'uuid': db.db_uuid,
                        'active': db.active
                    } for db in self.db_ids]
                }
                if Api.send_to_api(self, data):
                    rec.sync_state = 'synchronized'
            else:
                raise UserError('Must select a partner for token generation')