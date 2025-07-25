# Creando variables
nombre = "Rodrigo Loyola"
producto = "Pollo a la brasa"
precio = 50.50
cantidad = 2
total = int(precio * cantidad)

# Visualización del cliente
print("\nBuen día {}, el detalle de su compra es el siguiente:"
      "\n- Producto: {}"
      "\n- Precio unitario: {}"
      "\n- Cantidad: {}"
      "\n- Total a pagar: {}".format(nombre, producto, precio, cantidad, total))
