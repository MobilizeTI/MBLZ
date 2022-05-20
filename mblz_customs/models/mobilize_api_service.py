from odoo import models, fields, api
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)

class MobilizeApiService(models.Model):
    _name = 'mobilize.api.service'
    _description = 'Servicio Mobilize (API)'
    
    name = fields.Char('Name')
    service_type_id = fields.Many2one('mobilize.api.service.type', string='Tipo de Servicio')
    
    partner_id = fields.Many2one('res.partner', string='Partner')
    # db_uuid = fields.Char('UUID')
    api_active = fields.Boolean('Active', default=True)
    
    @api.onchange('api_active')
    def onchange_active(self):
        if not self.api_active:
            _logger.info(f'LOG: desactivar servicio de la api {self.partner_id.id}')
            partner_str = str(self.partner_id.id).replace('NewId_', '')
            partner_id_int = int(partner_str)
            partner_id = self.partner_id.browse(int(partner_str))
            _logger.info(f'LOG: --> partner_id a busacr {partner_id_int} partner_id {partner_id}')
            if partner_id:
                partner_id.api_sync(params={'deactivate_service_id': self.id})
            # self.partner_id.api_sync()
            # _logger.info(f'LOG: desactivar servicio de la api {self.partner_id}')
    