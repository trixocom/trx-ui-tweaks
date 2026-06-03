# -*- coding: utf-8 -*-
# Copyright 2026 Trixocom
from odoo import models


class AccountMove(models.Model):
    _inherit = "account.move"

    def _get_name_invoice_report(self):
        """Reporte de factura para diarios SIN documentos fiscales.

        l10n_ar_ux fuerza el layout fiscal argentino
        (``l10n_ar.report_invoice_document``) para toda compa\u00f1\u00eda AR,
        incluso en facturas que NO usan documentos (p. ej. exportaci\u00f3n por
        formulario en USD). Ese layout no dibuja el logo (espera el punto de
        venta AFIP del diario) y muestra la leyenda de tipo de cambio.

        Para esas facturas (``l10n_latam_use_documents == False``) volvemos al
        reporte EST\u00c1NDAR de Odoo, que s\u00ed dibuja el logo de la compa\u00f1\u00eda
        (layout de reportes) y no incluye la leyenda AR.
        """
        self.ensure_one()
        if not self.l10n_latam_use_documents:
            return "account.report_invoice_document"
        return super()._get_name_invoice_report()
