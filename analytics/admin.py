from django.contrib import admin
from django import forms 
from ckeditor_uploader.widgets import CKEditorUploadingWidget
#from django.utils.safestring import mark_safe

# Register your models here.
from .models import Analysis,Market,Asset,Exchange,Symbol,Channel,Timeframe,Status,Action, Rating, Alert

class AnalysisAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Analysis
        fields = '__all__'


class AnalysisAdmin(admin.ModelAdmin):
    form = AnalysisAdminForm
    prepopulated_fields = {'slug': ('title',)}


class MarketAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class AssetAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('acronym',)}

class AlertAdmin(admin.ModelAdmin):
    save_as = True


admin.site.register(Analysis, AnalysisAdmin)
admin.site.register(Market,MarketAdmin )
admin.site.register(Asset, AssetAdmin)
admin.site.register(Alert, AlertAdmin)
admin.site.register(Exchange)
admin.site.register(Symbol)
admin.site.register(Channel)
admin.site.register(Timeframe)
admin.site.register(Action)
admin.site.register(Rating)
admin.site.register(Status)




