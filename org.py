#
# Organisation utilities
#

def fix_org(org):
    # try to group orgs by removing common additions
    org = org.lower().replace(" ", "")
    org = org.removeprefix('@')
    org = org.removesuffix('inc.')
    org = org.removesuffix('inc')
    org = org.removesuffix('official')
    return org