from setuptools import setup, find_packages
import os.path

version = '1.2'

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
        'Products.ExternalStorage',
        'Products.FoundationMember',
        'Products.MemcachedManager',
        'Products.PloneFormGen',
        'Products.PloneHelpCenter',
        'Products.PloneKeywordManager',
        'Products.PloneSoftwareCenter',
        'Products.Poi',
        'Products.RedirectionTool',
        'Products.TinyMCE',
        'Products.contentmigration',
        'collective.psc.externalstorage',
        'collective.psc.mirroring',
        'collective.recaptcha',
        'plone.app.jquerytools',
        'plone.memoize',
        'python-memcached',
        'zc.beforestorage',
        'zope.interface',
        'zope.structuredtext',
      ],
      )

