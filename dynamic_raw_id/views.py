from django.apps import apps
from django.conf import settings
from django.contrib.auth.decorators import user_passes_test
from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseForbidden,
)
from django.shortcuts import render
from django.urls import reverse


@user_passes_test(lambda u: u.is_staff)
def label_view(  # noqa: PLR0913 Too Many arguments
    request: HttpRequest,
    app_name: str,
    model_name: str,
    admin_site,
    template_name: str,
    multi: bool = False,
    template_object_name: str = "object",
) -> HttpResponse:
    admin_site_name = admin_site.name
    # The list of to obtained objects is in GET.id. No need to resume if we
    # didn't get it.
    if not request.GET.get("id"):
        msg = "No list of objects given"
        return HttpResponseBadRequest(settings.DEBUG and msg or "")

    # Given objects are either an integer or a comma-separated list of
    # integers. Validate them and ignore invalid values. Also strip them
    # in case the user entered values by hand, such as '1, 2,3'.
    object_list = [pk.strip() for pk in request.GET["id"].split(",")]

    # Make sure this model exists and the user has 'change' permission for it.
    # If he doesn't have this permission, Django would not display the
    # change_list in the popup, and the user was never able to select objects.
    try:
        model = apps.get_model(app_name, model_name)
    except LookupError:
        msg = f"Model {app_name}.{model_name} does not exist."
        return HttpResponseBadRequest(msg)

    if model not in admin_site._registry:
        msg = "Model %s.%s not registered." % (app_name, model_name)
        return HttpResponseBadRequest(settings.DEBUG and msg or "")

    model_admin = admin_site._registry[model]
    if not model_admin.has_view_permission(request):
        return HttpResponseForbidden()

    # Check 'view' permission
    if not request.user.has_perm(f"{app_name}.view_{model_name}"):
        return HttpResponseForbidden()

    try:
        if multi:
            model_template = f"dynamic_raw_id/{app_name}/multi_{model_name}.html"
            objs = model.objects.filter(pk__in=object_list)
            objects = [
                (obj, reverse(f"{admin_site_name}:{app_name}_{model_name}_change", args=[obj.pk]))
                for obj in objs
            ]
            extra_context = {template_object_name: objects}
        else:
            model_template = f"dynamic_raw_id/{app_name}/{model_name}.html"
            obj = model.objects.get(pk=object_list[0])
            change_url = reverse(f"{admin_site_name}:{app_name}_{model_name}_change", args=[obj.pk])
            extra_context = {template_object_name: (obj, change_url)}

    # most likely, the pk wasn't convertable
    except ValueError:
        msg = "ValueError during lookup"
        return HttpResponseBadRequest(msg)
    except model.DoesNotExist:
        msg = "Model instance does not exist"
        return HttpResponseBadRequest(msg)

    return render(request, (model_template, template_name), extra_context)
