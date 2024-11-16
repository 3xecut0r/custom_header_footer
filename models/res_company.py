from odoo import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    header_image = fields.Binary('Header Image', readonly=False)
    footer_image = fields.Binary('Footer Image', readonly=False)