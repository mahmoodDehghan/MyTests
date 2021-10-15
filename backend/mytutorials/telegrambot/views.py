from django.http import HttpResponse
from .helpers.echobot_helper import activate_bot, deactive_bot
# Create your views here.
def start_bot(request):
  activate_bot()
  return HttpResponse("<p>Bot is Activated</p>")


def end_bot(request):
  deactive_bot()
  return HttpResponse("<p>the Bot is deactivated</p>")  