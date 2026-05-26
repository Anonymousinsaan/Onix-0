import psutil
import os

def check_resource_usage():
    """
    Checks the current memory usage of the process.
    Designed to respect the 1GB RAM ceiling.
    """
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    mem_mb = mem_info.rss / (1024 * 1024)

    status = "OK"
    if mem_mb > 800:
        status = "CRITICAL"
    elif mem_mb > 500:
        status = "WARNING"

    return {
        "memory_usage_mb": round(mem_mb, 2),
        "status": status,
        "limit_mb": 1024
    }

if __name__ == "__main__":
    print(check_resource_usage())
