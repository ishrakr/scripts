from pydactyl import PterodactylClient
import time
import datetime

api = PterodactylClient('ptero-link', 'ptero-client-password')

uuid_list = ['','']

msg = "say [ALERT] The server will perform a scheduled reboot in 30 seconds."

for uuid in uuid_list :
    api.client.servers.send_console_command(server_id=uuid,cmd=msg)
    time.sleep(30)
    api.client.servers.send_power_action(server_id=uuid, signal="restart")