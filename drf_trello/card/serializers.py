from trello_app.models import *
from rest_framework import serializers


class CardSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    board_id = serializers.IntegerField()
    column_id = serializers.IntegerField()
    title = serializers.CharField(max_length=150)
    description = serializers.CharField(max_length=150)
    date = serializers.DateField()

    def create(self, validated_data):
        return Card.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.board_id = validated_data.get('board_id', instance.board_id)
        instance.column_id = validated_data.get('column_id', instance.column_id)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance


class LabelSerializer(serializers.Serializer):
    board_id = serializers.IntegerField()
    title = serializers.CharField()
    color_id = serializers.IntegerField()

    def create(self, validated_data):
        return Label.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.board_id = validated_data.get('board_id', instance.board_id)
        instance.title = validated_data.get('title', instance.title)
        instance.color_id = validated_data.get('color_id', instance.color_id)
        instance.save()
        return instance


class LabelColorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    color = serializers.CharField()

    def create(self, validated_data):
        return LabelColor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.color = validated_data.get('color', instance.color)
        instance.save()
        return instance


class LabelCardSerializer(serializers.Serializer):
    card_id = serializers.IntegerField()
    label_id = serializers.IntegerField()

    def create(self, validated_data):
        return LabelCard.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.card_id = validated_data.get('card_id', instance.card_id)
        instance.label_id = validated_data.get('label_id', instance.label_id)
        instance.save()
        return instance


class CheckListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    board_id = serializers.IntegerField()
    title = serializers.CharField()

    def create(self, validated_data):
        return CheckList.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.board_id = validated_data.get('board_id', instance.board_id)
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance


class CheckListCardSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    card_id = serializers.IntegerField()
    checklist_id = serializers.IntegerField()

    def create(self, validated_data):
        return CheckListCard.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.card_id = validated_data.get('card_id', instance.card_id)
        instance.checklist_id = validated_data.get('checklist_id', instance.checklist_id)
        instance.save()
        return instance


class AttachmentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    board_id = serializers.IntegerField()
    file = serializers.FileField()

    def create(self, validated_data):
        return Attachment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.board_id = validated_data.get('board_id', instance.board_id)
        instance.file = validated_data.get('file', instance.file)
        instance.save()
        return instance


class AttachCardSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    card_id = serializers.IntegerField()
    attachment_id = serializers.IntegerField()

    def create(self, validated_data):
        return AttachmentCard.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.card_id = validated_data.get('card_id', instance.card_id)
        instance.attachment_id = validated_data.get('attachment_id', instance.attachment_id)
        instance.save()
        return instance
