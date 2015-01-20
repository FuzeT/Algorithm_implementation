__author__ = 'fuze'


class Sunday:

    def __init__(self, text):
        self.text = text
        self.length = len(text)

    def find(self, script):
        flag = False
        if isinstance(script, str):
            script_length = len(script)
            if self.length < script_length:
                return False
            else:
                text_cursor = script_length
                while not flag:
                    if text_cursor > self.length:
                        return False
                    script_cursor = script_length - 1
                    temp_cursor = text_cursor - 1
                    while self.text[temp_cursor] == script[script_cursor]:
                        temp_cursor -= 1
                        script_cursor -= 1
                        if script_cursor < 0:
                            return True, temp_cursor+1, text_cursor-1
                    else:
                        script_cursor = script_length - 1
                        temp_cursor = text_cursor - 1
                        if temp_cursor+1 > self.length:
                            return False
                    while self.text[temp_cursor+1] != script[script_cursor]:
                        script_cursor -= 1
                        if script_cursor < 0:
                            text_cursor = text_cursor + script_length + 1
                            break
                    else:
                        text_cursor = text_cursor + script_length - script_cursor

if __name__ == '__main__':
    string = "This is a long long string for test, and what i'm searching for is that!"
    test = Sunday(string)
    r = test.find('ds')
    print r