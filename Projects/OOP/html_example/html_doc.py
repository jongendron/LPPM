# is-a -> inheritance (Head is a subclass of tag)
# has-a -> composition (HtmlDoc has a Head, Body, and DocType class set as it's attributes)
# Resource: https://www.w3.org/TR/html401/struct/global.html

class Tag(object):

    def __init__(self, name, contents):
        self.start_tag = '<{}>'.format(name)
        self.end_tag = '</{}>'.format(name)
        self.contents = contents

    def __str__(self): # what is printed with print() function
        return "{0.start_tag}{0.contents}{0.end_tag}".format(self)
    
    def display(self, file=None):
        print(self, file=file) # print to file


class DocType(Tag):

    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/html4/strict.dtd', '')
        self.end_tag = '' # DOCTYPE doesn't have an end tag


class Head(Tag):

    # def __init__(self):
    #     super().__init__('head', '')
    def __init__(self, title=None):
        super().__init__('head', '')
        if title:
            self._title_tag = str(Tag('title', title)) # add a title
            self.contents += "\n\t"
            self.contents += self._title_tag
            self.contents += "\n"


class Body(Tag):

    def __init__(self):
        super().__init__('body', '')
        self._body_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents) # Composition: contains Tag class as part of attribute
        self._body_contents.append(new_tag)

    def display(self, file=None):
        for tag in self._body_contents:
            self.contents += str(tag)

        super().display(file=file) # print contents


# HtmlDoc class is composed of DocType, Head, and Body classes (Composition)
class HtmlDoc(object):

    # def __init__(self, title=None): # composition because attributes are class instances created within not saved as
    #     self._doc_type = DocType()
    #     self._head = Head(title=title)
    #     self._body = Body()

    def __init__(self, doc_type, head, body): # aggregation because instances are not created within the composition class, rather just saved as such
        self._doc_type = doc_type
        self._head = head
        self._body = body

    def add_tag(self, name, contents): # purposly had same same so the same method is always done whereever .add_tag is seen
        self._body.add_tag(name, contents)

    def display(self, file=None): # matches corresponding method in classes it's composed of so easier for users to see association (Polymorphic behavior with composition)
        self._doc_type.display(file=file)
        print('<html>', file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print('</html>', file=file)

if __name__ == '__main__':
    # my_page = HtmlDoc(title='Document Title')
    # my_page.add_tag('h1', 'Main Heading')
    # my_page.add_tag('h2', 'sub-heading')
    # my_page.add_tag('p', 'This is a paragraph that will appear on the page.')
    # with open("test.html", "w") as test_doc:
    #     my_page.display(file=test_doc)

    # Aggregation (has-a relation, but the superclass doesn't own the objects like in composition)
    # If the superclass instance is deleted, the classes it's composed of are not deleted in aggregation
    # Aggregation is convienient when you want class instances independent of a container class object (instance)
    new_body = Body()
    new_body.add_tag('h1', 'Aggregation')
    new_body.add_tag('p', "Unlike <strong>composition</strong>, aggregation uses existing instances"
                     " of objects to build up another object.")
    new_body.add_tag('p', "The composed object doesn't actually own the objects that it's composed of "
                     " - if it's destroyed, those objects continue to exist.")
    
    new_docType = DocType()
    new_header = Head('Aggregation document')

    my_page = HtmlDoc(new_docType, new_header, new_body)

    # Give our document new content by switching it's body
    my_page._body = new_body
    with open('test2.html', 'w') as test_doc:
        my_page.display(file=test_doc)