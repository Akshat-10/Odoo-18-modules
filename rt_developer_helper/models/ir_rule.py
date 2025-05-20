from odoo import models

class IrRule(models.Model):
    _name = "ir.rule"
    _inherit = ["ir.rule", "rt.external.id.computer"]