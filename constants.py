from commands import (
    greeting_user,
    end_process,
    show_all_contacts
)


COMANDS_WITHOUT_ARGUMENTS = {
            'show_all': show_all_contacts,
            'hello': greeting_user,
            'good_bye': end_process, 
            'exit': end_process, 
            'close': end_process, 
            '.': end_process
            }
COMANDS_WITH_ARGUMENTS  = ['add', 'change', 'remove', 'show']
