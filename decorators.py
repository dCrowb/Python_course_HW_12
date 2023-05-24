class PhoneError(Exception):
    pass


class DateError(Exception):
    pass


def input_error(func):
    def inner(*args):
        try:
            result = func(*args)
            return result
        except SystemExit:
            print('Incorect command')
        except PhoneError:
            return 'Incorrect phone number'
        # except AttributeError:
        #     print('Incorect argument!')
        except ValueError:
            print('Give me name and phone please')
        except KeyError:
            print('User doesn`t exist')
        except IndexError:
            print('Enter user name')
        # except UnboundLocalError:
        #     print('Try again')
    return inner


def datatime_error(func):
    def inner(*args):
        try:
            result = func(*args)
            return result
        except ValueError:
            print('Incorrect birthday! Must be dd.mm.yyyy')
        except DateError:
            print('This person is not yet born!')
    return inner