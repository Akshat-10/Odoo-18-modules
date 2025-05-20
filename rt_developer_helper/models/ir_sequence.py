from odoo import models

class IrSequence(models.Model):
    _name = "ir.sequence"
    _inherit = ["ir.sequence", "rt.external.id.computer"]