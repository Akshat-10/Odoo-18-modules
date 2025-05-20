from odoo import models

class Groups(models.Model):
    _name = "res.groups"
    _inherit = ["res.groups", "rt.external.id.computer"]