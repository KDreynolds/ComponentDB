#!/usr/bin/env python

#######################################################################

import cherrypy
import json

from cdb.common.service.cdbController import CdbController
from cdb.common.objects.cdbObject import CdbObject
from cdb.common.exceptions.cdbException import CdbException
from cdb.common.exceptions.internalError import InternalError

from cdb.cdb_web_service.impl.componentControllerImpl import ComponentControllerImpl

#######################################################################

class ComponentController(CdbController):

    def __init__(self):
        CdbController.__init__(self)
        self.componentControllerImpl = ComponentControllerImpl()

    @cherrypy.expose
    def getComponents(self, **kwargs):
        try:
           response = '%s' % self.toJson(self.componentControllerImpl.getComponents())
        except CdbException, ex:
            self.logger.error('%s' % ex)
            self.handleException(ex)
            response = ex.getJsonRep()
        except Exception, ex:
            self.logger.error('%s' % ex)
            self.handleException(ex)
            response = InternalError(ex).getJsonRep()
        return self.formatJsonResponse(response)


