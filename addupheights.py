def lookforplayers(player1,player2):
    flag = 0
    for pl in foundplayers:
        if (player1 == pl[0] and player2 == pl[1]) or (player2 == pl[0] and player1 == pl[1]):
            flag = 1
    return flag

foundplayers = []

def addupheights(x):
    import urllib, json
    url = "https://mach-eight.uc.r.appspot.com/"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    
    count = 0
    for playeri in data["values"]:
        suma = 0
        foundplayer = ""
        
        for playerj in data["values"]:
            suma = int(playeri["h_in"]) + int(playerj["h_in"])
            if suma == x and lookforplayers(playeri["first_name"] + " " + playeri["last_name"],playerj["first_name"] + " " + playerj["last_name"]) == 0:          
                foundplayers.append((playeri["first_name"] + " " + playeri["last_name"],playerj["first_name"] + " " + playerj["last_name"]))
                count += 1
                print(playeri["first_name"] + " " + playeri["last_name"] + " " + playerj["first_name"] + " " + playerj["last_name"])


    if count == 0:
        print("No matches found")

    return foundplayers

def mainfunction():
    try:
        number = int(input("Enter number:"))
        addupheights(number)
    except:
        print("You must enter a number")
