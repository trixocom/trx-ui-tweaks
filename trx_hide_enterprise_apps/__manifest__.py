{
    "name": "Hide Enterprise Apps",
    "version": "19.0.1.0.1",
    "author": "Trixocom",
    "website": "https://www.trixocom.com",
    "license": "LGPL-3",
    "category": "Tools",
    "summary": "Oculta los modulos Enterprise (OEEL-1) del listado de Apps",
    "description": """
Trixocom — Hide Enterprise Apps
================================
Sobrescribe el dominio de la accion `base.open_module_tree` (menu Apps)
para excluir todos los modulos con licencia OEEL-1 (Odoo Enterprise),
incluidos los teasers `state=uninstallable` que la imagen oficial de
Odoo Community trae preinstalados como promo de Enterprise.

Mantiene visibles los modulos OPL-1 (modulos propietarios Trixocom) y
todo lo LGPL-3 / AGPL-3.
""",
    "depends": ["base"],
    "data": [
        "views/ir_actions.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": True,
}
