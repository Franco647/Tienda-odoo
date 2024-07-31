from odoo import api, fields, models

class TiendaProductos(models.Model):
    _name = 'tienda.producto'

    nombre = fields.Char('Nombre', required=True)
    description = fields.Text('Descripción', help="Detalles del roducto")
    stock = fields.Integer('Stock')
    foto = fields.Binary('Foto')
    precio = fields.Float('Precio')
    categoria = fields.Many2one(sting='Categoria', comodel_name='tienda.categoria')
    
    def _compute_display_name(self):
        for obj in self:
            obj.display_name = obj.nombre