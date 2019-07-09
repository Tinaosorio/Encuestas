from django.forms.utils import ErrorList


class DivErrorList(ErrorList):
    def __str__(self):
        return self.as_divs

    @property
    def as_divs(self):
        if not self:
            return ''
        else:
            return '<div class="alert alert-danger">%s</div>' % \
                   ''.join(['<div>%s</div>' % e for e in self])
