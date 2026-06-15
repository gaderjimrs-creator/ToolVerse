import psutil
import os


class MySystemTools:
    def __init__(self):
        pass

    def get_os_name(self):
        return os.name

    def get_current_working_directory(self):
        return os.getcwd()

    def list_directory_contents(self, path='.'):
        return os.listdir(path)

    def create_directory(self, path):
        os.makedirs(path, exist_ok=True)

    def remove_directory(self, path):
        os.rmdir(path)

    def get_environment_variable(self, var_name):
        return os.environ.get(var_name)

    def set_environment_variable(self, var_name, value):
        os.environ[var_name] = value

    def delete_environment_variable(self, var_name):
        if var_name in os.environ:
            del os.environ[var_name]
    
    def get_Python_version(self):
        import sys
        return sys.version
    
    def get_current_directory(self):
        return os.getcwd()
    
    def change_directory(self, path):
        os.chdir(path)
    
    def get_file_permissions(self, file_path):
        import stat
        if os.path.exists(file_path):
            permissions = stat.filemode(os.stat(file_path).st_mode)
            return permissions
        else:
            return "File does not exist"
    
    def set_file_permissions(self, file_path, mode):
        import os
        if os.path.exists(file_path):
            os.chmod(file_path, mode)
        else:
            return "File does not exist"
    
    def get_system_info(self):
        import platform
        return {
            "system": platform.system(),
            "node": platform.node(),
            "release": platform.release(),
            "version": platform.version(),
            "machine": platform.machine(),
            "processor": platform.processor()
        }
    
    def get_environment_variables(self):
        return dict(os.environ)
    
    def get_process_id(self):
        import os
        return os.getpid()
    
    def get_parent_process_id(self):
        import os
        return os.getppid()
    
    def get_user_id(self):
        import os
        return os.getuid() if hasattr(os, 'getuid') else None
    
    def get_group_id(self):
        import os
        return os.getgid() if hasattr(os, 'getgid') else None
    
    def get_current_user(self):
        import getpass
        return getpass.getuser()
    
    def get_home_directory(self):
        return os.path.expanduser("~")
    
    def get_temp_directory(self):
        import tempfile
        return tempfile.gettempdir()
    
    def get_current_timestamp(self):
        import time
        return time.time()
    
    def get_current_datetime(self):
        from datetime import datetime
        return datetime.now()
    
    def get_system_uptime(self):
        import time
        if hasattr(time, 'monotonic'):
            return time.monotonic()
        else:
            return "System uptime not available"
    
    def get_cpu_count(self):
        import os
        return os.cpu_count()
    
    def get_memory_info(self):
        import psutil
        mem = psutil.virtual_memory()
        return {
            "total": mem.total,
            "available": mem.available,
            "used": mem.used,
            "free": mem.free
        }
    
    def get_disk_usage(self, path='/'):
        import shutil
        total, used, free = shutil.disk_usage(path)
        return {
            "total": total,
            "used": used,
            "free": free
        }
    
    def get_network_info(self):
        net_if_addrs = psutil.net_if_addrs()
        net_if_stats = psutil.net_if_stats()
        network_info = {}
        for interface, addrs in net_if_addrs.items():
            network_info[interface] = {
                "addresses": [addr.address for addr in addrs],
                "is_up": net_if_stats[interface].isup if interface in net_if_stats else None
            }
        return network_info
    
    def get_system_load(self):
        import os
        if hasattr(os, 'getloadavg'):
            return os.getloadavg()
        else:
            return "System load not available"
    
