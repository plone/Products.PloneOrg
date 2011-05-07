

def step_1(context):
    wftool = context.portal_workflow
    if 'collector_issue_workflow' in wftool.objectIds():
        wftool.manage_delObjects(['collector_issue_workflow'])
