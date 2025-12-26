from django import forms

from .models import Booking, Review


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'phone', 'service']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Например, Анна'}),
            'phone': forms.TextInput(attrs={'placeholder': '+7 (___) ___-__-__'}),
        }

    def clean_phone(self):
        phone = (self.cleaned_data.get('phone') or '').strip()
        if len(phone) < 7:
            raise forms.ValidationError('Введите корректный телефон.')
        return phone


class ReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(
        label='Оценка',
        choices=[(i, f'{i}/5') for i in range(5, 0, -1)],
    )

    class Meta:
        model = Review
        fields = ['name', 'rating', 'text']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ваше имя'}),
            'text': forms.Textarea(attrs={'placeholder': 'Напишите ваш отзыв', 'rows': 4}),
        }

    def clean_text(self):
        text = (self.cleaned_data.get('text') or '').strip()
        if len(text) < 12:
            raise forms.ValidationError('Отзыв слишком короткий (минимум 12 символов).')
        return text
