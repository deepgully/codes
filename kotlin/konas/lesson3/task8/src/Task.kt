// Return a map of the customers living in each city
fun Shop.groupCustomersByCity(): Map<City, List<Customer>> = this.customers.groupBy { it.city }