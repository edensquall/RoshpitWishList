from wtforms import SelectField
from wtforms.widgets import Select, HTMLString, html_params


class SelectHasAttributesOption(Select):
    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', field.id)
        if self.multiple:
            kwargs['multiple'] = True
        if 'required' not in kwargs and 'required' in getattr(field, 'flags', []):
            kwargs['required'] = True
        html = ['<select %s>' % html_params(name=field.name, **kwargs)]
        for val, label, selected, render_kw in field.iter_choices_with_render_kw():
            html.append(self.render_option(val, label, selected, **render_kw))
        html.append('</select>')
        return HTMLString(''.join(html))


class SelectHasAttributesOptionField(SelectField):
    widget = SelectHasAttributesOption()

    def iter_choices(self):
        for value, label, *_ in self.choices:
            yield value, label, self.coerce(value) == self.data

    def pre_validate(self, form):
        for v, *_ in self.choices:
            if self.data == v:
                break
        else:
            raise ValueError(self.gettext('Not a valid choice'))

    def iter_choices_with_render_kw(self):
        for value, label, *render_kw in self.choices:
            render_kw = render_kw[0] if render_kw else {}
            yield value, label, self.coerce(value) == self.data, render_kw
