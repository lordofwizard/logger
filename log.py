class Logger:
    def __init__(self, log_file):
        self.log_file = log_file

    def __log_time(self) -> dict:
        current_time = datetime.now()
        date_str = current_time.strftime("%m-%d-%y")
        time_str = current_time.strftime("%H:%M:%S")
        return {"date": date_str, "time": time_str}

    def log(self,title: str, message : str ,severity : int):
        """Function to give a log for an object that will store the command message with _color_
        """
        log_data = {
            **self.__log_time(),
            "title":title,
            "logmsg": message,
            "severity" : severity
        }
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w') as f:
                pass  # Creates the file if it doesn't exist
        with open(self.log_file, 'a') as f:
            json.dump(log_data, f)
            f.write('\n')
    def log(self,title: str, message : str):
        """Function to give a log for an object that will store the command message
        """
        log_data = {
            **self.__log_time(),
            "title":title,
            "logmsg": message
        }
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w') as f:
                pass  # Creates the file if it doesn't exist
        with open(self.log_file, 'a') as f:
            json.dump(log_data, f)
            f.write('\n')
