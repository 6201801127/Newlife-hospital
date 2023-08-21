from odoo import fields, api, models, _ 

class HospitalRooms(models.Model):

    _name = "room.details"
    _description = "All room detials"


    room_no = fields.Char(string="Room No.")
    ref_code = fields.Char(string="Ref. Code")
    description = fields.Char(string="Description")
    

    