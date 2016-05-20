// Return all products this customer has ordered
fun Customer.getOrderedProducts(): Set<Product> = this.orders.flatMap { it.products }.toSet()

// Return all products that were ordered by at least one customer
fun Shop.getAllOrderedProducts(): Set<Product> = this.customers.flatMap { it.orders.flatMap { it.products } }.toSet()