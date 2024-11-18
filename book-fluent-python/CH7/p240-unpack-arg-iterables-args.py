def tag(name, *content, class_=None, **attrs):
    print("tag() entered: name: ", name, ", *content: ", content, ", class_: ", class_, "attrs: ", attrs) 
    "Generate one more more html tags."

    if class_ is not None:
        attrs['class'] = class_

    attr_pairs=(f'{attr}={value}"' for attr, value in sorted(attrs.items()))
    attr_str=''.join(attr_pairs)
    if content:
        elements=(f'<{name}{attr_str}>{c}</{name}>' for c in content)
        return '\n'.join(elements)
    else:
        return f'<{name}{attr_str}/>'

print(tag('br'))
print(tag('p', 'hello'))
print(tag('p', 'hello', 'world'))
print(tag('p', 'hello', id=33))
print(tag('p', 'hello', 'world', class_='sidebar'))
print(tag(content='testing', name='img'))
my_tag={'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'class' : 'framed'}
print(tag(**my_tag))


