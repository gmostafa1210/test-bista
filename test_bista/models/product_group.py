from odoo import api, models, fields, _
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError
import re

class ParentGroup(models.Model):
    _name = 'parent.group'
    _description = 'Parent Group'
    _rec_name = 'parent_group'

    parent_group = fields.Char(string='Parent Group')

    product_group_line = fields.One2many('product.group.line', 'product_group_id', string='Product Line')


class ProductGroup(models.Model):
    _name = 'product.group'
    _description = 'Product Group'

    name = fields.Char(string='Product Name')
    group = fields.Char(string='Product Group')


class ProductGroupLine(models.Model):
    _name = 'product.group.line'
    _description = 'Product Group Line'
    _rec_name = 'name_id'
    _sql_constraints = [
        ('short_code_uniq', 'unique (short_code)', 'Short Code exists!')
    ]

    name_id = fields.Many2one('product.group', string='Product Name')
    short_code = fields.Char(string='Short Code')

    product_group_id = fields.Many2one('parent.group', string='Product Under')

    @api.model
    def create(self, values):
        code_str = values['short_code']
        code_num = code_str[3::]
        if code_str[0:3] != 'pg-':
            raise UserError(_('Invalid input. Please start with "pg-"'))
        if code_num.isnumeric() == False:
            raise UserError(_('Invalid input. Insert number after "pg-"'))
        else:
            return super(ProductGroupLine, self).create(values)
    
    def write(self, values):
        if 'short_code' in values.keys():
            code_str = values['short_code']
            code_num = code_str[3::]
            if code_str[0:3] != 'pg-':
                raise UserError(_('Invalid input. Please start with "pg-"'))
            if code_num.isnumeric() == False:
                raise UserError(_('Invalid input. Insert number after "pg-"'))
            else:
                return super(ProductGroupLine, self).write(values)


class ResPartnerNew(models.Model):
    _inherit = "res.partner"

    @api.onchange('email')
    def validate_mail(self):
        if self.email:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@gmail.com', self.email)
            if match == None:
                raise ValidationError('Not a valid E-mail ID')


