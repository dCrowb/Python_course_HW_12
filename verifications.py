import re
import datetime
import decorators


@decorators.input_error
def check_phone_number(phone: str):
    phone = phone.replace(' ', '').replace('-', '')
    check_phone = re.search(r'[+][0-9]{12}|[0-9]{10}', phone)
    if check_phone and len(phone) == 13:
        return phone
    elif check_phone and len(phone) == 10:
        phone = '+38' + phone
        return phone
    else:
        raise decorators.PhoneError
  
    
@decorators.datatime_error
def check_birthday(birthday: str):
    datetime_object = datetime.datetime.strptime(birthday, '%d.%m.%Y').date()
    if datetime.datetime.now().date() <= datetime_object:
        raise decorators.DateError
    return datetime_object


if __name__ == '__main__':
    print(check_birthday('14.05.2023'))
