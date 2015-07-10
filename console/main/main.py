from sys import platform

from LinuxCloudServiceRegistry import LinuxCloudServiceRegistry
from ProgramCannonStartError import ProgramCannotStartError
from WindowsCloudServiceRegistry import WindowsCloudServiceRegistry

if platform.startswith('win'):
    cloud_service_registry = WindowsCloudServiceRegistry(
        None,
        None,
        None,
        None,
        None)
elif platform.startswith('linux'):
    cloud_service_registry = LinuxCloudServiceRegistry(
        None,
        None,
        None,
        None,
        None)
else:
    raise ProgramCannotStartError('Unsupported operating system.')

cloud_service_registry.say_hello()
