from setuptools import setup, find_packages
import os.path

version = '1.4'

test_require = ['plone.app.testing']


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
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        'Products.Carousel',
        'Products.ExternalStorage',
        'Products.FoundationMember',
        'Products.MemcachedManager',
        'Products.PloneFormGen',
        'Products.PloneHelpCenter',
        'Products.PloneKeywordManager',
        'Products.PloneSoftwareCenter',
        'Products.PloneServicesCenter',
        'Products.Poi',
        'Products.RedirectionTool',
        'Products.TinyMCE',
        'Products.contentmigration',
        'collective.contentrules.mailtogroup',
        'collective.contentrules.mailtolocalrole',
        'collective.psc.blobstorage',
        'collective.psc.externalstorage',
        'collective.psc.mirroring',
        'collective.recaptcha',
        'plone.app.caching',
        'plone.app.jquerytools',
        'plone.memoize',
        'ploneorg.kudobounty',
        'python-memcached',
        'roman',
        'zc.beforestorage',
        'zope.interface',
        'zope.structuredtext',
      ],
      test_require=test_require,
      extras_require={'test': test_require},
      )
