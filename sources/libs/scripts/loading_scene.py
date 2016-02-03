import bge
import time
import datetime

import logging
import logging.config
import sys
import argparse


from libs.apaimanee.client import ApaimaneeMOBAClient

def initial_game():
    # print("arg:", sys.argv)
    parser = argparse.ArgumentParser(prog='ApaimaneeMOBA',
                                     description='Apaimanee MOBA Game')
    parser.add_argument('blend', nargs='?',
                        help='')
    parser.add_argument('--client_id', nargs='?', const='test_client_id',
                        default='test_client_id',
                        help='ApaimaneeMOBA client_id')
    parser.add_argument('--room_id', nargs='?', const='test_room_id',
                        default='test_room_id',
                        help='ApamneeMOBA room_id')
    parser.add_argument('--host', nargs='?', const='localhost',
                        default='localhost',
                        help='ApamneeMOBA API host')
    parser.add_argument('--port', nargs='?', const=1883,
                        default=1883,
                        help='ApamneeMOBA API port')




    args = parser.parse_args()

    logging.config.fileConfig('logging.conf')
    logger = logging.getLogger('apmn')

    logger.info('Apaimanee Game start')
    logger.info('Try to connect to host {} port {} client_id {} room_id {}'.format(args.host, args.port, args.client_id, args.room_id))


    ac = ApaimaneeMOBAClient(args.client_id,
                             args.host, args.port,
                             args.room_id)

    ac.connect()
    gc = ac.game_client
    
    # remove if release
    if args.client_id == 'test_client_id' and args.room_id == 'test_room_id':
        gc.user.loggedin_info = dict(token='test_token')
        gc.room.current_room = dict(room_id=args.room_id)
    
    
    gc.game.ready()
    logger.info('Apaimanee Game load ready')

def loading_scene():
    cont = bge.logic.getCurrentController()
    scene_act = cont.actuators["Scene"]

    owner = cont.owner

    if 'start_time' in owner:
        ac = ApaimaneeMOBAClient()
        if ac.game_logic.status == 'play':

            logger = logging.getLogger('apmn')
            logger.info('Play game')

            cont.activate(scene_act)

        start_time = owner['start_time']
        diff_time = datetime.datetime.now() - start_time
        print('wait for play singnal', diff_time.seconds)

        if diff_time > datetime.timedelta(minutes=2):
            game_out_actualtor = cont.actuators['GameOut']
            print('time out')
            ac.disconnect()
            cont.activate(game_out_actualtor)


    else:
        
        try:
            initial_game()
        except Exception as e:
            print('Initial Fail:', e)
            game_out_actualtor = cont.actuators['GameOut']
            cont.activate(game_out_actualtor)

        owner['start_time'] = datetime.datetime.now()


