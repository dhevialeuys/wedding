from odoo import api, fields, models


class KursiTamu(models.Model):
    _name = 'wedding.kursitamu'
    _description = 'Data Tentang Kursi Tamu dan Harganya'

    name = fields.Char(string='Name')
    tipe = fields.Selection(string='Tipe Kursi', selection = [('plastik', 'Plastik'), ('stainless', 'Stainless')])
    stok = fields.Integer(string='Stok Kursi')
    harga = fields.Integer(string='Harga Sewa')
    img = fields.Binary(string='Image')
    
    
    