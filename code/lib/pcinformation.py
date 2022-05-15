import os
import socket


class PCInformation:

    @staticmethod
    def CMD_command(title, command):
        response = title + "\n"
        lines = os.popen(command)
        for line in lines:
            line.replace('\n\n', '\n')
            response += line
        return response

    def display_dns(self):
        return self.CMD_command(
            title="DNS Display Information",
            command="ipconfig /displaydns")

    def ip_config(self):
        return self.CMD_command(
            title="Information: IP REG_CONFIG_ALL /all",
            command="ipconfig /all")

    def system_info(self):
        return self.CMD_command(
            title="Information: System",
            command="systeminfo")

    def driver_info(self):
        return self.CMD_command(
            title="Information: Driver Information",
            command="DRIVERQUERY")

    def taks_list(self):
        return self.CMD_command(
            title="Information: Taks List",
            command="TASKLIST")

    def service_active(self):
        return self.CMD_command(
            title="Information: Services active",
            command="net start")

    def list_hard_diks (self):
        return self.CMD_command(
            title="Information List Hard Disk",
            command="fsutil fsinfo drives")

    def red_info(self):
        def internalIP():
            internal_ip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            internal_ip.connect(('google.com', 0))
            return internal_ip.getsockname()[0]

        response = "Information: RED Info\n"
        lines = os.popen('arp -a -N ' + internalIP())
        for line in lines:
            line.replace('\n\n', '\n')
            response += line
        return response
