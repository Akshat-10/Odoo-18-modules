from odoo import fields, models


class ExternalIDComputer(models.Model):
    _name = "rt.external.id.computer"
    _description = "External ID Computer"
    
    rt_xml_id = fields.Char('RT External ID', compute="_compute_rt_xml_id")

    def _compute_rt_xml_id(self):
        res = self.get_external_id()
        for rec in self:
            rec.rt_xml_id = res.get(rec.id)