import subprocess
import os

services = (
    "AppVClient",
    "BDESVC",
    "diagnosticshub.standardcollector.service",
    "DiagTrack",
    "DialogBlockingService",
    "fhsvc",
    "GameInputSvc",
    "HvHost",
    "LanmanServer",
    "LanmanWorkstation",
    "lfsvc",
    "LPlatSvc",
    "LxpSvc",
    "MapsBroker",
    "MsKeyboardFilter",
    "NetTcpPortSharing",
    "PhoneSvc",
    "PrintNotify",
    "RemoteAccess",
    "RemoteRegistry",
    "RetailDemo",
    "SCardSvr",
    "ScDeviceEnum",
    "SCPolicySvc",
    "SDRSVC",
    "SEMgrSvc",
    "SensorDataService",
    "SensorService",
    "SensrSvc",
    "SessionEnv",
    "shpamsvc",
    "Spooler",
    "ssh-agent",
    "SysMain",
    "TapiSrv",
    "TermService",
    "Themes",
    "tzautoupdate",
    "UevAgentService",
    "UmRdpService",
    "vmicguestinterface",
    "vmicheartbeat",
    "vmickvpexchange",
    "vmicrdv",
    "vmicshutdown",
    "vmictimesync",
    "vmicvmsession",
    "vmicvss",
    "wbengine",
    "WbioSrvc",
    "wisvc",
    "wlidsvc",
    "WMPNetworkSvc",
    "workfolderssvc",
    "WSearch",
    "XblAuthManager",
    "XblGameSave",
    "XboxGipSvc",
    "XboxNetApiSvc",
    "BcastDVRUserService",
    "cbdhsvc",
    "OneSyncSvc",
    "PimIndexMaintenanceSvc",
    "UnistoreSvc",
)


def check_service_exists(service_name: str) -> bool:
    result = subprocess.run(
        ["sc", "query", service_name], capture_output=True, text=True
    )

    # Nếu returncode == 0 tức là dịch vụ tồn tại
    return result.returncode == 0


def change_status_to_disable(service_name: str):
    try:
        subprocess.run(
            ["sc", "config", service_name, "start=", "disabled"],
            check=True,
            stdout=subprocess.DEVNULL,  # Không in thông báo khi thành công
            stderr=subprocess.PIPE,  # Bắt lỗi nếu có
            text=True,  # Để nhận kết quả dưới dạng chuỗi thay vì bytes
        )
        print(f"{service_name} has been disabled successfully")
    except subprocess.CalledProcessError as err:
        # print(f"Failed to disable {service_name}: {err.stderr.strip()}")
        print(f"Failed to disable {service_name}: {err}")


if __name__ == "__main__":
    try:
        for service in services:
            if check_service_exists(service):
                change_status_to_disable(service)
            else:
                print(f"Service {service} does not exist")

    except Exception as e:
        print(f"Exception: {e}")
    finally:
        os.system("pause")
