from odoo import models, fields, api, _
from odoo.exceptions import UserError


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    discount_amount = fields.Float(string='Discount Amount')

    # @api.depends('price_unit', 'product_uom_qty', 'tax_id', 'discount_amount')
    # def _compute_amount(self):
    #     super(SaleOrderLine, self)._compute_amount()
    #     for line in self:
    #         if line.discount_amount:
    #             line.update({
    #                 'price_subtotal': line.price_subtotal - line.discount_amount,
    #                 'price_total': line.price_total - line.discount_amount
    #             })
    @api.depends('discount_amount')
    def _compute_price_reduce(self):
        for line in self:
            line.price_reduce = line.price_unit * (1.0 - line.discount / 100.0)
            if line.discount_amount > 0.0:
                line.price_reduce = line.price_unit - (line.discount_amount / line.product_uom_qty)
    
    @api.depends('discount_amount')
    def _compute_amount(self):
        """
        Compute the amounts of the SO line.
        """
        for line in self:
            if line.discount_amount == 0.0 and line.discount > 0.0:
                price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
            elif line.discount_amount >= 0.0 and line.discount == 0.0:
                price = line.price_unit
            else:
                raise UserError(_("Discount Method Error!"))

            taxes = line.tax_id.compute_all(price, line.order_id.currency_id, line.product_uom_qty, product=line.product_id, partner=line.order_id.partner_shipping_id, discount_amount=line.discount_amount)
            line.update({
                'price_tax': sum(t.get('amount', 0.0) for t in taxes.get('taxes', [])),
                'price_total': taxes['total_included'],
                'price_subtotal': taxes['total_excluded'],
            })
    
    def _prepare_invoice_line(self, **optional_values):
        res = super(SaleOrderLine, self)._prepare_invoice_line(**optional_values)
        res.update({
            'discount_amount': self.discount_amount,
            'quantity': self.product_uom_qty,  
        })
        return res

    def _convert_to_tax_base_line_dict(self):
        """ Convert the current record to a dictionary in order to use the generic taxes computation method
        defined on account.tax.

        :return: A python dictionary.
        """
        self.ensure_one()
        return self.env['account.tax']._convert_to_tax_base_line_dict(
            self,
            partner=self.order_id.partner_id,
            currency=self.order_id.currency_id,
            product=self.product_id,
            taxes=self.tax_id,
            price_unit=self.price_unit,
            quantity=self.product_uom_qty,
            discount=self.discount,
            price_subtotal=self.price_subtotal,
            discount_amount=self.discount_amount,
        )

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # @api.depends('order_line.tax_id', 'order_line.price_unit', 'amount_total', 'amount_untaxed', 'currency_id')
    # def _compute_tax_totals(self):
    #     for order in self:
    #         order_lines = order.order_line.filtered(lambda x: not x.display_type)
    #         order.tax_totals = self.env['account.tax']._prepare_tax_totals(
    #             [x._convert_to_tax_base_line_dict() for x in order_lines],
    #             order.currency_id or order.company_id.currency_id,
    #         )
            
    
    # @api.depends('order_line.price_subtotal', 'order_line.price_tax', 'order_line.price_total', 'order_line.discount_amount')
    # def _compute_amount(self):

    #     super(SaleOrder, self)._compute_amount()
    #     for order in self:
    #         total_untaxed = total_tax = 0.0
    #         for line in order.order_line:
    #             total_untaxed += line.price_subtotal
    #             total_tax += line.price_tax
                

    #         order.update({
    #             'amount_untaxed': order.currency_id.round(total_untaxed),
    #             'amount_tax': order.currency_id.round(total_tax),
    #             'amount_total': total_untaxed + total_tax
    #         })
