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
          'Products.AddRemoveWidget',
          'Products.ArchAddOn',
          'Products.CacheSetup',
          'Products.DataGridField',
          'Products.ExternalStorage',
          'Products.FoundationMember',
          'Products.PloneHelpCenter',
          'Products.PloneSoftwareCenter',
          'Products.Poi',
          'Products.RedirectionTool',
          'Products.contentmigration',
          'collective.psc.externalstorage',
          'collective.psc.blobstorage',
          'collective.psc.mirroring',
          'plone.intelligenttext',
          'plone.app.blob',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )

