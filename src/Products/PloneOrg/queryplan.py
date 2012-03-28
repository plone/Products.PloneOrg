# query plan dumped at 'Wed Mar 28 01:41:43 2012'

queryplan = {
  ('', 'plone.org', 'portal_catalog'): {
    'VALUE_INDEXES': frozenset(['getSeverity', 'in_reply_to', 'isOutdated', 'getSelfCertifiedCriteria', 'getStartHere']),
    ('Creator', 'allowedRolesAndUsers', 'effectiveRange', 'path', 'portal_type', 'show_inactive', 'sort_on', 'sort_order'): {
      'Creator':
      (0.0144, 1, True),
      'Creator#intersection':
      (0.00020000000000000001, 1, False),
      'allowedRolesAndUsers':
      (0.0038999999999999998, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0037000000000000002, 1, False),
      'effectiveRange':
      (0.0027000000000000001, 1, True),
      'effectiveRange#intersection':
      (0.0016000000000000001, 1, False),
      'path':
      (0.0067000000000000002, 1, False),
      'path#intersection':
      (0.0, 1, False),
      'portal_type':
      (0.0025000000000000001, 1, True),
      'portal_type#intersection':
      (0.00089999999999999998, 1, False),
      'show_inactive':
      (0.0, 0, False),
      'sort_on':
      (0.0, 0, False),
      'sort_order':
      (0.0, 0, False),
    },
    ('Creator', 'allowedRolesAndUsers', 'effectiveRange', 'sort_on', 'sort_order'): {
      'Creator':
      (0.0018, 1, True),
      'Creator#intersection':
      (0.00059999999999999995, 1, False),
      'allowedRolesAndUsers':
      (0.0001, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0, 1, False),
      'effectiveRange':
      (0.0074999999999999997, 1, True),
      'effectiveRange#intersection':
      (0.0038999999999999998, 1, False),
      'sort_on':
      (0.0, 0, False),
      'sort_order':
      (0.0, 0, False),
    },
    ('SearchableText', 'Type', 'allowedRolesAndUsers', 'b_size', 'b_start', 'effectiveRange', 'sort_on', 'start'): {
      'SearchableText':
      (0.090899999999999995, 1, False),
      'SearchableText#intersection':
      (0.0, 1, False),
      'Type':
      (0.00020000000000000001, 1, True),
      'Type#intersection':
      (0.0001, 1, False),
      'allowedRolesAndUsers':
      (0.0032000000000000002, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0030999999999999999, 1, False),
      'b_size':
      (0.0, 0, False),
      'b_start':
      (0.0, 0, False),
      'effectiveRange':
      (0.00020000000000000001, 1, True),
      'effectiveRange#intersection':
      (0.0, 1, False),
      'sort_on':
      (0.0, 0, False),
      'start':
      (0.00020000000000000001, 1, True),
      'start#intersection':
      (0.0, 1, False),
    },
    ('SearchableText', 'allowedRolesAndUsers', 'b_size', 'b_start', 'effectiveRange', 'path', 'portal_type', 'show_inactive'): {
      'SearchableText':
      (0.016500000000000001, 1, False),
      'SearchableText#intersection':
      (0.0, 1, False),
      'allowedRolesAndUsers':
      (0.0030999999999999999, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0030000000000000001, 1, False),
      'b_size':
      (0.0, 0, False),
      'b_start':
      (0.0, 0, False),
      'effectiveRange':
      (0.00020000000000000001, 1, True),
      'effectiveRange#intersection':
      (0.0, 1, False),
      'path':
      (0.0027000000000000001, 1, False),
      'path#intersection':
      (0.0025000000000000001, 1, False),
      'portal_type':
      (0.00029999999999999997, 1, True),
      'portal_type#intersection':
      (0.00020000000000000001, 1, False),
      'show_inactive':
      (0.0, 0, False),
    },
    ('SearchableText', 'allowedRolesAndUsers', 'b_size', 'b_start', 'effectiveRange', 'path', 'portal_type', 'show_inactive', 'sort_order'): {
      'SearchableText':
      (0.001, 1, False),
      'SearchableText#intersection':
      (0.0, 1, False),
      'allowedRolesAndUsers':
      (0.0030000000000000001, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0028999999999999998, 1, False),
      'b_size':
      (0.0, 0, False),
      'b_start':
      (0.0, 0, False),
      'effectiveRange':
      (0.00020000000000000001, 1, True),
      'effectiveRange#intersection':
      (0.0, 1, False),
      'path':
      (0.0025999999999999999, 1, False),
      'path#intersection':
      (0.0025000000000000001, 1, False),
      'portal_type':
      (0.00029999999999999997, 1, True),
      'portal_type#intersection':
      (0.00020000000000000001, 1, False),
      'show_inactive':
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
      (0.0073000000000000001, 1, True),
      'effectiveRange#intersection':
      (0.0038999999999999998, 1, False),
      'getCategories':
      (0.0073000000000000001, 1, True),
      'getCategories#intersection':
      (0.0060000000000000001, 1, False),
      'getCompatibility':
      (0.00029999999999999997, 1, True),
      'getCompatibility#intersection':
      (0.00029999999999999997, 1, False),
      'portal_type':
      (0.00080000000000000004, 1, True),
      'portal_type#intersection':
      (0.00069999999999999999, 1, False),
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
      (0.00029999999999999997, 1, True),
      'effectiveRange#intersection':
      (0.0001, 1, False),
      'getCategories':
      (0.0154, 1, True),
      'getCategories#intersection':
      (0.0025000000000000001, 1, False),
      'portal_type':
      (0.0033, 1, True),
      'portal_type#intersection':
      (0.0033, 1, False),
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
      (0.0073000000000000001, 1, True),
      'effectiveRange#intersection':
      (0.0038999999999999998, 1, False),
      'getCompatibility':
      (0.00080000000000000004, 1, True),
      'getCompatibility#intersection':
      (0.00080000000000000004, 1, False),
      'portal_type':
      (0.00029999999999999997, 1, True),
      'portal_type#intersection':
      (0.00020000000000000001, 1, False),
      'sort_on':
      (0.0, 0, False),
      'sort_order':
      (0.0, 0, False),
    },
    ('SearchableText', 'allowedRolesAndUsers', 'effectiveRange', 'path', 'portal_type', 'show_inactive', 'sort_on', 'sort_order'): {
      'SearchableText':
      (0.010999999999999999, 1, False),
      'SearchableText#intersection':
      (0.0, 1, False),
      'allowedRolesAndUsers':
      (0.0040000000000000001, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0038999999999999998, 1, False),
      'effectiveRange':
      (0.0016000000000000001, 1, True),
      'effectiveRange#intersection':
      (0.00080000000000000004, 1, False),
      'path':
      (0.0077000000000000002, 1, False),
      'path#intersection':
      (0.0014, 1, False),
      'portal_type':
      (0.0020999999999999999, 1, True),
      'portal_type#intersection':
      (0.00059999999999999995, 1, False),
      'show_inactive':
      (0.0, 0, False),
      'sort_on':
      (0.0, 0, False),
      'sort_order':
      (0.0, 0, False),
    },
    ('SearchableText', 'allowedRolesAndUsers', 'effectiveRange', 'path', 'portal_type', 'show_inactive', 'sort_order'): {
      'SearchableText':
      (0.012200000000000001, 1, False),
      'SearchableText#intersection':
      (0.0011000000000000001, 1, False),
      'allowedRolesAndUsers':
      (0.0035999999999999999, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0035000000000000001, 1, False),
      'effectiveRange':
      (0.0011999999999999999, 1, True),
      'effectiveRange#intersection':
      (0.00059999999999999995, 1, False),
      'path':
      (0.0063, 1, False),
      'path#intersection':
      (0.0, 1, False),
      'portal_type':
      (0.0020999999999999999, 1, True),
      'portal_type#intersection':
      (0.00050000000000000001, 1, False),
      'show_inactive':
      (0.0, 0, False),
      'sort_order':
      (0.0, 0, False),
    },
    ('SearchableText', 'allowedRolesAndUsers', 'effectiveRange', 'path', 'portal_type', 'sort_limit'): {
      'SearchableText':
      (0.0020999999999999999, 1, False),
      'SearchableText#intersection':
      (0.00069999999999999999, 1, False),
      'allowedRolesAndUsers':
      (0.0035000000000000001, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0033999999999999998, 1, False),
      'effectiveRange':
      (0.00029999999999999997, 1, True),
      'effectiveRange#intersection':
      (0.0001, 1, False),
      'path':
      (0.0067999999999999996, 1, False),
      'path#intersection':
      (0.0, 1, False),
      'portal_type':
      (0.0018, 1, True),
      'portal_type#intersection':
      (0.00020000000000000001, 1, False),
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
      (0.00020000000000000001, 1, True),
      'effectiveRange#intersection':
      (0.0001, 1, False),
      'portal_type':
      (0.0030999999999999999, 1, True),
      'portal_type#intersection':
      (0.0030000000000000001, 1, False),
      'sort_on':
      (0.0, 0, False),
      'sort_order':
      (0.0, 0, False),
    },
    ('Subject', 'Type', 'allowedRolesAndUsers', 'b_size', 'b_start', 'effectiveRange', 'sort_on'): {
      'Subject':
      (0.0012999999999999999, 1, True),
      'Subject#intersection':
      (0.0, 1, False),
      'Type':
      (0.0085000000000000006, 1, True),
      'Type#intersection':
      (0.0076, 1, False),
      'allowedRolesAndUsers':
      (0.0032000000000000002, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0032000000000000002, 1, False),
      'b_size':
      (0.0, 0, False),
      'b_start':
      (0.0, 0, False),
      'effectiveRange':
      (0.00020000000000000001, 1, True),
      'effectiveRange#intersection':
      (0.0, 1, False),
      'sort_on':
      (0.0, 0, False),
    },
    ('Subject', 'allowedRolesAndUsers', 'b_size', 'b_start', 'effectiveRange', 'path', 'portal_type', 'show_inactive'): {
      'Subject':
      (0.0022000000000000001, 1, True),
      'Subject#intersection':
      (0.00050000000000000001, 1, False),
      'allowedRolesAndUsers':
      (0.0025999999999999999, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0025000000000000001, 1, False),
      'b_size':
      (0.0, 0, False),
      'b_start':
      (0.0, 0, False),
      'effectiveRange':
      (0.00020000000000000001, 1, True),
      'effectiveRange#intersection':
      (0.0, 1, False),
      'path':
      (0.0067000000000000002, 1, False),
      'path#intersection':
      (0.0, 1, False),
      'portal_type':
      (0.00080000000000000004, 1, True),
      'portal_type#intersection':
      (0.0, 1, False),
      'show_inactive':
      (0.0, 0, False),
    },
    ('Subject', 'allowedRolesAndUsers', 'b_size', 'b_start', 'effectiveRange', 'path', 'portal_type', 'show_inactive', 'sort_on'): {
      'Subject':
      (0.0044000000000000003, 1, True),
      'Subject#intersection':
      (0.0030000000000000001, 1, False),
      'allowedRolesAndUsers':
      (0.0041000000000000003, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0040000000000000001, 1, False),
      'b_size':
      (0.0, 0, False),
      'b_start':
      (0.0, 0, False),
      'effectiveRange':
      (0.00020000000000000001, 1, True),
      'effectiveRange#intersection':
      (0.0, 1, False),
      'path':
      (0.0064000000000000003, 1, False),
      'path#intersection':
      (0.0, 1, False),
      'portal_type':
      (0.0018, 1, True),
      'portal_type#intersection':
      (0.00020000000000000001, 1, False),
      'show_inactive':
      (0.0, 0, False),
      'sort_on':
      (0.0, 0, False),
    },
    ('Subject', 'allowedRolesAndUsers', 'b_size', 'b_start', 'effectiveRange', 'path', 'portal_type', 'show_inactive', 'sort_on', 'sort_order'): {
      'Subject':
      (0.0015, 1, True),
      'Subject#intersection':
      (0.00050000000000000001, 1, False),
      'allowedRolesAndUsers':
      (0.0041000000000000003, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0041000000000000003, 1, False),
      'b_size':
      (0.0, 0, False),
      'b_start':
      (0.0, 0, False),
      'effectiveRange':
      (0.0001, 1, True),
      'effectiveRange#intersection':
      (0.0, 1, False),
      'path':
      (0.0064999999999999997, 1, False),
      'path#intersection':
      (0.0, 1, False),
      'portal_type':
      (0.00089999999999999998, 1, True),
      'portal_type#intersection':
      (0.0, 1, False),
      'show_inactive':
      (0.0, 0, False),
      'sort_on':
      (0.0, 0, False),
      'sort_order':
      (0.0, 0, False),
    },
    ('Subject', 'allowedRolesAndUsers', 'effectiveRange', 'path', 'portal_type', 'show_inactive', 'sort_order'): {
      'Subject':
      (0.021700000000000001, 1, True),
      'Subject#intersection':
      (0.00050000000000000001, 1, False),
      'allowedRolesAndUsers':
      (0.0023999999999999998, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0023999999999999998, 1, False),
      'effectiveRange':
      (0.0001, 1, True),
      'effectiveRange#intersection':
      (0.0, 1, False),
      'path':
      (0.0061999999999999998, 1, False),
      'path#intersection':
      (0.0, 1, False),
      'portal_type':
      (0.00069999999999999999, 1, True),
      'portal_type#intersection':
      (0.0, 1, False),
      'show_inactive':
      (0.0, 0, False),
      'sort_order':
      (0.0, 0, False),
    },
    ('Type', 'allowedRolesAndUsers', 'b_size', 'b_start', 'effectiveRange', 'path', 'sort_on', 'sort_order'): {
      'Type':
      (0.0097999999999999997, 1, True),
      'Type#intersection':
      (0.0088999999999999999, 1, False),
      'allowedRolesAndUsers':
      (0.0032000000000000002, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0030999999999999999, 1, False),
      'b_size':
      (0.0, 0, False),
      'b_start':
      (0.0, 0, False),
      'effectiveRange':
      (0.00020000000000000001, 1, True),
      'effectiveRange#intersection':
      (0.0, 1, False),
      'path':
      (0.085500000000000007, 1, False),
      'path#intersection':
      (0.0, 1, False),
      'sort_on':
      (0.0, 0, False),
      'sort_order':
      (0.0, 0, False),
    },
    ('Type', 'allowedRolesAndUsers', 'b_size', 'b_start', 'effectiveRange', 'review_state', 'sort_on', 'start'): {
      'Type':
      (0.0001, 1, True),
      'Type#intersection':
      (0.0, 1, False),
      'allowedRolesAndUsers':
      (0.0033, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0032000000000000002, 1, False),
      'b_size':
      (0.0, 0, False),
      'b_start':
      (0.0, 0, False),
      'effectiveRange':
      (0.00020000000000000001, 1, True),
      'effectiveRange#intersection':
      (0.0001, 1, False),
      'review_state':
      (0.0012999999999999999, 1, True),
      'review_state#intersection':
      (0.0011999999999999999, 1, False),
      'sort_on':
      (0.0, 0, False),
      'start':
      (0.0047000000000000002, 1, True),
      'start#intersection':
      (0.0, 1, False),
    },
    ('Type', 'allowedRolesAndUsers', 'effectiveRange', 'review_state', 'sort_on'): {
      'Type':
      (0.0011000000000000001, 1, True),
      'Type#intersection':
      (0.0, 1, False),
      'allowedRolesAndUsers':
      (0.0057000000000000002, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0055999999999999999, 1, False),
      'effectiveRange':
      (0.0001, 1, True),
      'effectiveRange#intersection':
      (0.0, 1, False),
      'review_state':
      (0.0020999999999999999, 1, True),
      'review_state#intersection':
      (0.0012999999999999999, 1, False),
      'sort_on':
      (0.0, 0, False),
    },
    ('UID', 'allowedRolesAndUsers', 'effectiveRange'): {
      'UID':
      (0.0023, 1, True),
      'UID#intersection':
      (0.0, 1, False),
      'allowedRolesAndUsers':
      (0.00059999999999999995, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.00059999999999999995, 1, False),
      'effectiveRange':
      (0.0001, 1, True),
      'effectiveRange#intersection':
      (0.0, 1, False),
    },
    ('allowedRolesAndUsers', 'effectiveRange', 'end', 'portal_type', 'review_state', 'sort_on'): {
      'allowedRolesAndUsers':
      (0.0001, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0, 1, False),
      'effectiveRange':
      (0.0001, 1, True),
      'effectiveRange#intersection':
      (0.0, 1, False),
      'end':
      (0.00029999999999999997, 1, True),
      'end#intersection':
      (0.0, 1, False),
      'portal_type':
      (0.0033, 1, True),
      'portal_type#intersection':
      (0.0032000000000000002, 1, False),
      'review_state':
      (0.0011999999999999999, 1, True),
      'review_state#intersection':
      (0.0011000000000000001, 1, False),
      'sort_on':
      (0.0, 0, False),
    },
    ('allowedRolesAndUsers', 'effectiveRange', 'getArea', 'path', 'portal_type', 'review_state', 'sort_on', 'sort_order'): {
      'allowedRolesAndUsers':
      (0.00069999999999999999, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.00059999999999999995, 1, False),
      'effectiveRange':
      (0.0001, 1, True),
      'effectiveRange#intersection':
      (0.0, 1, False),
      'getArea':
      (0.0001, 1, True),
      'getArea#intersection':
      (0.0, 1, False),
      'path':
      (0.0023, 1, False),
      'path#intersection':
      (0.0, 1, False),
      'portal_type':
      (0.0001, 1, True),
      'portal_type#intersection':
      (0.0001, 1, False),
      'review_state':
      (0.0001, 1, True),
      'review_state#intersection':
      (0.0, 1, False),
      'sort_on':
      (0.0, 0, False),
      'sort_order':
      (0.0, 0, False),
    },
    ('allowedRolesAndUsers', 'effectiveRange', 'getCategories', 'path', 'portal_type', 'sort_on', 'sort_order'): {
      'allowedRolesAndUsers':
      (0.0054999999999999997, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0054000000000000003, 1, False),
      'effectiveRange':
      (0.0016000000000000001, 1, True),
      'effectiveRange#intersection':
      (0.001, 1, False),
      'getCategories':
      (0.011599999999999999, 1, True),
      'getCategories#intersection':
      (0.010200000000000001, 1, False),
      'path':
      (0.00020000000000000001, 1, False),
      'path#intersection':
      (0.0, 1, False),
      'portal_type':
      (0.00029999999999999997, 1, True),
      'portal_type#intersection':
      (0.00020000000000000001, 1, False),
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
      (0.0001, 1, True),
      'effectiveRange#intersection':
      (0.0, 1, False),
      'getCountry':
      (0.0070000000000000001, 1, True),
      'getCountry#intersection':
      (0.0053, 1, False),
      'meta_type':
      (0.0001, 1, True),
      'meta_type#intersection':
      (0.0001, 1, False),
      'sort_on':
      (0.0, 0, False),
    },
    ('allowedRolesAndUsers', 'effectiveRange', 'getSections', 'path', 'portal_type'): {
      'allowedRolesAndUsers':
      (0.0091000000000000004, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0091000000000000004, 1, False),
      'effectiveRange':
      (0.00029999999999999997, 1, True),
      'effectiveRange#intersection':
      (0.0001, 1, False),
      'getSections':
      (0.0025000000000000001, 1, True),
      'getSections#intersection':
      (0.0016000000000000001, 1, False),
      'path':
      (0.00020000000000000001, 1, False),
      'path#intersection':
      (0.0, 1, False),
      'portal_type':
      (0.00020000000000000001, 1, True),
      'portal_type#intersection':
      (0.0, 1, False),
    },
    ('allowedRolesAndUsers', 'effectiveRange', 'is_default_page', 'is_folderish', 'path', 'portal_type', 'review_state', 'sort_on', 'sort_order'): {
      'allowedRolesAndUsers':
      (0.0033999999999999998, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0033, 1, False),
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
      (0.00040000000000000002, 1, True),
      'portal_type#intersection':
      (0.0, 1, False),
      'review_state':
      (0.0011999999999999999, 1, True),
      'review_state#intersection':
      (0.0011999999999999999, 1, False),
      'sort_on':
      (0.0, 0, False),
      'sort_order':
      (0.0, 0, False),
    },
    ('allowedRolesAndUsers', 'effectiveRange', 'is_default_page', 'object_provides', 'path', 'sort_on'): {
      'allowedRolesAndUsers':
      (0.00059999999999999995, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.00050000000000000001, 1, False),
      'effectiveRange':
      (0.00020000000000000001, 1, True),
      'effectiveRange#intersection':
      (0.0, 1, False),
      'is_default_page':
      (0.0001, 1, True),
      'is_default_page#intersection':
      (0.0, 1, False),
      'object_provides':
      (0.00020000000000000001, 1, True),
      'object_provides#intersection':
      (0.0001, 1, False),
      'path':
      (0.00050000000000000001, 1, False),
      'path#intersection':
      (0.0, 1, False),
      'sort_on':
      (0.0, 0, False),
    },
    ('allowedRolesAndUsers', 'effectiveRange', 'is_default_page', 'path', 'portal_type', 'review_state', 'sort_on', 'sort_order'): {
      'allowedRolesAndUsers':
      (0.0033, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0032000000000000002, 1, False),
      'effectiveRange':
      (0.00040000000000000002, 1, True),
      'effectiveRange#intersection':
      (0.0, 1, False),
      'is_default_page':
      (0.0001, 1, True),
      'is_default_page#intersection':
      (0.0, 1, False),
      'path':
      (0.00020000000000000001, 1, False),
      'path#intersection':
      (0.0, 1, False),
      'portal_type':
      (0.00040000000000000002, 1, True),
      'portal_type#intersection':
      (0.0, 1, False),
      'review_state':
      (0.0011999999999999999, 1, True),
      'review_state#intersection':
      (0.0011000000000000001, 1, False),
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
      (0.0077000000000000002, 1, True),
      'effectiveRange#intersection':
      (0.0040000000000000001, 1, False),
      'meta_type':
      (0.036600000000000001, 1, True),
      'meta_type#intersection':
      (0.035200000000000002, 1, False),
      'sort_on':
      (0.0, 0, False),
    },
    ('allowedRolesAndUsers', 'effectiveRange', 'object_provides', 'path', 'show_inactive', 'sort_on'): {
      'allowedRolesAndUsers':
      (0.0019, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0019, 1, False),
      'effectiveRange':
      (0.0001, 1, True),
      'effectiveRange#intersection':
      (0.0, 1, False),
      'object_provides':
      (0.00029999999999999997, 1, True),
      'object_provides#intersection':
      (0.00020000000000000001, 1, False),
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
      (0.0035000000000000001, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0033999999999999998, 1, False),
      'effectiveRange':
      (0.00029999999999999997, 1, True),
      'effectiveRange#intersection':
      (0.0001, 1, False),
      'path':
      (0.0809, 1, False),
      'path#intersection':
      (0.0, 1, False),
    },
    ('allowedRolesAndUsers', 'effectiveRange', 'path', 'portal_type'): {
      'allowedRolesAndUsers':
      (0.0022000000000000001, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0020999999999999999, 1, False),
      'effectiveRange':
      (0.0001, 1, True),
      'effectiveRange#intersection':
      (0.0, 1, False),
      'path':
      (0.002, 1, False),
      'path#intersection':
      (0.0, 1, False),
      'portal_type':
      (0.00050000000000000001, 1, True),
      'portal_type#intersection':
      (0.00040000000000000002, 1, False),
    },
    ('allowedRolesAndUsers', 'effectiveRange', 'path', 'portal_type', 'review_state'): {
      'allowedRolesAndUsers':
      (0.00050000000000000001, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.00040000000000000002, 1, False),
      'effectiveRange':
      (0.0001, 1, True),
      'effectiveRange#intersection':
      (0.0, 1, False),
      'path':
      (0.00040000000000000002, 1, False),
      'path#intersection':
      (0.0, 1, False),
      'portal_type':
      (0.0001, 1, True),
      'portal_type#intersection':
      (0.0, 1, False),
      'review_state':
      (0.0001, 1, True),
      'review_state#intersection':
      (0.0, 1, False),
    },
    ('allowedRolesAndUsers', 'effectiveRange', 'path', 'portal_type', 'review_state', 'show_inactive', 'sort_on', 'sort_order'): {
      'allowedRolesAndUsers':
      (0.0030000000000000001, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0028999999999999998, 1, False),
      'effectiveRange':
      (0.00040000000000000002, 1, True),
      'effectiveRange#intersection':
      (0.0, 1, False),
      'path':
      (0.0041000000000000003, 1, False),
      'path#intersection':
      (0.0, 1, False),
      'portal_type':
      (0.00059999999999999995, 1, True),
      'portal_type#intersection':
      (0.00059999999999999995, 1, False),
      'review_state':
      (0.001, 1, True),
      'review_state#intersection':
      (0.00089999999999999998, 1, False),
      'show_inactive':
      (0.0, 0, False),
      'sort_on':
      (0.0, 0, False),
      'sort_order':
      (0.0, 0, False),
    },
    ('allowedRolesAndUsers', 'effectiveRange', 'path', 'portal_type', 'review_state', 'sort_on', 'sort_order'): {
      'allowedRolesAndUsers':
      (0.0022000000000000001, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0022000000000000001, 1, False),
      'effectiveRange':
      (0.0001, 1, True),
      'effectiveRange#intersection':
      (0.0, 1, False),
      'path':
      (0.0030000000000000001, 1, False),
      'path#intersection':
      (0.0, 1, False),
      'portal_type':
      (0.00050000000000000001, 1, True),
      'portal_type#intersection':
      (0.00040000000000000002, 1, False),
      'review_state':
      (0.00029999999999999997, 1, True),
      'review_state#intersection':
      (0.00029999999999999997, 1, False),
      'sort_on':
      (0.0, 0, False),
      'sort_order':
      (0.0, 0, False),
    },
    ('allowedRolesAndUsers', 'effectiveRange', 'path', 'portal_type', 'show_inactive', 'sort_on'): {
      'allowedRolesAndUsers':
      (0.0001, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0, 1, False),
      'effectiveRange':
      (0.0, 0, False),
      'path':
      (0.00059999999999999995, 1, False),
      'path#intersection':
      (0.00050000000000000001, 1, False),
      'portal_type':
      (0.0001, 1, True),
      'portal_type#intersection':
      (0.0, 1, False),
      'show_inactive':
      (0.0, 0, False),
      'sort_on':
      (0.0, 0, False),
    },
    ('allowedRolesAndUsers', 'effectiveRange', 'path', 'portal_type', 'show_inactive', 'sort_on', 'sort_order'): {
      'allowedRolesAndUsers':
      (0.0030999999999999999, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0030000000000000001, 1, False),
      'effectiveRange':
      (0.00040000000000000002, 1, True),
      'effectiveRange#intersection':
      (0.0, 1, False),
      'path':
      (0.106, 1, False),
      'path#intersection':
      (0.0, 1, False),
      'portal_type':
      (0.00069999999999999999, 1, True),
      'portal_type#intersection':
      (0.00059999999999999995, 1, False),
      'show_inactive':
      (0.0, 0, False),
      'sort_on':
      (0.0, 0, False),
      'sort_order':
      (0.0, 0, False),
    },
    ('allowedRolesAndUsers', 'effectiveRange', 'path', 'portal_type', 'sort_on'): {
      'allowedRolesAndUsers':
      (0.00069999999999999999, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.00059999999999999995, 1, False),
      'effectiveRange':
      (0.0001, 1, True),
      'effectiveRange#intersection':
      (0.0, 1, False),
      'path':
      (0.00040000000000000002, 1, False),
      'path#intersection':
      (0.0, 1, False),
      'portal_type':
      (0.0001, 1, True),
      'portal_type#intersection':
      (0.0001, 1, False),
      'sort_on':
      (0.0, 0, False),
    },
    ('allowedRolesAndUsers', 'effectiveRange', 'path', 'portal_type', 'sort_on', 'sort_order'): {
      'allowedRolesAndUsers':
      (0.0020999999999999999, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0020999999999999999, 1, False),
      'effectiveRange':
      (0.0001, 1, True),
      'effectiveRange#intersection':
      (0.0, 1, False),
      'path':
      (0.0028999999999999998, 1, False),
      'path#intersection':
      (0.0, 1, False),
      'portal_type':
      (0.00050000000000000001, 1, True),
      'portal_type#intersection':
      (0.00040000000000000002, 1, False),
      'sort_on':
      (0.0, 0, False),
      'sort_order':
      (0.0, 0, False),
    },
    ('allowedRolesAndUsers', 'effectiveRange', 'path', 'show_inactive', 'sort_on'): {
      'allowedRolesAndUsers':
      (0.0023999999999999998, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0023999999999999998, 1, False),
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
      (0.0041000000000000003, 1, True),
      'allowedRolesAndUsers#intersection':
      (0.0040000000000000001, 1, False),
      'effectiveRange':
      (0.0025000000000000001, 1, True),
      'effectiveRange#intersection':
      (0.0015, 1, False),
      'path':
      (0.0064000000000000003, 1, False),
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
      (0.00020000000000000001, 1, True),
      'effectiveRange#intersection':
      (0.0, 1, False),
      'portal_type':
      (0.0032000000000000002, 1, True),
      'portal_type#intersection':
      (0.0032000000000000002, 1, False),
      'review_state':
      (0.0011999999999999999, 1, True),
      'review_state#intersection':
      (0.0011000000000000001, 1, False),
      'sort_on':
      (0.0, 0, False),
      'sort_order':
      (0.0, 0, False),
    },
    ('path',): {
      'path':
      (0.0011999999999999999, 1, False),
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
      (0.0001, 1, True),
      'relationship#intersection':
      (0.0, 1, False),
      'targetUID':
      (0.0082000000000000007, 1, True),
      'targetUID#intersection':
      (0.0082000000000000007, 1, False),
    },
  },
  ('', 'plone.org', 'uid_catalog'): {
    'VALUE_INDEXES': frozenset([]),
    ('UID', 'sort_on'): {
    },
  },
}
