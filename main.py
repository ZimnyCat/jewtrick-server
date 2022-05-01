from mcstatus import MinecraftServer
from time import sleep

latest_player_count = 0 # prevents false positives

while True:
    try:
        player_count = MinecraftServer.lookup("2b2t.org").status().players.online
        print(player_count)
        if 100 > player_count > 30 and latest_player_count < player_count:
            status = "2" # join
            jew_online = open("jew_online.html", "w")
            jew_online.write(str(player_count)) # writes latest OK player count for jew trick client
            jew_online.close()
        else:
            status = "1" # dont join, player count is too high/low
        latest_player_count = player_count
    except:
        status = "0" # dont join, 2b is down
        latest_player_count = 0
    jewtrickstatus = open("jewtrickstatus.html", "w")
    jewtrickstatus.write(status) # writes status
    jewtrickstatus.close()
    sleep(2)

