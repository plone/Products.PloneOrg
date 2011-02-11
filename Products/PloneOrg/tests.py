import unittest
import doctest

from Testing import ZopeTestCase

from Products.PloneOrg import testing

optionflags = (doctest.NORMALIZE_WHITESPACE |
               doctest.ELLIPSIS |
               doctest.REPORT_NDIFF)


def test_suite():
    install_suite = ZopeTestCase.FunctionalDocFileSuite(
        'team.txt', optionflags=optionflags)
    install_suite.layer = testing.PLONEORG_FUNCTIONAL_TESTING
    return unittest.TestSuite([install_suite])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
