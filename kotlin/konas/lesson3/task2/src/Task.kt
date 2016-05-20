// Return the set of cities the customers are from
fun Shop.getCitiesCustomersAreFrom(): Set<City> = this.customers.map{it.city}.toSet()

// Return a list of the customers who live in the given city
fun Shop.getCustomersFrom(city: City): List<Customer> = this.customers.filter {it.city==city}.toList()