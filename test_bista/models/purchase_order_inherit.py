from odoo import models, fields, api, _

class PurchaseOrderInherit(models.Model):
    _inherit = "purchase.order"

    # question 2 b

    product_group_id = fields.Many2one("parent.group", string="Product Group")
    filter_group = fields.Boolean(string="Active Group Filter")


class ProductTemplateInherit(models.Model):
    _inherit = 'product.template'

    group_ids = fields.Many2one('product.group', string='Group')
    rating = state = fields.Selection([('1', '1 Star'), 
                ('2', '2 Star'),
                ('3', '3 Star'),
                ('4', '4 Star'),
                ('5', '5 Star')], 
                default='1', string='Rating')


class PurchaseOrderLineInherit(models.Model):    
    _inherit = 'purchase.order.line'

    product_ratings = fields.Many2one('product.template')
    rating_select = fields.Selection('Rating', related='product_id.rating')
    

