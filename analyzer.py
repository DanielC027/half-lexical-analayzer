import re


class Analayzer:
    def __init__(self) -> None:
        self.__phone_regex = r"^\d{10}$"
        self.__email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        self.__curp_regex = r"^[A-Z]{4}\d{6}[HM][A-Z]{5}[A-Z0-9]\d$"
        self.__rfc_regex = r"^[A-ZÑ&]{4}\d{6}[A-Z0-9]{3}$"
        self.__ipv4_regex = r"^(?:\d{1,3}\.){3}\d{1,3}$"
        self.__birthday_regex = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{2}$"

    def analayzer(self, string):
        # Instead of return tokens table, just return type of lexema found for this practice
        if re.match(self.__phone_regex, string):
            return "phone"
        elif re.match(self.__email_regex, string):
            return "email"
        elif re.match(self.__curp_regex, string):
            return "curp"
        elif re.match(self.__rfc_regex, string):
            return "rfc"
        elif re.match(self.__ipv4_regex, string):
            return "ipv4"
        elif re.match(self.__birthday_regex, string):
            return "birth"
        else:
            return "nothing"


print(Analayzer().analayzer("31/01/19"))
