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
    
    
class village(models.Model):
    _name = 'empires_of_legends.village'
    _description = 'Villages'

    name = fields.Char(required=True)
    civilization = fields.Selection([('1', 'Bizantinos'), ('2', 'Britanos'), ('3', 'Celtas'),
                                     ('4', 'Chinos'), ('5', 'Francos'), ('6', 'Godos'), ('7', 'Japoneses')])
    food = fields.Integer(string='Total comida')
    wood = fields.Integer(string='Total madera')
    stone = fields.Integer(string='Total piedra')
    iron = fields.Integer(string='Total hierro')
    gold = fields.Integer(string='Total oro')  # de pago
    infantry_qty = fields.Integer(string='Total caballeros')
    archery_qty = fields.Integer(string='Total arqueros')
    cavalry_qty = fields.Integer(string='Total jinetes')
    siege_qty = fields.Integer(string='Total asedio')
    troops_qty = fields.Integer(string='Total ejercito')
    attack_power = fields.Integer(string='Total poder')

    player = fields.Many2one('empires_of_legends.player')
    territory = fields.Many2one('empires_of_legends.territory',ondelete="cascade")
    buildings = fields.One2many('empires_of_legends.building', 'village', ondelete="restrict")
    

class building(models.Model):
    _name = 'empires_of_legends.building'
    _description = 'Building'

    name = fields.Char()
    avatar = fields.Image(related='type.avatar')

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

    def produce(self):
        for building in self:
            village = building.village
            food = village.food + building.produce_food
            wood = village.wood + building.produce_wood
            stone = village.stone + building.produce_stone
            iron = village.iron + building.produce_iron
            
            
    def train(self):
        for building in self:
            village = building.village
            food = village.food - building.consume_food
            wood = village.wood - building.consume_wood
            stone = village.stone - building.consume_stone
            iron = village.iron - building.consume_iron
            infantry_qty = village.infantry_qty + building.train_infantry
            archery_qty = village.archery_qty + building.train_cavalry
            cavalry_qty = village.cavalry_qty + building.train_archery
            siege_qty = village.siege_qty + building.train_siege


class building_type(models.Model):
    _name = 'empires_of_legends.building_type'
    _description = 'Building Types'

    name = fields.Char()
    avatar = fields.Image(max_width=200, max_height=200)

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
