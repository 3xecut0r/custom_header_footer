from odoo import fields, models


class BaseDocumentLayout(models.TransientModel):
    _inherit = 'base.document.layout'

    header_image = fields.Binary(related='company_id.header_image', readonly=False)
    footer_image = fields.Binary(related='company_id.footer_image', readonly=False)
