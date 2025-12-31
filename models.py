from tortoise.models import Model
from tortoise import fields

class Products(Model):
    id=fields.IntField(pk=True)
    name=fields.CharField(max_length=30, nullable=False)
    quantity_in_stock=fields.IntField(default=0)
    quantity_sold=fields.IntField(default=0)
    unit_price=fields.FloatField(default=0.0,max_digits=8, decimal_places=2)  
    supplied_by=fields.ForeignKeyField('models.Suppliers', related_name='goods_supplied', on_delete=fields.CASCADE) 
    revenue=fields.FloatField(default=0.0, max_digits=20, decimal_places=2) 
    