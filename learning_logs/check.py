from django.http import Http404


def check_topic_owner(request,topic):
    if topic.owner != request.user:
        raise Http404


def check_entry_owner(request,entry):
    if entry.owner != request.user:
        raise Http404


def check_topic_public(request,topic):
    if not topic.public and request.user!=topic.owner:
        raise Http404
