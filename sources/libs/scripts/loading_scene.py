from bge import logic
import time

import sys
import argparse


def loading_scene():
    cont = logic.getCurrentController()
    scene_act = cont.actuators["Scene"]

    print("arg:", sys.argv)
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
    parser.add_argument('--port', nargs='?', const='1883',
                        default='1883',
                        help='ApamneeMOBA API port')




    args = parser.parse_args()

    import logging
    import logging.config

    logging.config.fileConfig('logging.conf')
    logger = logging.getLogger('apmn')

    logger.info('Apaimanee Game start')
    logger.info('Try to connect to host {} port {} client_id {} room_id {}'.format(args.host, args.port, args.client_id, args.room_id))


    from libs.apaimanee.client import ApaimaneeMOBAClient
    ac = ApaimaneeMOBAClient(args.client_id,
                             args.host, args.port,
                             args.room_id)

    # wait start game signal from apaimanee server

    cont.activate(scene_act)
