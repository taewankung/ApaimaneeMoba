from apmn.forms import games as games_form
import logging
logger = logging.getLogger("apmn")
def create_room(request):
    if request.session.get('room_name',None):
        return request.redirect_url('/games/create_room')

    form =  games_form.CreateRoom(request.matchdict)

    if len(request.matchdict) == 0:
        return dict(form=form)

    if len(request.matchdict) > 0 and form.validate():
        room_name = form.data.get('room_name')
    else:
        return dict(
                    form = form,
                    message = 'Please Room Name.'
                    )

    try:
        data = request.apmn_client.room.create_room(room_name)
        if not data['responses']['room_id']:
            raise 'Not Found Room ID'

    except Exception as e:
        logger.exception(e)
        logger.error("error: ", data)
        return dict(
                message=data.get("error", "Can't Create Room"),
                form = form
                )


    return request.redirect_url('/games/room')


def join_game(request):
    room_id = request.matchdict['room_id']
    requestdata = request.apmn_client.room.join_game(room_id)

    return request.redirect_url('/games/room')



def room(request):
    requestdata = request.apmn_client.room.list_players()
    print('list_players', requestdata)

    players = requestdata['responses']['players']
    team1 = []
    team2 = []

    for player in players:
        if player["team"] == "team1":
            team1.append(player)
        else:
            team2.append(player)

    return dict(team1=team1, team2=team2)



def select_hero(request):
    return dict()
