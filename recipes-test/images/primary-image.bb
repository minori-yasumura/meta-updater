include recipes-core/images/core-image-minimal.bb

SUMMARY = "A minimal Uptane Primary image running aktualizr, for testing with a Linux secondary"

LICENSE = "MIT"

IMAGE_INSTALL_remove = " \
			virtual/network-configuration \
                        "

IMAGE_INSTALL_append = " \
                        primary-network-config \
                       "

# vim:set ts=4 sw=4 sts=4 expandtab:
