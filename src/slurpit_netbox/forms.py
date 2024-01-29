from core.choices import DataSourceStatusChoices
from django import forms
from dcim.choices import DeviceStatusChoices, DeviceAirflowChoices
from dcim.models import DeviceRole, DeviceType, Site, Location, Region, Rack
from django.utils.translation import gettext_lazy as _
from netbox.api.fields import ChoiceField
from netbox.forms import NetBoxModelBulkEditForm, NetBoxModelFilterSetForm, NetBoxModelForm
from utilities.forms import add_blank_choice
from utilities.forms.fields import CommentField, DynamicModelChoiceField
from utilities.forms.widgets import APISelect
from tenancy.models import TenantGroup, Tenant
from utilities.forms import BootstrapMixin
from .models import SlurpitImportedDevice, SlurpitPlanning, SlurpitSetting
from .management.choices import SlurpitApplianceTypeChoices

class OnboardingForm(NetBoxModelBulkEditForm):
    model = SlurpitImportedDevice
    device_type = DynamicModelChoiceField(
        label=_('Device type'),
        queryset=DeviceType.objects.all(),
        required=True,
        query_params={
            'manufacturer_id': '$manufacturer'
        }
    )
    role = DynamicModelChoiceField(
        label=_('Device role'),
        queryset=DeviceRole.objects.all(),
        required=True
    )
    site = DynamicModelChoiceField(
        label=_('Site'),
        queryset=Site.objects.all(),
        required=True
    )
    region = DynamicModelChoiceField(
        label=_('Region'),
        queryset=Region.objects.all(),
        required=False
    )
    location = DynamicModelChoiceField(
        label=_('Location'),
        queryset=Location.objects.all(),
        required=False,
        query_params={
            'site_id': '$site'
        },
        initial_params={
            'racks': '$rack'
        }
    )
    rack = DynamicModelChoiceField(
        label=_('Rack'),
        queryset=Rack.objects.all(),
        required=False,
        query_params={
            'site_id': '$site',
            'location_id': '$location',
        }
    )
    position = forms.DecimalField(
        label=_('Position'),
        required=False,
        help_text=_("The lowest-numbered unit occupied by the device"),
        localize=True,
        widget=APISelect(
            api_url='/api/dcim/racks/{{rack}}/elevation/',
            attrs={
                'disabled-indicator': 'device',
                'data-dynamic-params': '[{"fieldName":"face","queryParam":"face"}]'
            },
        )
    )
    latitude = forms.DecimalField(
        label=_('Latitude'),
        max_digits=8,
        decimal_places=6,
        required=False,
        help_text=_("GPS coordinate in decimal format (xx.yyyyyy)")
    )
    longitude = forms.DecimalField(
        label=_('longitude'),
        max_digits=9,
        decimal_places=6,
        required=False,
        help_text=_("GPS coordinate in decimal format (xx.yyyyyy)")
    )
    tenant_group = DynamicModelChoiceField(
        label=_('Tenant group'),
        queryset=TenantGroup.objects.all(),
        required=False,
        null_option='None',
        initial_params={
            'tenants': '$tenant'
        }
    )
    tenant = DynamicModelChoiceField(
        label=_('Tenant'),
        queryset=Tenant.objects.all(),
        required=False,
        query_params={
            'group_id': '$tenant_group'
        }
    )
    description = forms.CharField(
        label=_('Description'),
        max_length=200,
        required=False
    )
    airflow = forms.ChoiceField(
        label=_('Airflow'),
        choices=add_blank_choice(DeviceAirflowChoices),
        required=False
    )
    status = ChoiceField(
        label=_('Status'),
        choices=add_blank_choice(DeviceStatusChoices),
        required=False
    )

class SlurpitPlanningTableForm(BootstrapMixin, forms.Form):
    id = DynamicModelChoiceField(
        queryset=SlurpitPlanning.objects.all(),
        required=True,
        label=_("Slurpit Plans"),
    )

class SlurpitApplianceTypeForm(BootstrapMixin, forms.Form):
    model =  SlurpitSetting
    appliance_type = forms.ChoiceField(
        label=_('Appliance Type'),
        choices=add_blank_choice(SlurpitApplianceTypeChoices),
        required=False
    )