# trx-ui-tweaks

Pequeños ajustes de UI/UX para instancias Odoo Community administradas por Trixocom.

## Módulos

### `trx_hide_enterprise_apps`

Oculta del listado de **Apps** (`base.open_module_tree`) todos los módulos con licencia `OEEL-1` (Odoo Enterprise), incluidos los *teasers* que la imagen oficial `odoo:N.0` trae como placeholders de Enterprise (`state=uninstallable`).

Se auto-instala (`auto_install=True`) cuando `base` ya está presente, así que basta con sumarlo al `addons_path` y hacer un update de la DB.

**Compatibilidad**: Odoo 19 Community.
**Licencia**: LGPL-3.
**Autor**: Trixocom.
