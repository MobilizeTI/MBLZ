from odoo import fields, models

class ResConfigSettings(models.TransientModel):

    _inherit = 'res.config.settings'

    mblz_api_url = fields.Char('Mobilize Api URL', related='company_id.mblz_api_url', readonly=False)