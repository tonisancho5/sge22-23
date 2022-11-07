# -*- coding: utf-8 -*-

from email.policy import default
from odoo import models, fields, api


class player(models.Model):
    _name = 'empires_of_legends.player'
    _description = 'Players'

    name = fields.Char(required=True, default="Player Name")
    password = fields.Char()
    avatar = fields.Image(max_width=200, max_height=200)
    villages = fields.One2many('empires_of_legends.village', 'player')


class territory(models.Model):
    _name = 'empires_of_legends.territory'
    _description = 'Territories'

    name = fields.Char(required=True)
    villages = fields.One2many('empires_of_legends.village', 'territory')
    resourceSites = fields.One2many('empires_of_legends.resource_site', 'territory')
    
    
class village(models.Model):
    _name = 'empires_of_legends.village'
    _description = 'Villages'

    name = fields.Char(required=True)
    civilization = fields.Selection([('1', 'Bizantinos'), ('2', 'Britanos'), ('3', 'Celtas'),
                                     ('4', 'Chinos'), ('5', 'Francos'), ('6', 'Godos'), ('7', 'Japoneses')])
    food = fields.Integer(string='Total comida')
    wood = fields.Integer(string='Total')
    stone = fields.Integer(string='Total')
    iron = fields.Integer(string='Total')
    gold = fields.Integer(string='Total')  # de pago
    infantry_qty = fields.Integer(string='Total')
    archery_qty = fields.Integer(string='Total')
    cavalry_qty = fields.Integer(string='Total')
    siege_qty = fields.Integer(string='Total')
    troops_qty = fields.Integer(string='Total')
    attack_power = fields.Integer(string='Total')

    player = fields.Many2one('empires_of_legends.player')
    territory = fields.Many2one('empires_of_legends.territory',ondelete="cascade")
    buildings = fields.One2many('empires_of_legends.building', 'village', ondelete="restrict")
    

class resource_site(models.Model):
    _name = 'empires_of_legends.resource_site'
    _description = 'Resource Sites'

    name = fields.Char(required=True, default="Resource Site")
    resourceType = fields.Selection([('1', 'Food'), ('2', 'Wood'), ('3', 'Stone'), ('4', 'Iron')])
    territory = fields.Many2one('empires_of_legends.territory')


class building(models.Model):
    _name = 'empires_of_legends.building'
    _description = 'Building'

    name = fields.Char()

    produce_food = fields.Float(related='type.produce_food')
    produce_wood = fields.Float(related='type.produce_wood')
    produce_stone = fields.Float(related='type.produce_stone')
    produce_iron = fields.Float(related='type.produce_iron')

    consume_food = fields.Float(related='type.consume_food')
    consume_wood = fields.Float(related='type.consume_wood')
    consume_stone = fields.Float(related='type.consume_stone')
    consume_iron = fields.Float(related='type.consume_iron')

    train_infantry = fields.Integer(related='type.train_infantry')
    train_cavalry = fields.Integer(related='type.train_cavalry')
    train_archery = fields.Integer(related='type.train_archery')
    train_siege = fields.Integer(related='type.train_siege')

    type = fields.Many2one('empires_of_legends.building_type')
    village = fields.Many2one('empires_of_legends.village')


class building_type(models.Model):
    _name = 'empires_of_legends.building_type'
    _description = 'Building Types'

    name = fields.Char()

    produce_food = fields.Float()
    produce_wood = fields.Float()
    produce_stone = fields.Float()
    produce_iron = fields.Float()

    consume_food = fields.Float()
    consume_wood = fields.Float()
    consume_stone = fields.Float()
    consume_iron = fields.Float()

    train_infantry = fields.Integer()
    train_cavalry = fields.Integer()
    train_archery = fields.Integer()
    train_siege = fields.Integer()
