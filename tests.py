##############################################################################
#
# Copyright (c) 2004 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.0 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Test hookup

$Id$
"""
import os
import unittest
import zope.event
from zope.component.tests import placelesssetup

def tearDown(test):
    placelesssetup.tearDown(test)
    zope.event.subscribers.pop()

def setUp(test):
    test.globs['this_directory'] = os.path.split(__file__)[0]
    placelesssetup.setUp(test)

def test_suite():
    from zope.testing import doctest
    suite = unittest.TestSuite()
    # suite.addTest(doctest.DocTestSuite())
    suite.addTest(doctest.DocFileSuite('README.txt', tearDown=tearDown,
                                       setUp=placelesssetup.setUp))
    suite.addTest(doctest.DocFileSuite(
        'xpdl.txt', tearDown=tearDown, setUp=setUp,
        optionflags=doctest.NORMALIZE_WHITESPACE))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')

