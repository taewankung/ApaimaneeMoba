from apmn.forms import games as games_form

def create_room(request):

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

    return request.redirect_url('/games/room')


def room(request):
    return dict()
