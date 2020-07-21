from django.db import models




class Pessoa(models.Model):

    idPessoa = models.IntegerField()
    nome = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Card(models.Model):
    
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    data = models.DateField(auto_now=False, auto_now_add=False)
    acidente = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    rua = models.CharField(max_length=50)
    numero = models.IntegerField()
    likes = models.IntegerField()
    deslikes = models.IntegerField()
    

    def __str__(self):
        return self.acidente