# Imports
from .models import Review
from django import forms
from django.utils.safestring import mark_safe


# Review form
class FormReview(forms.ModelForm):
    # Credit for adapted choices on TypedChoiceField
    # See README.md for more details
    rating = forms.TypedChoiceField(
        choices=(
            (1, mark_safe('<span class="text-center altFont star">\
                <i class="fa fa-star highlight"></i>\
                <i class="fa fa-star"></i>\
                <i class="fa fa-star"></i>\
                <i class="fa fa-star"></i>\
                <i class="fa fa-star"></i>\
                Extremely Unsatisfied </span>')),
            (2, mark_safe('<span class="text-center altFont star">\
                <i class="fa fa-star highlight"></i>\
                <i class="fa fa-star highlight"></i>\
                <i class="fa fa-star"></i>\
                <i class="fa fa-star"></i>\
                <i class="fa fa-star"></i>\
                Unsatisfied </span>')),
            (3, mark_safe('<span class="text-center altFont star">\
                <i class="fa fa-star highlight"></i>\
                <i class="fa fa-star highlight"></i>\
                <i class="fa fa-star highlight"></i>\
                <i class="fa fa-star"></i>\
                <i class="fa fa-star"></i>\
                Neutral </span>')),
            (4, mark_safe('<span class="text-center altFont star">\
                <i class="fa fa-star highlight"></i>\
                <i class="fa fa-star highlight"></i>\
                <i class="fa fa-star highlight"></i>\
                <i class="fa fa-star highlight"></i>\
                <i class="fa fa-star"></i>\
                Satisfied </span>')),
            (5, mark_safe('<span class="text-center altFont star">\
                <i class="fa fa-star highlight"></i>\
                <i class="fa fa-star highlight"></i>\
                <i class="fa fa-star highlight"></i>\
                <i class="fa fa-star highlight"></i>\
                <i class="fa fa-star highlight"></i>\
                Extremely Satisfied </span>'))
            ),
        widget=forms.RadioSelect,
    )

    class Meta:
        model = Review
        fields = ['review', 'rating']
        exclude = ['added_by']
        widgets = {
            'review': forms.Textarea(attrs={'\
            placeholder': 'Tell us what you think...', 'class': 'altFont'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Remove labels auto generated by form
        self.fields['review'].label = False
        self.fields['rating'].label = False
