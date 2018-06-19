from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale
from werkzeug.routing import Map, Rule, NotFound, RequestRedirect
import werkzeug

class CustomCartForms(WebsiteSale):

    @http.route(['/shop/cart/custom_cart'], type='http', auth="public", methods=['POST'], website=True, multilang=False)
    def cart_update_custom(self, product_iref_1, add_qty_1, product_iref_2, add_qty_2, product_iref_3, add_qty_3, product_iref_4, add_qty_4, set_qty=0, goto_shop=None, lang=None, **kw):

        if lang:
            request.website = request.website.with_context(lang=lang)
        order = request.website.sale_get_order(force_create=1)
        errors = [];
        try:
            product = request.env['product.product'].search([('default_code', '=', product_iref_1)], limit=1)
            if product:
                optional_product_ids = []
                if hasattr(product, 'optional_product_ids'):
                    option_ids = product.optional_product_ids.mapped('product_variant_ids').ids
                    for k, v in kw.items():
                        if "optional-product-" in k and int(kw.get(k.replace("product", "add"))) and int(v) in option_ids:
                            optional_product_ids.append(int(v))

                attributes = self._filter_attributes(**kw)

                value = {}
                if add_qty_1 or set_qty:
                    value = order._cart_update(
                        product_id=int(product.id),
                        add_qty=int(add_qty_1),
                        set_qty=int(set_qty),
                        attributes=attributes,
                        optional_product_ids=optional_product_ids
                    )

                # options have all time the same quantity
                for option_id in optional_product_ids:
                    order._cart_update(
                        product_id=option_id,
                        set_qty=value.get('quantity'),
                        attributes=attributes,
                        linked_line_id=value.get('line_id')
                    )
        except Exception:
            pass

        try:
            product = request.env['product.product'].search([('default_code', '=', product_iref_2)], limit=1)
            if product:
                optional_product_ids = []
                if hasattr(product, 'optional_product_ids'):
                    option_ids = product.optional_product_ids.mapped('product_variant_ids').ids
                    for k, v in kw.items():
                        if "optional-product-" in k and int(kw.get(k.replace("product", "add"))) and int(v) in option_ids:
                            optional_product_ids.append(int(v))

                attributes = self._filter_attributes(**kw)

                value = {}
                if add_qty_2 or set_qty:
                    value = order._cart_update(
                        product_id=int(product.id),
                        add_qty=int(add_qty_2),
                        set_qty=int(set_qty),
                        attributes=attributes,
                        optional_product_ids=optional_product_ids
                    )

                # options have all time the same quantity
                for option_id in optional_product_ids:
                    order._cart_update(
                        product_id=option_id,
                        set_qty=value.get('quantity'),
                        attributes=attributes,
                        linked_line_id=value.get('line_id')
                    )
        except Exception:
            pass

        try:
            product = request.env['product.product'].search([('default_code', '=', product_iref_3)], limit=1)
            if product:
                optional_product_ids = []
                if hasattr(product, 'optional_product_ids'):
                    option_ids = product.optional_product_ids.mapped('product_variant_ids').ids
                    for k, v in kw.items():
                        if "optional-product-" in k and int(kw.get(k.replace("product", "add"))) and int(v) in option_ids:
                            optional_product_ids.append(int(v))

                attributes = self._filter_attributes(**kw)

                value = {}
                if add_qty_3 or set_qty:
                    value = order._cart_update(
                        product_id=int(product.id),
                        add_qty=int(add_qty_3),
                        set_qty=int(set_qty),
                        attributes=attributes,
                        optional_product_ids=optional_product_ids
                    )

                # options have all time the same quantity
                for option_id in optional_product_ids:
                    order._cart_update(
                        product_id=option_id,
                        set_qty=value.get('quantity'),
                        attributes=attributes,
                        linked_line_id=value.get('line_id')
                    )
        except Exception:
            pass

        try:
            product = request.env['product.product'].search([('default_code', '=', product_iref_4)], limit=1)
            if product:
                optional_product_ids = []
                if hasattr(product, 'optional_product_ids'):
                    option_ids = product.optional_product_ids.mapped('product_variant_ids').ids
                    for k, v in kw.items():
                        if "optional-product-" in k and int(kw.get(k.replace("product", "add"))) and int(v) in option_ids:
                            optional_product_ids.append(int(v))

                attributes = self._filter_attributes(**kw)

                value = {}
                if add_qty_4 or set_qty:
                    value = order._cart_update(
                        product_id=int(product.id),
                        add_qty=int(add_qty_4),
                        set_qty=int(set_qty),
                        attributes=attributes,
                        optional_product_ids=optional_product_ids
                    )

                # options have all time the same quantity
                for option_id in optional_product_ids:
                    order._cart_update(
                        product_id=option_id,
                        set_qty=value.get('quantity'),
                        attributes=attributes,
                        linked_line_id=value.get('line_id')
                    )
        except Exception:
            pass
        return werkzeug.utils.redirect('/shop/cart')
