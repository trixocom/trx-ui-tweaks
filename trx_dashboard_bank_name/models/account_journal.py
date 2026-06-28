# -*- coding: utf-8 -*-
# Copyright 2026 Trixocom
from odoo import fields, models


class AccountJournal(models.Model):
    _inherit = "account.journal"

    # Nombre del banco de la cuenta bancaria del diario (res.bank.name).
    # Los nombres de banco vienen de la localización (l10n_ar_bank).
    trx_bank_name = fields.Char(
        string="Nombre del banco",
        related="bank_account_id.bank_id.name",
        store=False,
        readonly=True,
    )

    # Número de cuenta de la cuenta bancaria del diario.
    trx_bank_acc_number = fields.Char(
        string="Número de cuenta",
        related="bank_account_id.acc_number",
        store=False,
        readonly=True,
    )
