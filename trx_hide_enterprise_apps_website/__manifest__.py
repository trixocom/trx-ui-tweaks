{
    "name": "Hide Enterprise Apps — Bridge website",
    "version": "19.0.1.0.0",
    "author": "Trixocom",
    "website": "https://www.trixocom.com",
    "license": "LGPL-3",
    "category": "Tools",
    "summary": "Bridge: oculta OEEL-1 tambien en la action duplicada del modulo website",
    "description": """
Trixocom — Hide Enterprise Apps (Bridge website)
=================================================
Modulo bridge que sobrescribe la action `website.action_website_add_features`
(menu top-level "Apps" en `/odoo/apps`) para excluir los modulos OEEL-1.

El modulo `website` clona la action `base.open_module_tree` con un id propio
y la engancha al menu principal "Apps". Sin este bridge, sobrescribir solo
`base.open_module_tree` no alcanza, porque el navbar usa la version del
modulo website.

Auto-install: solo se instala cuando AMBOS modulos `trx_hide_enterprise_apps`
y `website` ya estan presentes en la DB.
""",
    "depends": ["trx_hide_enterprise_apps", "website"],
    "data": [
        "views/ir_actions.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": True,
}
