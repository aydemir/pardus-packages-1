#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import pythonmodules


WorkDir = "terminator-" + get.srcVERSION()


def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.dodoc("COPYING", "INSTALL", "README", "ChangeLog")
