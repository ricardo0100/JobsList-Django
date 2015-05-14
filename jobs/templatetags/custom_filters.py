from widget_tweaks.templatetags.widget_tweaks import silence_without_field, register, append_attr


@register.filter("add_placeholder")
@silence_without_field
def add_placeholder(field, placeholder):
    return append_attr(field, 'placeholder:' + placeholder)
