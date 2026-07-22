# -*- coding: utf-8 -*-
# Copyright 2026 Trixocom
{
    "name": "Trixocom — Presupuestos: aprobación y firma online",
    "version": "19.0.1.0.0",
    "author": "Trixocom",
    "website": "https://www.trixocom.com",
    "license": "LGPL-3",
    "category": "Sales",
    "summary": (
        "Agrega en el PDF y en el mail de los presupuestos un link directo "
        "al portal para que el cliente pueda aprobar y firmar online, y "
        "activa la firma online por defecto en todas las compañías."
    ),
    "description": """
Trixocom — Presupuestos: aprobación y firma online
==================================================
Mejora UX horizontal para todos los sistemas Odoo 19 Trixocom.

* PDF del presupuesto (sale.report_saleorder_document): en cotizaciones
  en borrador o enviadas agrega un bloque "Aprobación y firma en línea"
  con el link al portal (incluye access token), para que el cliente pueda
  revisar, aprobar y firmar sin pedir credenciales.
* Mail "Ventas: enviar cotización" (sale.email_template_edi_sale): el
  post_init_hook agrega al cuerpo, en todos los idiomas instalados, un
  bloque con el mismo link directo al portal (ademas del botón estándar
  de Odoo).
* Activa "Firma online" (res.company.portal_confirmation_sign) en todas
  las compañías al instalar, para que el portal ofrezca Aceptar y firmar.

El bloque de mail se inserta una sola vez (marcador trx_portal_sign_link);
reinstalar o actualizar el módulo no lo duplica.
""",
    "depends": ["sale"],
    "data": [
        "views/sale_report_templates.xml",
    ],
    "post_init_hook": "post_init_hook",
    "installable": True,
    "application": False,
    "auto_install": False,
}
