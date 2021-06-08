# question 4 b

from odoo import fields, models, api, _

class WizardFilter(models.TransientModel):
    _name = 'wizard.filter'

    customer_id = fields.Many2many('res.partner', string='Customers')

    # question 4 c
    def wizard_filter(self):

        return {
            'name': "Filter Purchase Orders",
            'type': "ir.actions.act_window",
            'res_model': "purchase.order",
            'view_mode': "tree,form",
            'domain': [('partner_id.id','in', self.customer_id.ids)],
        }