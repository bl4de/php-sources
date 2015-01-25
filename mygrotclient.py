import http.client
import json
import random
import sys
import time
import logging

log = logging.getLogger('grot-client')

SERVER = 'php-grot-public-mjaniszew.c9.io'

if __name__ == '__main__':
    token = sys.argv[1]  # your Access Token
    game = sys.argv[2]  # 0 (development mode), 1 (duel), 2 (contest)

    time.sleep(random.random())

    # connect to the game server
    client = http.client.HTTPConnection(SERVER, 80)
    client.connect()

    # block until the game starts
    client.request('GET', '/games/{}/board?token={}'.format(game, token))

    response = client.getresponse()
    data = json.loads(response.read().decode())
    
    
    def nextmove(b, x, y):
            maxpoints = 0
            points = 0
            # for row in b:
            #     print()
            #     for col in row:
            #         print (col['points'])
                        
            #             # print(col['y'], col['x'], col['points'])
            # print (maxpoints, x, y)
            return (x+1, y+1)

    def sendrequest(x,y):
        # make your move and wait for a new round
        client.request(
            'POST', '/games/{}/board?token={}'.format(game, token),
            json.dumps({
                'x': x,
                'y': y,
            })
        )
    
        response = client.getresponse()
        return json.loads(response.read().decode())

    # start
    
    x = 1
    y = 1
    data = sendrequest(x,y)

    while data['moves'] > 0:
        # print(data)
        x, y = data['moved']
        xdirection = 1
        ydirection = 1
        
        maxpoints = 0
        
        if x + 1 < 5 and data['board'][x+1][y]['points'] > maxpoints:
            maxpoints = data['board'][x+1][y]['points']
            x = x + 1
            
        if x - 1 > -1 and data['board'][x-1][y]['points'] > maxpoints:
            maxpoints = data['board'][x-1][y]['points']
            x = x - 1
            
        if y + 1 < 5 and data['board'][x][y+1]['points'] > maxpoints:
            maxpoints = data['board'][x][y+1]['points']
            y = y + 1
        
        if y - 1 > -1 and data['board'][x][y-1]['points'] > maxpoints:
            maxpoints = data['board'][x][y-1]['points']
            y = y - 1
            
        # for i in range(5):
        #     for j in range(5):
        #         if data['board'][i][j]['points'] > maxpoints:
        #             x = i
        #             y = j
        #             maxpoints = data['board'][i][j]['points']
        
            
        print (x,y)
        print (maxpoints)
        
        data = sendrequest(x,y)
    