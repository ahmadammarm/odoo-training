from odoo import models, fields, api

class Propinsi(models.Model):
    _name           = "propinsi"
    _description    = "Referensi Propinsi"

    kode            = fields.Char(string='Kode', required=True)
    name            = fields.Char( required=True, string="Nama Propinsi",  help="")
    singkatan       = fields.Char( string="Singkatan",  help="")
    description     = fields.Text( string="Deskripsi",  help="")

    kota_ids        = fields.One2many(comodel_name="kota",  inverse_name="propinsi_id",  string="Kota",  help="")



class Kota(models.Model):
    _name           = "kota"
    _description    = "Referensi Kota"

    name            = fields.Char(required=True, string="Nama Kota",  help="")
    kode            = fields.Char(string='Kode', required=True)

    singkatan       = fields.Char( string="Singkatan",  help="")
    description     = fields.Text( string="Deskripsi",  help="")

    propinsi_id     = fields.Many2one(comodel_name="propinsi",  string="Propinsi",  help="")
    kecamatan_ids   = fields.One2many(comodel_name="kecamatan",  inverse_name="kota_id",  string="Kecamatan",  help="")

    
class Kecamatan(models.Model):
    _name           = "kecamatan"
    _description    = "Referensi Data Kecamatan"

    name            = fields.Char( required=True, string="Nama Kecamatan",  help="")
    kode            = fields.Char(string='Kode')
    
    description     = fields.Text( string="Deskripsi",  help="")

    kota_id         = fields.Many2one(comodel_name="kota",  string="Kota",  help="")
    desa_ids        = fields.One2many(comodel_name="desa",  inverse_name="kecamatan_id",  string="Desa/Kelurahan",  help="")

    

class Desa(models.Model):
    _name           = "desa"
    _description    = "Referensi Data Desa/Kelurahan"

    name            = fields.Char( required=True, string="Nama Desa/Kelurahan",  help="")
    kode            = fields.Char(string='Kode', required=True)
    
    description     = fields.Text( string="Description",  help="")
    kecamatan_id    = fields.Many2one(comodel_name="kecamatan",  string="Kecamatan",  help="")
