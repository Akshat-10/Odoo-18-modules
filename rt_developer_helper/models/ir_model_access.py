from odoo import models

class IrModelAccess(models.Model):
    _name = "ir.model.access"
    _inherit = ["ir.model.access", "rt.external.id.computer"]
