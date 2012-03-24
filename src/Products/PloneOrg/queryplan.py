# query plan dumped at 'Sat Mar 24 21:24:45 2012'

queryplan = {
  ('', 'plone.org', 'portal_catalog'): {
    'VALUE_INDEXES': frozenset(['getSeverity', 'getStartHere']),
    ('Creator', 'allowedRolesAndUsers', 'effectiveRange', 'path', 'portal_type', 'show_inactive', 'sort_on', 'sort_order'): {
      'Creator':
      (0.002, 1, True),
      'Creator#intersection':
      (0.0006, 1, False),
      'allowedRolesAndUsers':
      (0.0033, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0032, 1, False),
      'effectiveRange':
      (0.0026, 1, True),
      'effectiveRange#intersection':
      (0.0015, 1, False),
      'path':
      (0.0063, 1, False),
      'path#intersection':
      (0.0, 1, False),
      'portal_type':
      (0.0011, 1, True),
      'portal_type#intersection':
      (0.0, 1, False),
      'show_inactive':
      (0.0, 0, False),
      'sort_on':
      (0.0, 0, False),
      'sort_order':
      (0.0, 0, False),
    },
    ('Creator', 'allowedRolesAndUsers', 'effectiveRange', 'sort_on', 'sort_order'): {
      'Creator':
      (0.0039, 1, True),
      'Creator#intersection':
      (0.0006, 1, False),
      'allowedRolesAndUsers':
      (0.0043, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0042, 1, False),
      'effectiveRange':
      (0.0384, 1, True),
      'effectiveRange#intersection':
      (0.0, 1, False),
      'sort_on':
      (0.0, 0, False),
      'sort_order':
      (0.0, 0, False),
    },
    ('SearchableText', 'allowedRolesAndUsers', 'effectiveRange', 'getCategories', 'getCompatibility', 'portal_type', 'sort_on', 'sort_order'): {
      'SearchableText':
      (0.0, 1, False),
      'allowedRolesAndUsers':
      (0.0001, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0, 1, False),
      'effectiveRange':
      (0.0072, 1, True),
      'effectiveRange#intersection':
      (0.0039, 1, False),
      'getCategories':
      (0.0308, 1, True),
      'getCategories#intersection':
      (0.0293, 1, False),
      'getCompatibility':
      (0.0008, 1, True),
      'getCompatibility#intersection':
      (0.0008, 1, False),
      'portal_type':
      (0.0003, 1, True),
      'portal_type#intersection':
      (0.0002, 1, False),
      'sort_on':
      (0.0, 0, False),
      'sort_order':
      (0.0, 0, False),
    },
    ('SearchableText', 'allowedRolesAndUsers', 'effectiveRange', 'getCategories', 'portal_type', 'sort_on', 'sort_order'): {
      'SearchableText':
      (0.0, 1, False),
      'allowedRolesAndUsers':
      (0.0001, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0, 1, False),
      'effectiveRange':
      (0.0001, 1, True),
      'effectiveRange#intersection':
      (0.0, 1, False),
      'getCategories':
      (0.1438, 1, True),
      'getCategories#intersection':
      (0.1417, 1, False),
      'portal_type':
      (0.0032, 1, True),
      'portal_type#intersection':
      (0.0031, 1, False),
      'sort_on':
      (0.0, 0, False),
      'sort_order':
      (0.0, 0, False),
    },
    ('SearchableText', 'allowedRolesAndUsers', 'effectiveRange', 'getCompatibility', 'portal_type', 'sort_on', 'sort_order'): {
      'SearchableText':
      (0.0, 1, False),
      'allowedRolesAndUsers':
      (0.0001, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0, 1, False),
      'effectiveRange':
      (0.0001, 1, True),
      'effectiveRange#intersection':
      (0.0, 1, False),
      'getCompatibility':
      (0.0003, 1, True),
      'getCompatibility#intersection':
      (0.0003, 1, False),
      'portal_type':
      (0.0031, 1, True),
      'portal_type#intersection':
      (0.0031, 1, False),
      'sort_on':
      (0.0, 0, False),
      'sort_order':
      (0.0, 0, False),
    },
    ('SearchableText', 'allowedRolesAndUsers', 'effectiveRange', 'path', 'portal_type', 'show_inactive', 'sort_on', 'sort_order'): {
      'SearchableText':
      (0.0113, 1, False),
      'SearchableText#intersection':
      (0.0, 1, False),
      'allowedRolesAndUsers':
      (0.004, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0039, 1, False),
      'effectiveRange':
      (0.0016, 1, True),
      'effectiveRange#intersection':
      (0.0008, 1, False),
      'path':
      (0.0077, 1, False),
      'path#intersection':
      (0.0013, 1, False),
      'portal_type':
      (0.0021, 1, True),
      'portal_type#intersection':
      (0.0006, 1, False),
      'show_inactive':
      (0.0, 0, False),
      'sort_on':
      (0.0, 0, False),
      'sort_order':
      (0.0, 0, False),
    },
    ('SearchableText', 'allowedRolesAndUsers', 'effectiveRange', 'path', 'portal_type', 'sort_limit'): {
      'SearchableText':
      (1.4404, 1, False),
      'SearchableText#intersection':
      (0.0006, 1, False),
      'allowedRolesAndUsers':
      (0.0033, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0032, 1, False),
      'effectiveRange':
      (0.0002, 1, True),
      'effectiveRange#intersection':
      (0.0, 1, False),
      'path':
      (0.0061, 1, False),
      'path#intersection':
      (0.0, 1, False),
      'portal_type':
      (0.0012, 1, True),
      'portal_type#intersection':
      (0.0, 1, False),
      'sort_limit':
      (0.0, 0, False),
    },
    ('SearchableText', 'allowedRolesAndUsers', 'effectiveRange', 'portal_type', 'sort_on', 'sort_order'): {
      'SearchableText':
      (0.0, 1, False),
      'allowedRolesAndUsers':
      (0.0001, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0, 1, False),
      'effectiveRange':
      (0.0003, 1, True),
      'effectiveRange#intersection':
      (0.0001, 1, False),
      'portal_type':
      (0.0033, 1, True),
      'portal_type#intersection':
      (0.0032, 1, False),
      'sort_on':
      (0.0, 0, False),
      'sort_order':
      (0.0, 0, False),
    },
    ('Subject', 'allowedRolesAndUsers', 'effectiveRange', 'path', 'portal_type', 'show_inactive', 'sort_order'): {
      'Subject':
      (0.0023, 1, True),
      'Subject#intersection':
      (0.0006, 1, False),
      'allowedRolesAndUsers':
      (0.0034, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0033, 1, False),
      'effectiveRange':
      (0.0002, 1, True),
      'effectiveRange#intersection':
      (0.0, 1, False),
      'path':
      (0.0066, 1, False),
      'path#intersection':
      (0.0, 1, False),
      'portal_type':
      (0.0012, 1, True),
      'portal_type#intersection':
      (0.0, 1, False),
      'show_inactive':
      (0.0, 0, False),
      'sort_order':
      (0.0, 0, False),
    },
    ('Subject', 'allowedRolesAndUsers', 'effectiveRange', 'path', 'portal_type', 'sort_on', 'sort_order'): {
      'Subject':
      (0.0013, 1, True),
      'Subject#intersection':
      (0.0, 1, False),
      'allowedRolesAndUsers':
      (0.0008, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0007, 1, False),
      'effectiveRange':
      (0.0004, 1, True),
      'effectiveRange#intersection':
      (0.0, 1, False),
      'path':
      (0.0066, 1, False),
      'path#intersection':
      (0.0, 1, False),
      'portal_type':
      (0.0001, 1, True),
      'portal_type#intersection':
      (0.0001, 1, False),
      'sort_on':
      (0.0, 0, False),
      'sort_order':
      (0.0, 0, False),
    },
    ('Type', 'allowedRolesAndUsers', 'effectiveRange', 'review_state', 'sort_on'): {
      'Type':
      (0.0191, 1, True),
      'Type#intersection':
      (0.0, 1, False),
      'allowedRolesAndUsers':
      (0.1312, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.1311, 1, False),
      'effectiveRange':
      (0.0002, 1, True),
      'effectiveRange#intersection':
      (0.0, 1, False),
      'review_state':
      (0.027, 1, True),
      'review_state#intersection':
      (0.0026, 1, False),
      'sort_on':
      (0.0, 0, False),
    },
    ('allowedRolesAndUsers', 'effectiveRange', 'end', 'portal_type', 'review_state', 'sort_on'): {
      'allowedRolesAndUsers':
      (0.0001, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0, 1, False),
      'effectiveRange':
      (0.0072, 1, True),
      'effectiveRange#intersection':
      (0.0039, 1, False),
      'end':
      (0.0008, 1, True),
      'end#intersection':
      (0.0006, 1, False),
      'portal_type':
      (0.0002, 1, True),
      'portal_type#intersection':
      (0.0001, 1, False),
      'review_state':
      (0.0011, 1, True),
      'review_state#intersection':
      (0.0011, 1, False),
      'sort_on':
      (0.0, 0, False),
    },
    ('allowedRolesAndUsers', 'effectiveRange', 'getArea', 'path', 'portal_type', 'review_state', 'sort_on', 'sort_order'): {
      'allowedRolesAndUsers':
      (0.0025, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0024, 1, False),
      'effectiveRange':
      (0.0001, 1, True),
      'effectiveRange#intersection':
      (0.0, 1, False),
      'getArea':
      (0.0004, 1, True),
      'getArea#intersection':
      (0.0003, 1, False),
      'path':
      (0.0055, 1, False),
      'path#intersection':
      (0.0, 1, False),
      'portal_type':
      (0.0005, 1, True),
      'portal_type#intersection':
      (0.0005, 1, False),
      'review_state':
      (0.0003, 1, True),
      'review_state#intersection':
      (0.0, 1, False),
      'sort_on':
      (0.0, 0, False),
      'sort_order':
      (0.0, 0, False),
    },
    ('allowedRolesAndUsers', 'effectiveRange', 'getCategories', 'path', 'portal_type', 'review_state', 'show_inactive', 'sort_on', 'sort_order'): {
      'allowedRolesAndUsers':
      (0.0032, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0031, 1, False),
      'effectiveRange':
      (0.0006, 1, True),
      'effectiveRange#intersection':
      (0.0002, 1, False),
      'getCategories':
      (0.0364, 1, True),
      'getCategories#intersection':
      (0.0346, 1, False),
      'path':
      (0.0002, 1, False),
      'path#intersection':
      (0.0, 1, False),
      'portal_type':
      (0.0008, 1, True),
      'portal_type#intersection':
      (0.0007, 1, False),
      'review_state':
      (0.0029, 1, True),
      'review_state#intersection':
      (0.0029, 1, False),
      'show_inactive':
      (0.0, 0, False),
      'sort_on':
      (0.0, 0, False),
      'sort_order':
      (0.0, 0, False),
    },
    ('allowedRolesAndUsers', 'effectiveRange', 'getCountry', 'meta_type', 'sort_on'): {
      'allowedRolesAndUsers':
      (0.0001, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0, 1, False),
      'effectiveRange':
      (0.0075, 1, True),
      'effectiveRange#intersection':
      (0.0041, 1, False),
      'getCountry':
      (0.0414, 1, True),
      'getCountry#intersection':
      (0.0399, 1, False),
      'meta_type':
      (0.4611, 1, True),
      'meta_type#intersection':
      (0.4369, 1, False),
      'sort_on':
      (0.0, 0, False),
    },
    ('allowedRolesAndUsers', 'effectiveRange', 'getSections', 'path', 'portal_type'): {
      'allowedRolesAndUsers':
      (0.0002, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0001, 1, False),
      'effectiveRange':
      (0.0002, 1, True),
      'effectiveRange#intersection':
      (0.0, 1, False),
      'getSections':
      (0.001, 1, True),
      'getSections#intersection':
      (0.0, 1, False),
      'path':
      (0.0002, 1, False),
      'path#intersection':
      (0.0, 1, False),
      'portal_type':
      (0.0241, 1, True),
      'portal_type#intersection':
      (0.0004, 1, False),
    },
    ('allowedRolesAndUsers', 'effectiveRange', 'getSections', 'path', 'show_inactive', 'sort_on'): {
      'allowedRolesAndUsers':
      (0.0023, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0023, 1, False),
      'effectiveRange':
      (0.0001, 1, True),
      'effectiveRange#intersection':
      (0.0, 1, False),
      'getSections':
      (0.0002, 1, True),
      'getSections#intersection':
      (0.0, 1, False),
      'path':
      (0.0001, 1, False),
      'path#intersection':
      (0.0, 1, False),
      'show_inactive':
      (0.0, 0, False),
      'sort_on':
      (0.0, 0, False),
    },
    ('allowedRolesAndUsers', 'effectiveRange', 'is_default_page', 'is_folderish', 'path', 'portal_type', 'review_state', 'sort_on', 'sort_order'): {
      'allowedRolesAndUsers':
      (0.0033, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0032, 1, False),
      'effectiveRange':
      (0.0001, 1, True),
      'effectiveRange#intersection':
      (0.0, 1, False),
      'is_default_page':
      (0.0001, 1, True),
      'is_default_page#intersection':
      (0.0, 1, False),
      'is_folderish':
      (0.0019, 1, True),
      'is_folderish#intersection':
      (0.0, 1, False),
      'path':
      (0.0001, 1, False),
      'path#intersection':
      (0.0, 1, False),
      'portal_type':
      (0.0004, 1, True),
      'portal_type#intersection':
      (0.0, 1, False),
      'review_state':
      (0.0013, 1, True),
      'review_state#intersection':
      (0.0012, 1, False),
      'sort_on':
      (0.0, 0, False),
      'sort_order':
      (0.0, 0, False),
    },
    ('allowedRolesAndUsers', 'effectiveRange', 'is_default_page', 'object_provides', 'path', 'sort_on'): {
      'allowedRolesAndUsers':
      (0.0006, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0005, 1, False),
      'effectiveRange':
      (0.0002, 1, True),
      'effectiveRange#intersection':
      (0.0, 1, False),
      'is_default_page':
      (0.0001, 1, True),
      'is_default_page#intersection':
      (0.0, 1, False),
      'object_provides':
      (0.0002, 1, True),
      'object_provides#intersection':
      (0.0001, 1, False),
      'path':
      (0.0005, 1, False),
      'path#intersection':
      (0.0, 1, False),
      'sort_on':
      (0.0, 0, False),
    },
    ('allowedRolesAndUsers', 'effectiveRange', 'is_default_page', 'path', 'portal_type', 'review_state', 'sort_on', 'sort_order'): {
      'allowedRolesAndUsers':
      (0.0034, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0033, 1, False),
      'effectiveRange':
      (0.0004, 1, True),
      'effectiveRange#intersection':
      (0.0, 1, False),
      'is_default_page':
      (0.0001, 1, True),
      'is_default_page#intersection':
      (0.0, 1, False),
      'path':
      (0.0002, 1, False),
      'path#intersection':
      (0.0, 1, False),
      'portal_type':
      (0.0004, 1, True),
      'portal_type#intersection':
      (0.0, 1, False),
      'review_state':
      (0.0013, 1, True),
      'review_state#intersection':
      (0.0012, 1, False),
      'sort_on':
      (0.0, 0, False),
      'sort_order':
      (0.0, 0, False),
    },
    ('allowedRolesAndUsers', 'effectiveRange', 'meta_type', 'sort_on'): {
      'allowedRolesAndUsers':
      (0.0001, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0, 1, False),
      'effectiveRange':
      (0.008, 1, True),
      'effectiveRange#intersection':
      (0.0042, 1, False),
      'meta_type':
      (0.0007, 1, True),
      'meta_type#intersection':
      (0.0006, 1, False),
      'sort_on':
      (0.0, 0, False),
    },
    ('allowedRolesAndUsers', 'effectiveRange', 'object_provides', 'path', 'show_inactive', 'sort_on'): {
      'allowedRolesAndUsers':
      (0.0001, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0001, 1, False),
      'effectiveRange':
      (0.0001, 1, True),
      'effectiveRange#intersection':
      (0.0, 1, False),
      'object_provides':
      (0.0001, 1, True),
      'object_provides#intersection':
      (0.0, 1, False),
      'path':
      (0.0001, 1, False),
      'path#intersection':
      (0.0, 1, False),
      'show_inactive':
      (0.0, 0, False),
      'sort_on':
      (0.0, 0, False),
    },
    ('allowedRolesAndUsers', 'effectiveRange', 'object_provides', 'path', 'sort_on'): {
      'allowedRolesAndUsers':
      (0.002, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0019, 1, False),
      'effectiveRange':
      (0.0001, 1, True),
      'effectiveRange#intersection':
      (0.0, 1, False),
      'object_provides':
      (0.0001, 1, True),
      'object_provides#intersection':
      (0.0, 1, False),
      'path':
      (0.0001, 1, False),
      'path#intersection':
      (0.0, 1, False),
      'sort_on':
      (0.0, 0, False),
    },
    ('allowedRolesAndUsers', 'effectiveRange', 'path'): {
      'allowedRolesAndUsers':
      (0.0036, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0035, 1, False),
      'effectiveRange':
      (0.0003, 1, True),
      'effectiveRange#intersection':
      (0.0001, 1, False),
      'path':
      (0.3144, 1, False),
      'path#intersection':
      (0.0, 1, False),
    },
    ('allowedRolesAndUsers', 'effectiveRange', 'path', 'portal_type'): {
      'allowedRolesAndUsers':
      (0.0031, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.003, 1, False),
      'effectiveRange':
      (0.0005, 1, True),
      'effectiveRange#intersection':
      (0.0002, 1, False),
      'path':
      (0.0001, 1, False),
      'path#intersection':
      (0.0, 1, False),
      'portal_type':
      (0.0029, 1, True),
      'portal_type#intersection':
      (0.0028, 1, False),
    },
    ('allowedRolesAndUsers', 'effectiveRange', 'path', 'portal_type', 'review_state', 'show_inactive', 'sort_on', 'sort_order'): {
      'allowedRolesAndUsers':
      (0.0042, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0041, 1, False),
      'effectiveRange':
      (0.0027, 1, True),
      'effectiveRange#intersection':
      (0.0015, 1, False),
      'path':
      (0.0063, 1, False),
      'path#intersection':
      (0.0, 1, False),
      'portal_type':
      (0.0073, 1, True),
      'portal_type#intersection':
      (0.0073, 1, False),
      'review_state':
      (0.052, 1, True),
      'review_state#intersection':
      (0.0493, 1, False),
      'show_inactive':
      (0.0, 0, False),
      'sort_on':
      (0.0, 0, False),
      'sort_order':
      (0.0, 0, False),
    },
    ('allowedRolesAndUsers', 'effectiveRange', 'path', 'portal_type', 'review_state', 'sort_on', 'sort_order'): {
      'allowedRolesAndUsers':
      (0.0, 0, False),
      'effectiveRange':
      (0.0, 0, False),
      'path':
      (0.0041, 1, False),
      'path#intersection':
      (0.0, 1, False),
      'portal_type':
      (0.0, 0, False),
      'review_state':
      (0.0003, 1, True),
      'review_state#intersection':
      (0.0002, 1, False),
      'sort_on':
      (0.0, 0, False),
      'sort_order':
      (0.0, 0, False),
    },
    ('allowedRolesAndUsers', 'effectiveRange', 'path', 'portal_type', 'show_inactive', 'sort_on'): {
      'allowedRolesAndUsers':
      (0.0021, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.002, 1, False),
      'effectiveRange':
      (0.0001, 1, True),
      'effectiveRange#intersection':
      (0.0, 1, False),
      'path':
      (0.0001, 1, False),
      'path#intersection':
      (0.0, 1, False),
      'portal_type':
      (0.0007, 1, True),
      'portal_type#intersection':
      (0.0, 1, False),
      'show_inactive':
      (0.0, 0, False),
      'sort_on':
      (0.0, 0, False),
    },
    ('allowedRolesAndUsers', 'effectiveRange', 'path', 'portal_type', 'show_inactive', 'sort_on', 'sort_order'): {
      'allowedRolesAndUsers':
      (0.0014, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0013, 1, False),
      'effectiveRange':
      (0.0004, 1, True),
      'effectiveRange#intersection':
      (0.0, 1, False),
      'path':
      (0.003, 1, False),
      'path#intersection':
      (0.0, 1, False),
      'portal_type':
      (0.0003, 1, True),
      'portal_type#intersection':
      (0.0003, 1, False),
      'show_inactive':
      (0.0, 0, False),
      'sort_on':
      (0.0, 0, False),
      'sort_order':
      (0.0, 0, False),
    },
    ('allowedRolesAndUsers', 'effectiveRange', 'path', 'portal_type', 'sort_on'): {
      'allowedRolesAndUsers':
      (0.0027, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0027, 1, False),
      'effectiveRange':
      (0.0001, 1, True),
      'effectiveRange#intersection':
      (0.0, 1, False),
      'path':
      (0.0022, 1, False),
      'path#intersection':
      (0.0, 1, False),
      'portal_type':
      (0.0006, 1, True),
      'portal_type#intersection':
      (0.0005, 1, False),
      'sort_on':
      (0.0, 0, False),
    },
    ('allowedRolesAndUsers', 'effectiveRange', 'path', 'portal_type', 'sort_on', 'sort_order'): {
      'allowedRolesAndUsers':
      (0.0019, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0018, 1, False),
      'effectiveRange':
      (0.0001, 1, True),
      'effectiveRange#intersection':
      (0.0, 1, False),
      'path':
      (0.0026, 1, False),
      'path#intersection':
      (0.0, 1, False),
      'portal_type':
      (0.0005, 1, True),
      'portal_type#intersection':
      (0.0004, 1, False),
      'sort_on':
      (0.0, 0, False),
      'sort_order':
      (0.0, 0, False),
    },
    ('allowedRolesAndUsers', 'effectiveRange', 'path', 'show_inactive', 'sort_on'): {
      'allowedRolesAndUsers':
      (0.0025, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0024, 1, False),
      'effectiveRange':
      (0.0001, 1, True),
      'effectiveRange#intersection':
      (0.0, 1, False),
      'path':
      (0.0001, 1, False),
      'path#intersection':
      (0.0, 1, False),
      'show_inactive':
      (0.0, 0, False),
      'sort_on':
      (0.0, 0, False),
    },
    ('allowedRolesAndUsers', 'effectiveRange', 'path', 'sort_on', 'sort_order'): {
      'allowedRolesAndUsers':
      (0.004, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.004, 1, False),
      'effectiveRange':
      (0.0023, 1, True),
      'effectiveRange#intersection':
      (0.0015, 1, False),
      'path':
      (0.0063, 1, False),
      'path#intersection':
      (0.0, 1, False),
      'sort_on':
      (0.0, 0, False),
      'sort_order':
      (0.0, 0, False),
    },
    ('allowedRolesAndUsers', 'effectiveRange', 'portal_type', 'review_state', 'sort_on', 'sort_order'): {
      'allowedRolesAndUsers':
      (0.0001, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0, 1, False),
      'effectiveRange':
      (0.0074, 1, True),
      'effectiveRange#intersection':
      (0.004, 1, False),
      'portal_type':
      (0.0007, 1, True),
      'portal_type#intersection':
      (0.0007, 1, False),
      'review_state':
      (0.0012, 1, True),
      'review_state#intersection':
      (0.0012, 1, False),
      'sort_on':
      (0.0, 0, False),
      'sort_order':
      (0.0, 0, False),
    },
    ('allowedRolesAndUsers', 'end', 'portal_type', 'review_state', 'sort_on'): {
      'allowedRolesAndUsers':
      (0.0049, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0, 1, False),
      'end':
      (0.0049, 1, True),
      'end#intersection':
      (0.0006, 1, False),
      'portal_type':
      (0.0002, 1, True),
      'portal_type#intersection':
      (0.0001, 1, False),
      'review_state':
      (0.0011, 1, True),
      'review_state#intersection':
      (0.0011, 1, False),
      'sort_on':
      (0.0, 0, False),
    },
    ('allowedRolesAndUsers', 'is_default_page', 'is_folderish', 'path', 'portal_type', 'review_state', 'sort_on', 'sort_order'): {
      'allowedRolesAndUsers':
      (0.0386, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0, 1, False),
      'is_default_page':
      (0.0001, 1, True),
      'is_default_page#intersection':
      (0.0, 1, False),
      'is_folderish':
      (0.002, 1, True),
      'is_folderish#intersection':
      (0.0, 1, False),
      'path':
      (0.0001, 1, False),
      'path#intersection':
      (0.0, 1, False),
      'portal_type':
      (0.0004, 1, True),
      'portal_type#intersection':
      (0.0, 1, False),
      'review_state':
      (0.0013, 1, True),
      'review_state#intersection':
      (0.0012, 1, False),
      'sort_on':
      (0.0, 0, False),
      'sort_order':
      (0.0, 0, False),
    },
    ('allowedRolesAndUsers', 'object_provides', 'path', 'sort_on'): {
      'allowedRolesAndUsers':
      (0.0025, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0, 1, False),
      'object_provides':
      (0.0001, 1, True),
      'object_provides#intersection':
      (0.0, 1, False),
      'path':
      (0.0002, 1, False),
      'path#intersection':
      (0.0, 1, False),
      'sort_on':
      (0.0, 0, False),
    },
    ('allowedRolesAndUsers', 'path', 'review_state', 'sort_on', 'sort_order'): {
    },
    ('allowedRolesAndUsers', 'portal_type', 'review_state', 'sort_on', 'sort_order'): {
      'allowedRolesAndUsers':
      (0.0054, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0, 1, False),
      'portal_type':
      (0.0007, 1, True),
      'portal_type#intersection':
      (0.0007, 1, False),
      'review_state':
      (0.0013, 1, True),
      'review_state#intersection':
      (0.0012, 1, False),
      'sort_on':
      (0.0, 0, False),
      'sort_order':
      (0.0, 0, False),
    },
    ('path',): {
      'path':
      (0.0051, 1, False),
      'path#intersection':
      (0.0, 1, False),
    },
  },
  ('', 'plone.org', 'reference_catalog'): {
    'VALUE_INDEXES': frozenset([]),
    ('relationship', 'sourceUID'): {
      'relationship':
      (0.0001, 1, True),
      'relationship#intersection':
      (0.0, 1, False),
      'sourceUID':
      (0.0001, 1, True),
      'sourceUID#intersection':
      (0.0, 1, False),
    },
    ('relationship', 'targetUID'): {
      'relationship':
      (0.2632, 1, True),
      'relationship#intersection':
      (0.2507, 1, False),
      'targetUID':
      (0.0001, 1, True),
      'targetUID#intersection':
      (0.0, 1, False),
    },
  },
  ('', 'plone.org', 'uid_catalog'): {
    'VALUE_INDEXES': frozenset([]),
  },
}
