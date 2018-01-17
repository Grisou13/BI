def un_camel(x):
    final = ''
    for item in x:
        if item.isupper():
            final += "_"+item.lower()
        else:
            final += item
    if final[0] == "_":
        final = final[1:]
    return final

class Processor:
    input = ""
    out = ""

    def __init__(self):
        if not hasattr(self,"name"):
            self.name = un_camel(self.__class__.__name__.replace("Processor","")) # remove Processor to the name