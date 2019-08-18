import  xml.dom.minidom
class obj:
    def __init__(self):

        dom = xml.dom.minidom.parse('data.xml')
        self.root = dom.documentElement
    def name(self):

        bb = self.root.getElementsByTagName('p')
        for i in bb:
            print(i.getAttribute("name"))

    def age(self):

        bb = self.root.getElementsByTagName('p')
        for i in bb:
            print(i.getAttribute("age"))

    def key(self):

        bb = self.root.getElementsByTagName('el')
        for i in bb:
            print(i.getAttribute("key"))

    def value(self):

        bb = self.root.getElementsByTagName('el')
        for i in bb:
            print(i.getAttribute("value"))