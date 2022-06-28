from django import forms

from blogpost.models import Post, Block


class PostForm(forms.ModelForm):


    class Meta:
        model = Post
        exclude= ("file",)


class BlockForm(forms.ModelForm):

    class Meta:
        model = Block
        exclude = ('bloking_user',)