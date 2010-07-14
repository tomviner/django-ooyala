from django.template import RequestContext
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render_to_response
from django.http import HttpResponse
from datetime import datetime, date, timedelta

from ooyala.conf import *
from ooyala.library import OoyalaQuery, OoyalaLabelManage, OoyalaChannel
from ooyala.constants import OoyalaConstants as O
from ooyala.models import OoyalaItem

@staff_member_required
def backlot_query(request):
    req = OoyalaQuery(content_type='video')

    ooyala_response = req.process()
    if type(ooyala_response)!=str:
        items = ooyala_response.getElementsByTagName('item')
        for item in items:
            OoyalaItem.from_xml(item)

    else:
        print "got an error back"

    return HttpResponse("tada")


