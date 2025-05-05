from odoo import fields, models, _

class APICall(models.Model):    
    _name = 'api.call'
    _description = 'API call'
    _order = 'id desc'
    _check_company_auto = True

    action = fields.Char(string='Action', required=False, readonly=True)
    called_url = fields.Char(string='Called URL', required=False, readonly=True)
    headers = fields.Text(string='Headers', required=False, readonly=True)
    body = fields.Text(string='Body', required=False, readonly=True)
    params = fields.Text(string='Params', required=False, readonly=True)
    status_code = fields.Integer(string='Status code', required=False, readonly=True, help='')
    type = fields.Char(string='Type', required=False, readonly=True)   
    value = fields.Text(string='Value', required=False, readonly=True, help='')
    record_count = fields.Integer(string='Record count', required=False, readonly=True, help='')
    res_model = fields.Char(string='Resource model', required=False, readonly=True)
    res_id = fields.Integer(string='Resource ID', required=False, readonly=True)

    active = fields.Boolean(string='Active', required=True, readonly=True, default=True)
    company_id = fields.Many2one('res.company', 'Company', required=True, index=True, default=lambda self: self.env.company)

    def action_view_record(self):
        self.ensure_one()
        if not self.res_model or not self.res_id:
            return
        
        return {
            'name': _('API call record'),
            'type': 'ir.actions.act_window',
            'res_model': self.res_model,
            'view_mode': 'form',
            'res_id': self.res_id,
            'target': 'current',
        }

   