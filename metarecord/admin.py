from django import forms
from django.contrib import admin
from django.db import transaction

from .models import Action, Attribute, AttributeValue, Function, Phase, Record, RecordType


class ModelFormWithAttributes(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # set initial values for the attribute fields
        for name in Attribute.objects.values_list('name', flat=True):
            try:
                self.fields[name].initial = self.instance.attribute_values.get(attribute__name=name)
            except AttributeValue.DoesNotExist:
                pass


class StructuralElementAdmin(admin.ModelAdmin):
    exclude = ('attribute_values',)
    form = ModelFormWithAttributes

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add dynamic attributes as ChoiceFields or CharFields to the form.
        # One known caveat in this method is that a restart is required for new fields to show
        # because this is run only at app startup.
        new_fields = []
        for name, is_free_text in Attribute.objects.values_list('name', 'is_free_text'):
            if is_free_text:
                new_field = (
                    name,
                    forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 4, 'cols': 80}))
                )
            else:
                new_field = (
                    name,
                    forms.ModelChoiceField(
                        queryset=AttributeValue.objects.filter(attribute__name=name),
                        required=False
                    )
                )
            new_fields.append(new_field)
        self.form.base_fields.update(new_fields)

    @transaction.atomic
    def save_model(self, request, obj, form, change):
        obj.save()

        # handle dynamic ManyToMany attribute saving
        for name, is_free_text in Attribute.objects.values_list('name', 'is_free_text'):
            value = form.cleaned_data.get(name)
            attribute = Attribute.objects.get(name=name)

            # handle free text attributes
            if is_free_text:
                attribute = Attribute.objects.get(name=name)
                if value:
                    try:
                        attribute_value = obj.attribute_values.get(attribute=attribute)
                        attribute_value.value = value
                        attribute_value.save(update_fields=('value',))
                    except AttributeValue.DoesNotExist:
                        attribute_value = AttributeValue.objects.create(attribute=attribute, value=value)
                        obj.attribute_values.add(attribute_value)
                else:
                    obj.attribute_values.filter(attribute=attribute).delete()
                continue

            # handle choice attributes
            obj.attribute_values.filter(attribute=attribute).delete()
            if value:
                obj.attribute_values.add(form.cleaned_data.get(name))


class FunctionAdmin(StructuralElementAdmin):
    list_display = ('function_id', 'name')
    ordering = ('function_id',)
    exclude = ('attribute_values',)


class PhaseAdmin(StructuralElementAdmin):
    pass


class ActionAdmin(StructuralElementAdmin):
    pass


class RecordAdmin(StructuralElementAdmin):
    pass


class AttributeValueInline(admin.StackedInline):
    model = AttributeValue
    extra = 0


class AttributeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
    inlines = (AttributeValueInline,)

    class Meta:
        model = Attribute


admin.site.register(Function, FunctionAdmin)
admin.site.register(Phase, PhaseAdmin)
admin.site.register(Action, ActionAdmin)
admin.site.register(Record, RecordAdmin)
admin.site.register(RecordType)
admin.site.register(Attribute, AttributeAdmin)
