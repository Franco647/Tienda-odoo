from odoo import api, fields, models, exceptions

class TiendaPedido(models.Model):
    _name = 'tienda.pedido'

    numero = fields.Char(string='Numero de pedido', readonly=True, default=lambda self: self.env['ir.sequence'].next_by_code('tienda.pedido.sequence'))
    fecha = fields.Datetime(default=fields.Datetime.now(), readonly=False)
    cliente = fields.Many2many('tienda.cliente', string='Cliente') 
    productos_ids = fields.Many2many('tienda.producto', string='Productos', domain="[('stock', '>', '0')]")
    total = fields.Float(string='Total', compute='_compute_total')
    estado = fields.Selection([('pendiente', 'Pendiente'), ('confirmado', 'Confirmado')], default='pendiente')

    @api.constrains('estado', 'prodcutos_ids')
    def _check_productos_ids_confirmado(self):
        for obj in self:
            if obj.estado == 'confirmado' and not obj.productos_ids:
                raise exceptions.ValidationError('Debe seleccionar al menos un prodcuto para confirmar.')

    @api.depends('productos_ids')
    def _compute_total(self):
        for obj in self:
            total = 0
            for producto in obj.productos_ids:
                total += producto.precio
            obj.total = total

    def _compute_display_name(self):
        for obj in self:
            obj.display_name = obj.numero