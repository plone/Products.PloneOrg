import re
from DateTime import DateTime
from zope.cachedescriptors.property import Lazy as lazy_property
from plone.app.layout.viewlets.common import ViewletBase


VERSION_RE = re.compile(r'([\d\.x]+)')
CURRENT_VERSION = 4
OLDEST_SUPPORTED_VERSION = 3


class OutOfDateWarning(ViewletBase):

	@lazy_property
	def daysago(self):
		return int(DateTime() - DateTime(self.context.ModificationDate()))

	@lazy_property
	def most_recent_version_number(self):
		versions = self.context.getVersions()
		max_version = 0
		for version in versions:
			m = VERSION_RE.search(version)
			if m:
				version_number = float(m.group(1).rstrip('.x'))
				if version_number > max_version:
					max_version = version_number
		return max_version

	def most_recent_version(self):
		versions = self.context.getVersions()
		max_version = 0
		for version in versions:
			m = VERSION_RE.search(version)
			if m:
				version_number = float(m.group(1).rstrip('.x'))
				if version_number > max_version:
					max_version = version
		return max_version

	def is_unknown(self):
		if self.most_recent_version_number:
			return False
		return True

	def is_current(self):
		if self.most_recent_version_number >= CURRENT_VERSION:
			return True
		return False

	def is_old(self):
		version_num = self.most_recent_version_number
		if OLDEST_SUPPORTED_VERSION <= version_num and version_num < CURRENT_VERSION :
			return True
		return False

	def is_unsupported(self):
		version_num = self.most_recent_version_number
		if version_num > 0 and self.most_recent_version_number < OLDEST_SUPPORTED_VERSION:
			return True
		return False
