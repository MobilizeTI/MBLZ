from odoo import fields, models
from odoo.exceptions import UserError
from odoo.tools.translate import _

class ResCompany(models.Model):
    _inherit = 'res.company'

    mblz_api_url = fields.Char('Mobilize Api URL', readonly=False)