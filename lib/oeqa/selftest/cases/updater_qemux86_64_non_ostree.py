import updater_qemux86_64
from updater_qemux86_64 import GeneralTests, AktualizrToolsTests, SharedCredProvTests


updater_qemux86_64.UBOOT_ENABLE = 'no'


class GeneralTestsNonOSTRee(GeneralTests):
    pass


class AktualizrToolsTestsNonOSTree(AktualizrToolsTests):
    pass


class SharedCredProvTestsnonOSTree(SharedCredProvTests):
    pass

