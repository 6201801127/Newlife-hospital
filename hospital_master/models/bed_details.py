from odoo import models, fields, api, _ 


class BedDetails(models.Model):

    _name = "bed.details"
    _description = "All bed details of nelife hospital"


    bed_no = fields.Char(string="Bed No.")
    ref_code = fields.Char(string="Ref Code")
    description = fields.Char(string="Description")