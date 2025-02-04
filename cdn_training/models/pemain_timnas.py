from odoo import models, fields, api

class PemainTimnas(models.Model):
    _name = 'pemain_timnas'
    _description = 'Pemain Timnas'
    _sql_constraints = [
        ('name_uniq', 'unique(nama)', 'Nama pemain sudah ada!'),
        ('nomor_punggung_uniq', 'unique(nomor_punggung)', 'Nomor punggung sudah ada!')
    ]
    
    nama = fields.Char(string='Nama', required=True)
    klub = fields.Char(string='Klub', required=True)
    nomor_punggung = fields.Integer(string='Nomor Punggung', required=True)
    id_posisi = fields.Many2one(comodel_name='posisi', string='Posisi')


class Posisi(models.Model):
    _name = 'posisi'
    _description = 'Posisi'
    
    nama = fields.Char(string='Posisi', required=True)
    

