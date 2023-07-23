from django import template
from django.contrib.auth import get_user_model
from django.utils.html import format_html


user_model =  get_user_model()
register = template.Library()


@register.filter
def author_details(author, current_user=None):
  if not isinstance(author, user_model):
    return ''
  
  name = f'{author.username}'

  if author == current_user:
    name = format_html('<strong>me</strong>')
  if author.first_name and author.last_name:
    name = f'{author.first_name} {author.last_name}'

  prefix, suffix = "", ""
  if author.email:
    prefix = format_html('<a href="mailto:{}">', author.email)
    suffix = format_html('</a>')

  return format_html('{}{}{}', prefix, name, suffix)
