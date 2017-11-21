from django.db import models


class Eleitor(models.Model):
    nome = models.CharField('nome', max_length=200)
    email = models.EmailField('Email')

    def __str__(self):
        return self.nome


class Eleicao(models.Model):
    quant_vagas = models.FloatField('quantidade')
    candidato = models.ManyToManyField(Eleitor, verbose_name='candidato')

class EleicaoEleitor(models.Model):
    Eleitor = models.ForeignKey('Eleitor')
    Eleicao = models.ForeignKey('Eleicao')
