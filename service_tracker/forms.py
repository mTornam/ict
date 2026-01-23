from django import forms
from .models import ServiceRecord

class ServiceRecordForm(forms.ModelForm):
    class Meta:
        model = ServiceRecord
        exclude = ['returned_at','received_at']
        widgets = {
            'is_resolved': forms.widgets.CheckboxInput(attrs={'class': 'rounded border-gray-300'}),
            'room_number': forms.TextInput(attrs={
                'inputmode': 'numeric',
                'pattern': '[0-9]*',
                'placeholder': 'e.g. 202',
                'class': 'border border-gray-300 rounded px-3 py-2 w-full',
            }),
            'requester_name': forms.TextInput(attrs={'class': 'border border-gray-300 rounded px-3 py-2 w-full'}),
            'requester_contact': forms.TextInput(attrs={'class': 'border border-gray-300 rounded px-3 py-2 w-full'}),
            'device_name': forms.TextInput(attrs={'class': 'border border-gray-300 rounded px-3 py-2 w-full'}),
            'device_type': forms.Select(attrs={'class': 'border border-gray-300 rounded px-3 py-2 w-full'}),
            'problem_type': forms.Select(attrs={'class': 'border border-gray-300 rounded px-3 py-2 w-full'}),
            'problem_desc': forms.Textarea(attrs={'class': 'border border-gray-300 rounded px-3 py-2 w-full', 'rows': 4}),
            'district': forms.Select(attrs={'class': 'border border-gray-300 rounded px-3 py-2 w-full'}),
            'received_by': forms.TextInput(attrs={'class': 'border border-gray-300 rounded px-3 py-2 w-full'}),
        }
        
    
    def clean_room_number(self):
        value = self.cleaned_data.get('room_number')

        if not value:
            return value
    
        if not value.isdigit():
            raise forms.ValidationError("Room number must contain digits only.")

        if len(value) > 3:
            raise forms.ValidationError("Room number must be at most 3 digits.")

        # Pad with leading zeros
        return value.zfill(3)            