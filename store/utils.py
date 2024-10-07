from store.models import Customer, Order, Product, OrderProduct


class CartForUser:
    def __init__(self,request,product_id=None,action=None):
        self.user = request.user

        if product_id and action:
            self.add_or_delete(product_id,action)

    def get_cart_info(self):
        customer,created = Customer.objects.get_or_create(
            user=self.user,
            name=self.user.username,
            email=self.user.email,
        )
        order,created = Order.objects.get_or_create(
            customer=customer
        )

        order_products = order.orderproduct_set.all()
        cart_total_price = order.get_cart_total_price
        cart_total_quantity = order.get_cart_total_quantity

        return {
            "products":order_products,
            "order":order,
            "cart_total_price":cart_total_price,
            "cart_total_quantity":cart_total_quantity
        }
    def add_or_delete(self,product_id,action):
        order = self.get_cart_info()['order']
        product = Product.objects.get(pk=product_id)
        order_product,created = OrderProduct.objects.get_or_create(order=order,product=product)

        if action == "add" and product.quantity > 0:
            order_product.quantity += 1
            product.quantity -= 1
        else:
            order_product.quantity -= 1
            product.quantity += 1

        order_product.save()
        product.save()


        if order_product.quantity <= 0:
            order_product.delete()

def get_cart_data(request):
    if request.user.is_authenticated:
        user_cart = CartForUser(request)
        cart_info = user_cart.get_cart_info()
    return {
        "products":cart_info["products"],
        "order":cart_info["order"],
        "cart_total_price":cart_info["cart_total_price"],
        "cart_total_quantity":cart_info["cart_total_quantity"],
    }