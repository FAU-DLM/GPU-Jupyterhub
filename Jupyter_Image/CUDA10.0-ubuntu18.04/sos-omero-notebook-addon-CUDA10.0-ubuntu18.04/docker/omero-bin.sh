#!/bin/bash
source activate python2
exec /opt/omero/OMERO.server/bin/omero "$@"
