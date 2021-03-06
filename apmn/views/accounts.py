'''
Created on Dec 3, 2012

@author: superizer
'''


import logging
logger = logging.getLogger(__name__)

from apmn.forms import accounts as account_form

def home(request):
    requestdata = request.apmn_client.room.list_rooms()
    print(requestdata)

    return dict(rooms=requestdata['responses']['rooms'])

def login(request):

    #print("This is login : ", request.matchdict)

    if request.session.get('user', None):
        return request.redirect_url('/home')

    form = account_form.AccountForm(request.matchdict)

    if len(request.matchdict) == 0:
        return dict(form=form)
    if len(request.matchdict) > 0 and form.validate():
        username = form.data.get('username')
        password = form.data.get('password')

    else:
        return dict(
                    form = form,
                    message = 'check username and password again'
                    )

    try:
        data = request.apmn_client.user.login(username, password)
        #print ('data:', data)
        #if 'access' not in data:
        #    raise 'error'
        if not data['responses']['loggedin']:
            raise 'password missmatch'

        request.remember(data)
    except Exception as e:
        logger.exception(e)
        return dict(
                    message='Passwords mismatch',
                    form = form
                    )

    return request.redirect_url('/home')

def register(request):
    form = account_form.RegisterForm(request.matchdict)
    if len(request.matchdict) == 0:
        return dict(form=form)
    if len(request.matchdict) > 0 and form.validate():
        username = form.data.get('username')
        firstname = form.data.get('firstname')
        lastname = form.data.get('lastname')
        confirmpassword = form.data.get('confirmpassword')
        email = form.data.get('email')
        password = form.data.get('password')
    else:
        return dict(
                    form = form,
                    message = "Prease recheck field"
                    )

    try:
        data = request.apmn_client.user.register(username, password, email, firstname, lastname)
        if data is None or 'error' in data:
            raise Exception('error')

    except Exception as e:
        logger.exception(e)
        logger.error("error: ", data)
        return dict(
                    message=data.get("error", "Can't Register"),
                    form = form
                    )

    return request.redirect_url('/login')

def logout(request):
    request.forget()
    return request.redirect_url('/login')

