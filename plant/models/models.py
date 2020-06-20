# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class custom/plant(models.Model):
#     _name = 'custom/plant.custom/plant'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class Plants(models.Model):
    _name='nurse.plant'

    name=fields.Char("Plant Name",required=True)
    price=fields.Float("Price")
    customer= fields.Many2one('res.company')
    email=fields.Char("Customer Email")
    state = fields.Selection(
        string='state',
        selection=[('draft', 'Draft'), ('confirm', 'confirm'),('cancel','Cancel')]
    , default='draft')

    changes=fields.Datetime(readonly=True)
    
#     result=fields.Float(compute="_calc_sum",store=True)
# @api.depends('price')
# def _calc_sum(self):
#     self.result= self.price * 100

class Customer(models.Model):
    _name='nurse.customer'

    name=fields.Char("Customer Name",required=True)
    email=fields.Char(help="To receive newsletter")
    company=fields.Many2one('res.company', string="company clients")

# class VendorsClass(models.Model):
#     _name = 'vendor.class'
#     _inhert = 'res.company'

#     vendor_x=fields.Char()


