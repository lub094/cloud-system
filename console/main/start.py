from sys import platform

from core.main.linux_cloud_service_registry import LinuxCloudServiceRegistry
from console.main.program_cannot_start_error import ProgramCannotStartError
from core.main.windows_cloud_service_registry import WindowsCloudServiceRegistry
from core.main.binaries.binary import Binary

binary = Binary(None, None, None, None, None)

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
        None)
else:
    raise ProgramCannotStartError('Unsupported operating system.')

cloud_service_registry.say_hello()
