from Products.Archetypes.Extensions.utils import install_subskin
from Products.PloneOrg.config import *
from StringIO import StringIO

def install(self):
	out=StringIO()
	install_subskin(self, out, GLOBALS)
	return out.getvalue()
