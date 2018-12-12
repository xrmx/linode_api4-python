# Custom Documentor for using properties
import sphinx
from sphinx.ext.autodoc import ClassDocumenter, Documenter
from linode_api4.objects.base import Base

class LinodeAPIClassDocumenter(ClassDocumenter):
    objtype = 'class'

    priority = 10

    @classmethod
    def can_document_member(cls, member, membername, isattr, parent):
        result =  type(member) == type and issubclass(member, Base)
        if result:
            print("I FOUND ONE!!!!!")
        return result

    def import_object(self):
        ret = super().import_object()

        if hasattr(ret, 'properties'):
            for k, v in ret.properties:
                setattr(ret, k, 'testing thism jawn')

        return ret


# register our documenter
def setup(app):
    app.add_autodocumenter(LinodeAPIClassDocumenter)

    return {'version': sphinx.__display_version__, 'parallel_read_safe': True}

