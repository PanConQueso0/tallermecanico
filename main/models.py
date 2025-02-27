from django.db import models

# Create your models here.
class Estado(models.Model):
    idEstado = models.AutoField(primary_key=True, verbose_name="Codigo estado")
    nombreEstado = models.CharField(max_length=30, verbose_name="Nombre estado")


class TipoRecibo(models.Model):
    idTipoRecibo = models.AutoField(primary_key=True, verbose_name="Codigo tipo recibo")
    nombreTipoRecibo = models.CharField(
        max_length=30, verbose_name="Nombre tipo recibo"
    )


class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True, verbose_name="Codigo usuario")
    nombreUsuario = models.CharField(max_length=30, verbose_name="Nombre usuario")
    contraseniaUsuario = models.CharField(
        max_length=30, verbose_name="Contraseña usuario"
    )


class Empleado(models.Model):
    idEmpleado = models.AutoField(primary_key=True, verbose_name="Codigo empleado")
    nombresEmpleado = models.CharField(max_length=30, verbose_name="Nombre empleado")
    rutEmpleado = models.CharField(max_length=30, verbose_name="Rut empleado")
    idUsuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)


class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True, verbose_name="Codigo cliente")
    nombresCliente = models.CharField(max_length=30, verbose_name="Nombre cliente")
    rutCliente = models.CharField(max_length=30, verbose_name="Rut cliente")
    domicilioCliente = models.CharField(max_length=85, verbose_name="Domicilio cliente")
    idUsuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)


class Proveedor(models.Model):
    idProveedor = models.AutoField(primary_key=True, verbose_name="Codigo proveedor")
    nombresProveedor = models.CharField(max_length=30, verbose_name="Nombre proveedor")
    rutProveedor = models.CharField(max_length=30, verbose_name="Rut proveedor")
    domicilioProveedor = models.CharField(
        max_length=85, verbose_name="Domicilio proveedor"
    )
    fonoProveedor = models.CharField(max_length=85, verbose_name="Fono proveedor")

    rubroProveedor = models.CharField(max_length=85, verbose_name="Rubro Proveedor")


class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True, verbose_name="Codigo producto")
    nombreProducto = models.CharField(max_length=30, verbose_name="Nombre producto")
    stockProducto = models.IntegerField(verbose_name="Codigo producto")
    idProveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True)


class Servicio(models.Model):
    idServicio = models.AutoField(primary_key=True, verbose_name="Codigo cliente")
    nombresServicio = models.CharField(max_length=30, verbose_name="Nombre cliente")
    idProducto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    idEstado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True)

class Recibo():
    idRecibo = models.AutoField(primary_key=True, verbose_name="Codigo recibo")
    fechaRecibo = models.DateField(verbose_name="Fecha del Recibo")
    totalRecibo = models.IntegerField(verbose_name="Valor Total")
    idTipoRecibo = models.ForeignKey(TipoRecibo, on_delete=models.SET_NULL, null=True)

class Pedido():
    idPedido = models.AutoField(primary_key=True, verbose_name="Codigo pedido")
    fechaPedido = models.DateField(verbose_name="Fecha del Pedido")
    fechaEntrega = models.DateField(null=True, verbose_name="Fecha de Entrega")
    valorPedido = models.IntegerField(verbose_name="Valor del Pedido")
    idEstado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True)
    idProveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True)
    idRecibo = models.ForeignKey(Recibo, on_delete=models.SET_NULL, null=True)

class Servicio_Cliente():
    idSolicitud = models.AutoField(primary_key=True, verbose_name="Codigo Solicitud Servicio")
    fechaSolicitud = models.DateField(verbose_name="Fecha de la Solicitud")
    horaReserva = models.TimeField(verbose_name="Hora de la Reserva")
    idCliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    idServicio = models.ForeignKey(Servicio, on_delete=models.SET_NULL, null=True)
    idEstado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True)
    idRecibo = models.ForeignKey(Recibo, on_delete=models.SET_NULL, null=True)

