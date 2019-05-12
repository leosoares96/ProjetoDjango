from django.db import models

# Create your models here.

class usuario(models.Model):
    nome = models.CharField("nome", max_length=50)
    email = models.EmailField("email", max_length=50)
    senha = models.CharField("senha", max_length=50)


    def __str__(self):
        return self.nome

class conteudo(models.Model):
    titulo = models.CharField("titulo", max_length=50)
    texto = models.TextField("texto", max_length=50)
    autor = models.CharField("autor", max_length=50)


    def __str__(self):
        return self.titulo

class contato(models.Model):
    nome = models.CharField("nome", max_length=50)
    assunto = models.CharField("assunto", max_length=50)
    conteudo = models.TextField("conteudo", max_length=200)


    def __str__(self):
        return self.nome

