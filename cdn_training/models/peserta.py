# from odoo import models, fields, api

# class Peserta(models.Model):
#     _name = 'peserta'
#     _description = 'Tabel Peserta'
#     _inherits =  {
#         "res.partner" : "partner_id"
#     }
    
#     partner_id = fields.Many2one(comodel="res.partner", string="Partner", required=True, ondelete="cascade")
#     pendidikan = fields.Selection(string='Pendidikan', selection=[('sd', 'SD'), ('smp', 'SMP'), ('sma', 'SMA'), ('d3', 'D3'), ('s1', 'S1'), ('s2', 'S2'), ('s3', 'S3')], required=True)
#     pekerjaan = fields.Char(string='Pekerjaan', required=True)
#     is_menikah = fields.Boolean(string='Menikah')
#     nama_pasangan = fields.Char(string='Nama Pasangan')
#     hp_pasangan = fields.Char(string='HP Pasangan')