import six


def is_magic_attr(name):
    return name.startswith('__') and name.endswith('__')


class SimpleChoiceMeta(type):

    def __new__(mcs, what, bases, attrs):
        choices = []
        for name, value in attrs.items():
            if is_magic_attr(name):
                continue

            attrs[name] = name
            choices.append((name, value))

        kls = super(SimpleChoiceMeta, mcs).__new__(mcs, what, bases, attrs)
        kls.choices = tuple(choices)

        return kls


@six.add_metaclass(SimpleChoiceMeta)
class SimpleChoice(object):
    pass
