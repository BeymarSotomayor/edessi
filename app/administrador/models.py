#administrador/models.py
#app.administrador.models
from decimal import ROUND_HALF_UP, Decimal
from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from datetime import datetime, time
# -------- Empresa --------

# -------- Categorías --------
class Category(models.Model):
    name = models.CharField("Nombre",max_length=100)

    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:  # Solo genera slug si no existe
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField("Nombre",max_length=100)
    detail = models.TextField("Detalle",blank=True, null=True)
    img_background = models.ImageField("Imagen Fondo",upload_to="img_productos", blank=True, null=True)
    img_name = models.ImageField("Imagen Nombre",upload_to="img_productos_name", blank=True, null=True)
    price = models.DecimalField("Precio",max_digits=10, decimal_places=2, blank=True, null=True)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="products")

    def __str__(self):
        return self.name

class Company(models.Model):
    logo_img = models.ImageField("Logo de la Empresa", upload_to="img_empresa", blank=True, null=True)
    name_company = models.CharField("Nombre de la Empresa", max_length=150)
    phone_company = models.CharField("Teléfono", max_length=20, blank=True, null=True)
    address = models.CharField("Dirección", max_length=255, blank=True, null=True)
    #location = models.CharField("Ubicación",max_length=255,blank=True,null=True)
    nit = models.IntegerField("NIT", blank=True, null=True)
    email = models.EmailField("Correo", max_length=150, blank=True, null=True)

    def __str__(self):
        return self.name_company

# -------- Clientes --------
class Client(models.Model):
    name = models.CharField("Nombre",max_length=100)
    last_name = models.CharField("Apellidos",max_length=100, blank=True, null=True)
    email = models.EmailField("Correo",max_length=150, blank=True, null=True)
    phone = models.CharField("Teléfono",max_length=20, blank=True, null=True)
    
    class Meta:
            constraints = [
                models.UniqueConstraint(fields=['name', 'last_name'], name='unique_client_name_lastname')
            ]

    def __str__(self):
        return f"{self.name} {self.last_name or ''}".strip()
    
class Service(models.Model):
    name = models.CharField("Nombre del servicio", max_length=150, unique=True)
    price = models.DecimalField(
        "Precio",
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    def __str__(self):
        return f"{self.name} - {self.price} Bs."
# -------- Accesorios --------

class Accessory(models.Model):
    name = models.CharField("Nombre", max_length=100, unique=True)

    def __str__(self):
        return self.name


# -------- Máquinas --------
class Machine(models.Model):
    STATUS_CHOICES = (
        #('Recibido', 'Recibido'),
        #('En Revisión', 'En Revisión'),
        #('Diagnóstico', 'Diagnóstico'),
        ('Reparación', 'Reparación'),
        #('Pausado', 'Pausado'),
        ('Cancelado', 'Cancelado'),
        #('En proceso', 'En proceso'),
        #('Terminado', 'Terminado'),
        ('Por Entregar', 'Por Entregar'),
        ('Entregado', 'Entregado'),
    )
    BRAND_CHOICES = (
        ('EPSON', 'EPSON'),
        ('brother', 'brother'),
        ('APPLE', 'APPLE'),
        ('LENOVO', 'LENOVO'),
        ('DELL', 'DELL'),
        ('HP', 'HP'),
        ('ASUS', 'ASUS'),
        ('ACER', 'ACER'),
        ('MICROSOFT', 'MICROSOFT'),
        ('SAMSUNG', 'SAMSUNG'),
        ('MSI', 'MSI'),
        ('TOSHIBA', 'TOSHIBA'),
        ('HUAWEI', 'HUAWEI'),
        ('SONY', 'SONY'),
        ('OTHER', 'Otra (escribir)'),  # opción personalizada
    )
    
    POSITION_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
        (11, 11),
        (12, 12),
    )

    ticket = models.IntegerField("Ficha")#,editable=False)
    img_machine = models.ImageField("Imagen de Evidencia de la Máquina",upload_to="img_maquinas", blank=True, null=True)
    brand = models.CharField("Marca",max_length=100, blank=True, null=True, choices=BRAND_CHOICES)
    services = models.ManyToManyField("Service", related_name="machines", blank=True)
    model = models.CharField("Modelo",max_length=100, blank=True, null=True)
    detail = models.CharField("Detalle",max_length=100, blank=True, null=True)
    problem = models.TextField("Detalle",blank=True, null=True)
    diagnostic = models.TextField("Detalle",blank=True, null=True)
    #position = models.IntegerField("Posición", blank=True, null=True, choices=POSITION_CHOICES)
    position = models.IntegerField("Posición", blank=True, null=True)
    accessories = models.TextField("Accesorios",blank=True, null=True)
    status = models.CharField("Estado",max_length=50, null=True, choices=STATUS_CHOICES,default="Recibido")

    price_aprox = models.DecimalField("Precio",max_digits=10,decimal_places=2,blank=True,null=True,validators=[MinValueValidator(0)],default=0)
    price_extra = models.DecimalField("Extra",max_digits=10,decimal_places=2,blank=True,null=True,validators=[MinValueValidator(0)],default=0)
    price_descuento = models.DecimalField("Descuento",max_digits=10,decimal_places=2,blank=True,null=True,validators=[MinValueValidator(0)],default=0)
    price_fact = models.BooleanField("¿Incluir IVA?", default=True)

    price = models.DecimalField("Total",max_digits=10,decimal_places=2,blank=True,null=True,validators=[MinValueValidator(0)],default=0)
    
    saldo = models.DecimalField("Saldo",max_digits=10,decimal_places=2,blank=True,null=True,validators=[MinValueValidator(0)],default=0)
    devolucion = models.DecimalField("Devolución",max_digits=10,decimal_places=2,blank=True,null=True,validators=[MinValueValidator(0)],default=0)
    price_a_cuenta = models.DecimalField("Precio a Cuenta",max_digits=10,decimal_places=2,blank=True,null=True,validators=[MinValueValidator(0)],default=0)


    created_at = models.DateTimeField("fecha de Recepción",auto_now_add=True)
    delivery_in = models.DateTimeField("fecha de Entrega",blank=True, null=True)

    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True, related_name="clients")

    def assign_position(self):
        """Asigna automáticamente una posición según la marca y la lógica de ocupamiento."""
        for pos in range(1, 25):  # posiciones de 1 a 12
            occupied = Machine.objects.filter(
                position=pos
            ).exclude(status="Entregado")
            if occupied.filter(brand__in=["EPSON", "brother"]).exists():
            # Si yo también soy EPSON o brother, solo permito si la posición está vacía
                if self.brand in ["EPSON", "brother"] and not occupied.exists():
                    return pos
                continue  # saltar esta posición porque está bloqueada

            if self.brand in ["EPSON", "brother"]:
                if not occupied.exists():  # posición libre
                    return pos
            else:
                if occupied.count() < 3:  # puede haber hasta 2
                    return pos

        # Si llegamos aquí, no hay posiciones disponibles
        raise ValidationError("No hay posiciones disponibles en el almacén.")
    



    def save(self, *args, **kwargs):
        if not self.pk:
            today = timezone.localdate()  # siempre local
            start = timezone.make_aware(datetime.combine(today, time.min))
            end = timezone.make_aware(datetime.combine(today, time.max))
            
            count_today = Machine.objects.filter(
                created_at__range=(start, end)
            ).count()
            
            self.ticket = count_today + 1

        """ if not self.pk:
            # Usamos la hora local del servidor para asegurar el conteo del ticket del día actual
            today = timezone.localtime(timezone.now()).date()
            count_today = Machine.objects.filter(created_at__date=today).count()
            self.ticket = count_today + 1 """
        
    
        if self.status == "Entregado":
            self.position = None
        
        else:
            # Si no tiene posición asignada → buscar una libre
            if not self.position:
                self.position = self.assign_position()
        
        
        
        # --- 💰 LÓGICA DE PRECIO ---
        base_price = (
            (self.price_aprox or Decimal(0)) +
            (self.price_extra or Decimal(0)) -
            (self.price_descuento or Decimal(0))
        )

        if self.price_fact:
            iva_factor = Decimal('1') + (Decimal('16') / Decimal('84'))
            total = base_price * iva_factor
        else:
            total = base_price

        # 🔹 Redondear a 2 decimales
        total = total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

        # Evitar negativos
        if total < 0:
            total = Decimal('0.00')

        self.price = total

        # --- 💵 CÁLCULO DE SALDO ---
        price_a_cuenta = self.price_a_cuenta or Decimal(0)
        saldo = total - price_a_cuenta

        # Redondear saldo
        saldo = saldo.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

        # Si el saldo es negativo → hay devolución
        if saldo < 0:
            self.devolucion = abs(saldo).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            self.saldo = Decimal('0.00')
        else:
            self.devolucion = Decimal('0.00')
            self.saldo = saldo.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        #self.full_clean()  # llama a clean() antes de guardar
        super().save(*args, **kwargs)

    # def __str__(self):
    #     return f"Machine {self.ticket} - {self.model}"
    def __str__(self):
        return f"Machine {self.ticket} - {self.model} (Pos: {self.position})"
    
    # 🔹 Señal para recalcular precio al cambiar servicios
@receiver(m2m_changed, sender=Machine.services.through)
def update_machine_price(sender, instance, action, **kwargs):
    if action in ["post_add", "post_remove", "post_clear"]:
        total = sum(service.price for service in instance.services.all())
        if instance.price_aprox != total:
            instance.price_aprox = total
            instance.save(update_fields=[
                "price_aprox",
                "price", 
                "saldo", 
            ])


