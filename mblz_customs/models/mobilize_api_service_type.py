from odoo import models, fields, api
from odoo.exceptions import UserError

class MobilizeServiceType(models.Model):
    _name = 'mobilize.api.service.type'
    _description = 'Tipo de Servicio Mobilize (API)'
    
    name = fields.Char('Name')
    # service_type_id = fields.Many2one('mobilize.api.service.type', string='Tipo de Servicio')
    
    # partner_id = fields.Many2one('res.partner', string='Partner')
    # # db_uuid = fields.Char('UUID')
    # active = fields.Boolean('Active', default=True)