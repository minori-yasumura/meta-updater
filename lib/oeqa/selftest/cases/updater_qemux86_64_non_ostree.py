import updater_qemux86_64
from updater_qemux86_64 import GeneralTests, AktualizrToolsTests, SharedCredProvTests, \
    ManualControlTests, DeviceCredProvTests, DeviceCredProvHsmTests, ResourceControlTests, \
    DeviceCredProvHsmTests


updater_qemux86_64.UBOOT_ENABLE = 'no'


class GeneralTestsNonOSTRee(GeneralTests):
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


class ResourceControlTestsNonOSTree(ResourceControlTests):
    pass
