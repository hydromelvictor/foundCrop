"""_summary_

Returns:
    _type_: _description_
"""
from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from .constant import CATEGORIES, COUNTRY, SEXE, STATUS


class User(AbstractUser):
    address = models.CharField(max_length=132, default='')
    picture = models.ImageField(upload_to='media', blank=True)
    country = models.CharField(max_length=132, choices=COUNTRY)
    state = models.CharField(max_length=16, default='')
    sexe = models.CharField(max_length=1, choices=SEXE, default='')
    status = models.CharField(max_length=132, choices=STATUS)

    def __str__(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        return self.username
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Client(User):
    is_client = models.BooleanField(default=True)

    def __str__(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        return "{}:{}".format(self.status, self.username)
    
    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'


class Professional(User):
    is_prof = models.BooleanField(default=True)

    def __str__(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        return "{}:{}".format(self.status, self.username)
    
    class Meta:
        verbose_name = 'Professional'
        verbose_name_plural = 'Professionals'


class Product(models.Model):
    professional = models.ForeignKey(User, related_name='products', on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    picture = models.ImageField(upload_to='media', blank=True)
    category = models.CharField(choices=CATEGORIES, max_length=50)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    
    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.name

    def get_absolute_url(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return reverse('productUpdate', kwargs={'prd_id': self.pk})
    
    def get_absolute_del_url(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return reverse('productDel', kwargs={'prd_id': self.pk})

    def get_absolute_add_url(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return reverse('add_to_cart', kwargs={'prd_id': self.pk})


class Card(models.Model):
    user = models.ForeignKey(User, related_name='cards', on_delete=models.PROTECT)
    zip_code = models.CharField(max_length=16)
    card_name = models.CharField(max_length=16)
    card_number = models.CharField(max_length=32)
    expiration = models.DateField(default=datetime.today)
    cvv = models.CharField(verbose_name='CVV', max_length=32)

    def __str__(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        return "MasterCard:{}".format(self.user)
    
    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'


class Command(models.Model):
    card = models.ForeignKey(Card, related_name='commands', on_delete=models.PROTECT)
    total = models.DecimalField(max_digits=50, decimal_places=2)
    # pour savoir sur quel commande ajouter le produits
    valid = models.BooleanField(default=True)
    # pour savoir si la command est payer
    pay = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Command'
        verbose_name_plural = 'Commands'

    def __str__(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        return "{}-{}".format('Command', self.card.user.username)

    @property
    def total(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        total = 0
        details = Detail.objects.filter(active=True)
        for detail in details:
            total += detail.total()
        return round(total, 2)


class Detail(models.Model):
    product = models.ForeignKey(Product, related_name='details', on_delete=models.PROTECT)
    cmd = models.ForeignKey(Command, related_name='details', on_delete=models.PROTECT)
    count = models.IntegerField()
    # pour ne pas ajouter des produits d'ancien facture
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        return "{}:{}:{}".format(self.cmd, self.product, self.count)

    @property
    def total(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return round(self.product.price * self.count, 2)
    
    def get_absolute_url(self):
        """_summary_
        
        Returns:
            _type_: _description_
        """
        return reverse('Update_to_cart', kwargs={'detail_id': self.pk})
    
    class Meta:
        verbose_name = 'Detail'
        verbose_name_plural = 'Details'
