from odoo import models

class IrModel(models.Model):
    _name = "ir.model"
    _inherit = ["ir.model", "rt.external.id.computer"]