# -*- coding: utf-8 -*-
# Copyright 2026 Trixocom
import re

MAIL_BLOCK = """
<div name="trx_portal_sign_link" style="margin: 20px 0px; text-align: center;">
    <a t-att-href="object.get_base_url() + object.get_portal_url()"
       style="display: inline-block; background-color: #4da6ff; color: #ffffff; font-size: 17px; font-weight: bold; padding: 14px 36px; border-radius: 8px; text-decoration: none;">
        APROBAR Y FIRMAR ESTE PRESUPUESTO
    </a>
</div>
"""

_BLOCK_RE = re.compile(r'<div[^>]*trx_portal_sign_link.*?</div>', re.S)


def _apply_mail_block(env):
    """Inserta (o reemplaza) el boton de aprobacion en el mail de cotizacion."""
    template = env.ref("sale.email_template_edi_sale", raise_if_not_found=False)
    if not template:
        return
    for lang_code, _name in env["res.lang"].get_installed():
        tpl = template.with_context(lang=lang_code)
        body = _BLOCK_RE.sub("", tpl.body_html or "")
        tpl.body_html = body + MAIL_BLOCK


def post_init_hook(env):
    """Activa la firma online y agrega el boton al portal en el mail de cotizacion."""
    env["res.company"].sudo().search([]).write({"portal_confirmation_sign": True})
    _apply_mail_block(env)
