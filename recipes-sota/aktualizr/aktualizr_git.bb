require aktualizr.inc

PV = "1.0+git${SRCPV}"
PR = "8"

# for garage-sign archive
GARAGE_SIGN_PV = "0.7.0-33-g214dfb1"
SRC_URI[md5sum] = "66ffe8dcd61d4c15646e1c4b7dde7401"
SRC_URI[sha256sum] = "7a7193ddf7e1a33ea60fbb20f98318a8bd78c325dab391d8c4ebd644a738abdc"

SRCREV = "d13ff1ceeca2694b982287740aca8f58edad514d"
BRANCH ?= "master"

S = "${WORKDIR}/git"
