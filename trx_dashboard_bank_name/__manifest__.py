# -*- coding: utf-8 -*-
# Copyright 2026 Trixocom
{
    "name": "Trixocom — Tablero: nombre de banco en las cards",
    "version": "19.0.1.0.0",
    "author": "Trixocom",
    "website": "https://www.trixocom.com",
    "license": "LGPL-3",
    "category": "Accounting",
    "summary": (
        "En el tablero de Contabilidad muestra el nombre del banco como "
        "título de la card y el número de cuenta debajo, para los "
        "diarios asociados a una cuenta bancaria."
    ),
    "description": """Trixocom — Tablero: nombre de banco en las cards
====================================================
Fix horizontal para el tablero de Contabilidad (kanban de account.journal).

Para los diarios que tienen una cuenta bancaria (bank_account_id) con un
banco asociado, la card del tablero pasa a mostrar:

  * Título  -> nombre del banco (res.bank.name, provisto por la
    localización l10n_ar_bank).
  * Debajo  -> número de cuenta (acc_number).

Los diarios sin banco (efectivo, ventas, compras, etc.) no se modifican y
siguen mostrando el nombre del diario como hasta ahora.
""",
    "depends": ["account", "l10n_ar_bank"],
    "data": [
        "views/account_journal_dashboard.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
