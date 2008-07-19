from setuptools import setup, find_packages
import os.path

version = '1.0'

setup(name='Products.PloneOrg',
      version=version,
      description="Plone.org site policy package.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Plone Foundation',
      author_email='plone-developers@lists.sourceforge.net',
      url='http://svn.plone.org/svn/plone/Products.PloneOrg',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.PloneLDAP',
          'Products.CacheSetup >=1.2.jarn.3',
          'Products.ExternalStorage',   # For migration purposes only
          'Products.contentmigration',  # For migration purposes only?
          'Products.FoundationMember',
          'Products.PloneHelpCenter',
          'Products.PloneSoftwareCenter',
          'collective.psc.mirroring',
          'Products.Poi',
          'Products.RedirectionTool',
          'plone.memoize',
          'zope.interface',
          'Products.MemcachedManager',
          'python-memcached',
          'Products.GenericSetup >= 1.4.1',

# These do not have a release yet
#          'collective.psc.externalstorage',
#          'collective.psc.blobstorage',
      ],
      )

