import updater_qemux86_64
from updater_qemux86_64 import GeneralTests, AktualizrToolsTests, SharedCredProvTests, \
    ManualControlTests, DeviceCredProvTests, DeviceCredProvHsmTests, ResourceControlTests, \
    DeviceCredProvHsmTests, IpSecondaryTests


updater_qemux86_64.UBOOT_ENABLE = 'no'


class GeneralTestsNonOSTree(GeneralTests):
    pass


class AktualizrToolsTestsNonOSTree(AktualizrToolsTests):
    pass


class SharedCredProvTestsNonOSTree(SharedCredProvTests):
    pass


class ManualControlTestsNonOSTree(ManualControlTests):
    pass


class DeviceCredProvTestsNonOSTree(DeviceCredProvTests):

    def setUpLocal(self):
        self.append_config('IMAGE_INSTALL_remove += " aktualizr-shared-prov"')
        self.append_config('IMAGE_INSTALL_append += " aktualizr-device-prov"')
        super().setUpLocal()


class DeviceCredProvHsmTestsNonOSTree(DeviceCredProvHsmTests):

    def setUpLocal(self):
        self.append_config('IMAGE_INSTALL_remove += " aktualizr-shared-prov"')
        self.append_config('IMAGE_INSTALL_append += " aktualizr-device-prov-hsm"')
        super().setUpLocal()


class IpSecondaryTestsNonOSTree(IpSecondaryTests):
    pass


class ResourceControlTestsNonOSTree(ResourceControlTests):
    pass
