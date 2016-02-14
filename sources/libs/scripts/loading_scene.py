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
    parser.add_argument('--token', nargs='?', const='test_token',
                        default='test_token',
                        help='ApamneeMOBA token')
    parser.add_argument('--host', nargs='?', const='localhost',
                        default='localhost',
                        help='ApamneeMOBA API host')
    parser.add_argument('--port', nargs='?', const=1883,
                        default=1883,
                        help='ApamneeMOBA API port')
    parser.add_argument('--log', nargs='?', const='logging.conf',
                        default='logging.conf',
                        help='ApamneeMOBA API logging')



    args = parser.parse_args()

    logging.config.fileConfig(args.log)
    logger = logging.getLogger('apmn')

    logger.info('Apaimanee Game start')
    logger.info('Try to connect to host {} port {} client_id {} room_id {}'.format(args.host, args.port, args.client_id, args.room_id))


    ac = ApaimaneeMOBAClient(args.client_id,
                             args.host, int(args.port),
                             args.room_id)

    ac.connect()
    gc = ac.game_client
    gc.user.loggedin_info = dict(token=args.token)
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
            logger = logging.getLogger('apmn')
            print('Initial Fail:', e)
            logger.exception(e)
            game_out_actualtor = cont.actuators['GameOut']
            cont.activate(game_out_actualtor)

        owner['start_time'] = datetime.datetime.now()


