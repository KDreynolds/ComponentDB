#!/usr/bin/env python

#
# Implementation for user info controller.
#

#######################################################################

from cdb.common.objects.cdbObject import CdbObject
from cdb.common.objects.cdbObjectManager import CdbObjectManager
from cdb.common.db.api.userDbApi import UserDbApi

#######################################################################

class UserInfoControllerImpl(CdbObjectManager):
    """ User info controller implementation class. """

    def __init__(self):
        CdbObjectManager.__init__(self)
        self.userDbApi = UserDbApi()

    def getUserInfos(self):
        return self.userDbApi.getUsers()

    def getUserById(self, id):
        return self.userDbApi.getUserById(id)

    def getUserByUsername(self, username):
        return self.userDbApi.getUserByUsername(username)

