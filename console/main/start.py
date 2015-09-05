from sys import platform

from core.main.linux_cloud_service_registry import LinuxCloudServiceRegistry
from console.main.program_cannot_start_error import ProgramCannotStartError
from core.main.windows_cloud_service_registry import \
    WindowsCloudServiceRegistry
from console.main.cloud_system_app import CloudSystemApp
from core.main.persistence.ram_data_persistence_manager import \
    RamDataPersistenceManager

if platform.startswith('win'):
    cloud_service_registry = WindowsCloudServiceRegistry(
        RamDataPersistenceManager())
elif platform.startswith('linux'):
    cloud_service_registry = LinuxCloudServiceRegistry(
        None,
        None,
        None,
        None)
else:
    raise ProgramCannotStartError('Unsupported operating system.')


def run_program():
    cloud_system_app = CloudSystemApp(cloud_service_registry)
    cloud_system_app.run_interactive_mode()
