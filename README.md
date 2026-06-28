# trx-ui-tweaks

Pequeños ajustes de UI/UX para instancias Odoo Community administradas por Trixocom.

## Módulos

### `trx_hide_enterprise_apps`

Oculta del listado de **Apps** (`base.open_module_tree`) todos los módulos con licencia `OEEL-1` (Odoo Enterprise), incluidos los *teasers* que la imagen oficial `odoo:N.0` trae como placeholders de Enterprise (`state=uninstallable`).

Se auto-instala (`auto_install=True`) cuando `base` ya está presente.

### `trx_hide_enterprise_apps_website`

Bridge para cuando el módulo `website` está instalado. `website` define **otra action** llamada `Apps` (`website.action_website_add_features`) que el navbar superior usa como ruta `/odoo/apps`; sin este bridge los teasers OEEL-1 vuelven a aparecer en esa vista. Aplica el mismo dominio que el módulo padre.

Se auto-instala cuando `trx_hide_enterprise_apps` y `website` están ambos presentes.

**Compatibilidad**: Odoo 19 Community.
**Licencia**: LGPL-3.
**Autor**: Trixocom.

### `trx_dashboard_bank_name`

En el **tablero de Contabilidad** (kanban de `account.journal`), para los diarios que tienen una cuenta bancaria (`bank_account_id`) con banco asociado, la card pasa a mostrar el **nombre del banco** como título y el **número de cuenta** debajo, en lugar de mostrar sólo el número de cuenta como título.

Los nombres de banco provienen de la localización (`l10n_ar_bank` → `res.bank.name`). Los diarios sin banco (efectivo, ventas, compras, etc.) no se modifican.

Hereda `account.account_journal_dashboard_kanban_view` y agrega dos campos *related* (no almacenados) sobre `account.journal`: `trx_bank_name` y `trx_bank_acc_number`. No se auto-instala.
