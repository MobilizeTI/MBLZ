from odoo import models, fields, api
from odoo.exceptions import UserError

class ResPartnerDb(models.Model):
    _name = 'res.partner.db'
    _description = 'Partner Databases'
    
    name = fields.Char('Name')
    partner_id = fields.Many2one('res.partner', string='Partner')
    db_uuid = fields.Char('UUID')
    active = fields.Boolean('Active', default=True)