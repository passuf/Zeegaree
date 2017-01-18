import os.path
from habitica.api import Habitica
from habitica.core import load_auth

def up_score(notification=''):

    if not 'Long Break' in notification and not 'Short Break' in notification:
        return

    auth = load_auth(os.path.expanduser('~') + '/.config/habitica/auth.cfg')
    habit = auth.pop('checklists')
    h = Habitica(auth=auth)
    h.user.tasks(_id=habit, _direction='up', _method='post')
