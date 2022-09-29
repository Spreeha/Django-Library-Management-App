from django.db import models

class Buyers(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  dob=models.DateField(null=True)
  mobile= models.CharField(max_length=200,null=True)
  email= models.CharField(max_length=200,null=True)
  address= models.CharField(max_length=2000,null=True)
  def __str__(self):
        return self.firstname 


class Sellers(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  dob=models.DateField(null=True)
  mobile= models.CharField(max_length=200,null=True)
  email= models.CharField(max_length=200,null=True)
  address= models.CharField(max_length=2000,null=True)
  def __str__(self):
        return self.firstname


class Books(models.Model):
    bookID = models.IntegerField(null=True)
    bookname = models.CharField(max_length=255)
    bookauthor = models.CharField(max_length=255)
    price = models.IntegerField(null=True)
    seller_name = models.ForeignKey(Sellers, on_delete=models.CASCADE)
    def __str__(self):
        return self.bookname 


class Checkout(models.Model):
    bookID = models.IntegerField(null=True)
    bookname = models.CharField(max_length=255)
    bookauthor = models.CharField(max_length=255)
    price = models.IntegerField(null=True)
    buyer_name = models.CharField(max_length=255)
    #seller_name = models.ForeignKey(Sellers, on_delete=models.CASCADE)
    def __str__(self):
        return self.bookname 
