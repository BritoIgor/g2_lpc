from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from eleicao_api.models import *
from django.conf.urls import url, include

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff')

class EleitorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Eleitor
        fields = ('nome', 'email')
    def create(self, validated_data):
        return Eleitor.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.nome = validated_data.get('nome', instance.nome)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance

class EleicaoSerializer(serializers.HyperlinkedModelSerializer):
    candidato = EleitorSerializer(many=True)
    class Meta:
        model = Eleicao
        fields = ('quant_vagas', 'candidato')
    def create(self, validated_data):
        return Eleicao.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.quant_vagas = validated_data.get('quant_vagas', instance.quant_vagas)
        instance.candidato = validated_data.get('candidato', instance.candidato)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance
