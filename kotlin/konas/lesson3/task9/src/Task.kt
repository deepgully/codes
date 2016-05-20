// Return customers who have more undelivered orders than delivered
fun Shop.getCustomersWithMoreUndeliveredOrdersThanDelivered(): Set<Customer> {
    return this.customers.partition {
        it.orders.count({it.isDelivered}) < (it.orders.size + 1) / 2
    }.first.toSet()
}