import datetime

class FileNameHandler:

    def get_backup_date():
        return str(datetime.datetime.today().strftime('%d-%m-%Y'))
