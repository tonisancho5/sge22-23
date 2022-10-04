# -*- coding: utf-8 -*-

from odoo import models, fields, api


class player(models.Model):
    _name = 'empires_of_legends.player'
    _description = 'Players'

    name = fields.Char(required =True)
    avatar = fields.Image(max_width = 200, max_height=200)

class territory(models.Model):
    _name = 'empires_of_legends.territory'
    _description = 'Territories'

    name = fields.Char(required = True)

class village(models.Model):
    _name = 'empires_of_legends.village'
    _description = 'Villages'

    name = fields.Char(required = True)



