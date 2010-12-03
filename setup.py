from setuptools import setup, find_packages


def read(input):
    return open(input, 'rb').read()


setup(name='Products.PloneOrg',
      version='1.4',
      description="Plone.org site policy package.",
      long_description=read('README.txt') + read('docs/DEVELOPER.txt') +
            read('docs/HISTORY.txt'),
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Plone Admins',
      author_email='admins@plone.org',
      url='http://svn.plone.org/svn/plone/Products.PloneOrg',
      license='GPL',
      packages=find_packages(),
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
        'collective.contentrules.mailtogroup',
        'collective.contentrules.mailtolocalrole',
        'collective.psc.externalstorage',
        'collective.psc.mirroring',
        'collective.recaptcha',
        'collective.xdv',
        'plone.app.jquerytools',
        'plone.memoize',
        'python-memcached',
        'zc.beforestorage',
        'zope.interface',
        'zope.structuredtext',
      ],
      )
