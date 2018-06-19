# -*- coding: utf-8 -*-
from odoo import fields, models, api, exceptions

class CustomerPO(models.Model):
    _inherit = 'sale.order'

    client_order_ref =  fields.Char(string='Customer PO');

    @api.constrains('client_order_ref')
    def _check_duplicates(self):
        duplicate = self.env['sale.order'].search([
            ('client_order_ref','=', self.client_order_ref),
            ('partner_id.name','=', self.partner_id.name),
            ('name', '!=', self.name)
        ])
        if str(duplicate.id) != 'False':
            raise exceptions.ValidationError("This Purchase Order reference already exists for this customer. Sale Order ->  " +
                str(duplicate.name))
        duplicate = self.env['sale.order'].search([
            ('client_order_ref','=', self.client_order_ref),
            ('name', '!=', self.name)
        ])
        if str(duplicate.id) != 'False':
            raise exceptions.ValidationError("This Purchase Order reference already exists. customer -> "+
                str(duplicate.partner_id.name) +" ; Sale Order ->  " +
                str(duplicate.name))


        # WORKS TOO >>>>
        # duplicate = self.env['sale.order'].browse([('user_id.name','=', self.user_id.name)])
        # if self.client_order_ref == self.client_order_ref:
        #     raise exceptions.ValidationError("Customer already belongs to  ")
