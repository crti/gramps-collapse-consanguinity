#  File: collapse-consanguinity.gpr.py
register(GRAMPLET,
         id="Collapse-Consanguinity",
         name=_("Collapse-Consanguinity"),
         description = _("Gramplet showing pedigree collapse and spousal consanguinity."),
         version="1.0.0",
         gramps_target_version="5.1",
         status = STABLE,
         fname="collapse-consanguinity.py",
         height = 50,
         detached_width = 400,
         detached_height = 500,
         gramplet = 'CollapseConsanguinityGramplet',
         gramplet_title=_("Collapse-Consanguinity"),
         help_url="5.1_Addons#Addon_List",
         navtypes=['Person']
         )
