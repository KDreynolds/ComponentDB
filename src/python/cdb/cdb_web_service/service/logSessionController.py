#!/usr/bin/env python

"""
Copyright (c) UChicago Argonne, LLC. All rights reserved.
See LICENSE file.
"""

import cherrypy
from cdb.cdb_web_service.impl.logControllerImpl import LogControllerImpl
from cdb.common.exceptions.invalidRequest import InvalidRequest
from cdb.common.service.cdbSessionController import CdbSessionController
from cdb.common.utility.encoder import Encoder


class LogSessionController(CdbSessionController):

    def __init__(self):
        CdbSessionController.__init__(self)
        self.logControllerImpl = LogControllerImpl()

    @cherrypy.expose
    @CdbSessionController.require(CdbSessionController.isLoggedIn())
    @CdbSessionController.execute
    def addLogAttachment(self, logId, attachmentName, attachmentDescription=None, **kwargs):
        if not logId:
            raise InvalidRequest("Invalid logId provided")
        if not attachmentName:
            raise InvalidRequest("Invalid attachment name provided")

        attachmentName = Encoder.decode(attachmentName)
        attachmentDescription = Encoder.decode(attachmentDescription)
        cherrypyData = cherrypy.request.body

        logAttachmentAdded = self.logControllerImpl.addLogAttachment(logId, attachmentName, attachmentDescription, cherrypyData)

        response = logAttachmentAdded.getFullJsonRep()
        self.logger.debug('Returning log attachment info for log with id %s: %s' % (logId, response))
        return response

