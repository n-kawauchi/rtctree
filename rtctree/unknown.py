# -*- Python -*-
# -*- coding: utf-8 -*-

'''rtctree

Copyright (C) 2009-2010
    Geoffrey Biggs
    RT-Synthesis Research Group
    Intelligent Systems Research Institute,
    National Institute of Advanced Industrial Science and Technology (AIST),
    Japan
    All rights reserved.
Licensed under the Eclipse Public License -v 1.0 (EPL)
http://www.opensource.org/licenses/eclipse-1.0.txt

File: unknown.py

Object representing an unknown node in the tree.

'''

__version__ = '$Revision: $'
# $Source$


from rtctree.exceptions import *
from rtctree.node import TreeNode


##############################################################################
## Unknown node object

class Unknown(TreeNode):
    '''Node representing an unknown object on a name server.

    Unknown nodes can occur below name server and directory nodes. They
    cannot contain any children.

    '''
    def __init__(self, name, parent, obj):
        '''Constructor.

        @param name Name of this object (i.e. its entry in the path).
        @param parent The parent node of this node, if any.
        @param obj The CORBA object to wrap.

        '''
        super(Unknown, self).__init__(name, parent)
        self._obj = obj

    ###########################################################################
    # Node functionality

    @property
    def object(self):
        '''The LightweightRTObject this object wraps.'''
        return self._obj

    ###########################################################################
    # Internal API

    def _add_child(self):
        # Unknowns cannot contain children.
        raise CannotHoldChildrenError


# vim: tw=79

