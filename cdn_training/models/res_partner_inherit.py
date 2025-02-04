from odoo import models, fields, api, _

class ResPartner(models.Model):
    _inherit        = "res.partner"

    propinsi_id     = fields.Many2one(comodel_name="propinsi",  string="Propinsi")
    kota_id         = fields.Many2one(comodel_name="kota",  string="Kota")
    kecamatan_id    = fields.Many2one(comodel_name="kecamatan",  string="Kecamatan")
    desa_id         = fields.Many2one(comodel_name="desa",  string="Desa/Kelurahan")
    jenis_kelamin   = fields.Selection(selection=[('laki-laki', 'Laki-Laki'), ('perempuan', 'Perempuan')], string="Jenis Kelamin")
