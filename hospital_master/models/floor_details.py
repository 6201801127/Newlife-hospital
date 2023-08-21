from odoo import models, fields, api, _ 


class FloorDetails(models.Model):

    _name = "floor.details"
    _description = "Hospital floor details"
    _rec_name = "floor_name"

    floor_name = fields.Char(string="Floor Name")
    ref_code = fields.Char(string="Ref. Code")
    rooms_ids = fields.Many2many(comodel_name="room.details",relationsheep="floor_rel", class1="floor_id",class2="room_id",string=
                                "Rooms")
    floor_description = fields.Char(string="Description")