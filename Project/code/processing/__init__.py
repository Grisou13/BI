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
    def __init__(self):
        if self.name is None:
            self.name = un_camel(self.__class__.__name__.replace("Processor","")) # remove Processor to the name
