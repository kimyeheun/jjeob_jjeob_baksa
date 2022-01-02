from django import forms
from .models import Food


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['food_title', 'heart_vote', 'food_desc', 'food_pic']
        widgets = {
            'food_title': forms.TextInput(
                attrs={
                    'class': 'food__input food_form',
                }
            ),
            # 'category_id': forms.Select(
            #     attrs={
            #         'class': 'food__input food_form',
            #     }
            # ),
            'heart_vote': forms.TextInput(
                attrs={
                    'type': "number",
                    'id': 'food__input__point',
                    'class': 'food__input food_form',
                }
            ),
            'food_desc': forms.Textarea(
                attrs={
                    'id': 'food__input__content',
                    'class': 'food__input food_form',
                }
            )
        }
