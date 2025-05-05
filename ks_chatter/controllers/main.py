# -*- coding: utf-8 -*-
from odoo.http import request, route, _logger

from odoo import http, _


class KsChatter(http.Controller):
    @route(['/get/partner/models'], type='json', auth='user')
    def ks_get_partner_models(self, model, id):
        model_obj = request.env['ir.model'].sudo()
        model_name = []
        display_name = []
        result = {}
        current_user = request.env.user
        access = request.env['ir.rule'].search([])
        current_model_obj = request.env[model].sudo()
        record = request.env[model].sudo().browse(id)
        current_model = model_obj.sudo().search([('model', '=', model)])
        if 'partner_id' in current_model_obj._fields and current_model_obj.search([('partner_id', '=', record.partner_id.id)]) and model_obj.search([('model', '=', current_model_obj._name)]).is_mail_activity and model_obj.search([('model', '=', current_model_obj._name)]).is_mail_thread:
            current_model_obj += current_model_obj.search([('partner_id', '=', record.partner_id.id)])
            partner_models = model_obj.sudo().search(
                [('field_id.name', '=', 'partner_id'), ('field_id.name', '=', 'message_ids')])
            for model_id in partner_models:
                if model_id.model == 'calendar.event':
                    print("Yes")
                try:
                    record_exist = request.env[model_id.model].sudo().search(
                        [('partner_id', '=', record.partner_id.id)])
                    if record_exist and record_exist.partner_id and model_id.is_mail_thread and model_id.is_mail_activity:
                        model_name_tuple = (model_id.model, model_id.name)
                        model_name.append(model_name_tuple)
                        display_name.append(model_id.name)
                        result.update({model_id.model: list(zip(record_exist.mapped('display_name'), record_exist.mapped('id')))})
                except:
                    continue

            partner_model = model_obj.sudo().search([('model', '=', 'res.partner')])
            record_exist = request.env[partner_model.model].sudo().search(
                [('id', '=', record.partner_id.id)])
            if record_exist and partner_model.is_mail_thread and partner_model.is_mail_activity:
                model_name_tuple = (partner_model.model, partner_model.name)
                model_name.append(model_name_tuple)
                display_name.append(partner_model.name)
                result.update({partner_model.model: list(zip(record_exist.mapped('name'), record_exist.mapped('id')))})

            result.update({'models': model_name, 'current_model': current_model.model, 'current_record': [record.name,record.id] if 'name' in record else [record.display_name, record.id],
                           'current_model_records': list(zip(current_model_obj.mapped('name'), current_model_obj.mapped('id'))) if 'name' in current_model_obj else  list(zip(current_model_obj.mapped('display_name'), current_model_obj.mapped('id'))), 'display_name': display_name})

        if record._name == 'res.partner' and record.name:
            model_name_tuple = (current_model.model, current_model.name)
            model_name.append(model_name_tuple)
            display_name.append(current_model.name)
            result.update({current_model.model: list(zip(record.mapped('name'), record.mapped('id')))})
            current_model_obj += current_model_obj.search([('id', '=', record.id)])
            partner_models = model_obj.sudo().search(
                [('field_id.name', '=', 'partner_id'), ('field_id.name', '=', 'message_ids')])
            for model_id in partner_models:
                try:
                    record_exist = request.env[model_id.model].sudo().search(
                        [('partner_id', '=', record.id)])
                    if record_exist and model_id.is_mail_thread and model_id.is_mail_activity:
                        model_name_tuple = (model_id.model, model_id.name)
                        model_name.append(model_name_tuple)
                        display_name.append(model_id.name)
                        field_to_map = 'name' if 'name' in record_exist else 'display_name'
                        result.update({model_id.model: list(zip(record_exist.mapped(field_to_map), record_exist.mapped('id')))})
                except:
                    continue

            result.update({'models': model_name, 'current_model': current_model.model, 'current_record': [record.name,record.id],
                           'current_model_records': list(zip(current_model_obj.mapped('name'), current_model_obj.mapped('id'))), 'display_name': display_name})

        return result

    @route(['/get/model/record'], type='json', auth='user')
    def ks_get_model_records(self, model, name, id):
        if not id and not model == 'res.partner':
            id = int(name[1]) if name[1] else False
        model = model.split(',')
        model_obj = request.env[model[0]].sudo()
        if id:
            record = model_obj.browse(id)
        else:
            if 'res.partner' in model:
                record = model_obj.search([('name', '=', name)], limit=1)
            else:
                record = model_obj.search([('display_name', '=', name)], limit=1)
        return {'id': record.id, 'name': record.display_name}

    @route(['/get/record'], type='json', auth='user')
    def ks_get_records(self, model, name):
        name = int(name.split(',')[1])
        model_obj = request.env[model].sudo()
        if 'name' in model_obj._fields:
            record = model_obj.search([('id', '=', name)], limit=1)
        else:
            record = model_obj.search([('id', '=', name)], limit=1)
        return {'id': record.id, 'name': record.display_name}
