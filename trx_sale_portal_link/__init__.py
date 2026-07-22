# -*- coding: utf-8 -*-
# Copyright 2026 Trixocom

MAIL_BLOCK = """
<div name="trx_portal_sign_link" style="margin: 12px 0px; padding: 10px 12px; border: 1px solid #d0d0d0; border-radius: 6px; font-size: 13px;">
    Puede revisar, <strong>aprobar y firmar</strong> este presupuesto en l&#237;nea ingresando al portal:<br/>
    <a t-att-href="object.get_base_url() + object.get_portal_url()" t-out="object.get_base_url() + object.get_portal_url()"/>
</div>
"""


def post_init_hook(env):
    """Activa la firma online y agrega el link al portal en el mail de cotizacion."""
    env["res.company"].sudo().search([]).write({"portal_confirmation_sign": True})

    template = env.ref("sale.email_template_edi_sale", raise_if_not_found=False)
    if not template:
        return
    for lang_code, _name in env["res.lang"].get_installed():
        tpl = template.with_context(lang=lang_code)
        body = tpl.body_html or ""
        if "trx_portal_sign_link" not in body:
            tpl.body_html = body + MAIL_BLOCK
