from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class BaseModelo(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    criado_em = models.DateField(auto_now_add=True)
    atualizado_em = models.DateField(auto_now_add=True)
    
    class Meta:
        abstract = True
        
class Facilidades(BaseModelo):
    facilidade_nome = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.facilidade_nome

class Hotel(BaseModelo):
    hotel_nome= models.CharField(max_length=100)
    hotel_preco = models.IntegerField()
    descricao = models.TextField()
    facilidades = models.ManyToManyField(Facilidades)
    qtd_quartos = models.IntegerField(default=10)

    def __str__(self) -> str:
        return self.hotel_nome
    
class HotelImagem(BaseModelo):
    hotel= models.ForeignKey(Hotel ,related_name="imagens", on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to="hotels")
    
class HotelReserva(BaseModelo):
    hotel= models.ForeignKey(Hotel  , related_name="hotel_reserva" , 
                             on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="usuario_reserva" ,
                             on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    tipo_de_reserva= models.CharField(max_length=100,
                                      choices=(('Pre Pagamento' , 'Pre Pagamento') ,
                                               ('Pos Pagamento' , 'Pos Pagamento')))
    
    def __str__(self):
        return 'Hotel: '+str(self.hotel)+' para cliente: '+str(self.user.username)