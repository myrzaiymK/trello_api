from django import forms
from .models import Board, Column, Card, Comment, Label
from django import forms


class LabelForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = [
            "title",
            "image",
        ]


class ColumnForm(forms.ModelForm):
    class Meta:
        model = Column
        fields = [
            "title",
            "board",
        ]


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = '__all__'
