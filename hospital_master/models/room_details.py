from odoo import fields, api, models, _ 

class HospitalRooms(models.Model):

    _name = "room.details"
    _description = "All room detials"
    _rec_name = "room_no"

    room_no = fields.Char(string="Room No.")
    ref_code = fields.Char(string="Ref. Code")
    bed_ids = fields.Many2many(comodel_name="bed.details", relationsheep="room_bed_rel",class1="room_id",class2="bed_id", string="Bed")
    description = fields.Char(string="Description")


    