import os


class CheckPoint:
    def __init__(self) -> None:
        pass

    def haveContent(self, file_name):
        try:
            if os.path.getsize(file_name) > 0:
                return True
            else:
                return False
        except Exception as ex:
            print("checkpoint/haveContent: ", ex)

    def getContent(self, file_name):
        try:
            with open(file_name, 'r') as file:
                return file.readline()

        except Exception as ex:
            print("checkpoint/getContent: ", ex)

    def setContent(self, file_name, content):
        try:
            with open(file_name, 'w') as file:
                file.write(content)

        except Exception as ex:
            print("checkpoint/setContent: ", ex)


# print(CheckPoint().haveContent("nada.txt"))
# print("->", CheckPoint().getContent("nada.txt"), "<-")
# CheckPoint().setContent("nada.txt", "hola1")
