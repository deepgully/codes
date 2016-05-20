fun renderProductTable(): String {
    return html {
        table {
            tr (color=getTitleColor()){
                this.td {
                    text("Product")
                }
                td {
                    text("Price")
                }
                td {
                    text("Popularity")
                }
            }
            val products = getProducts()
            products.forEachIndexed {
                i, product ->
                tr {
                    for (j in 0..2) {
                        td(color = getCellColor(i, j)) {
                            text(
                            when (j) {
                                0 -> product.toString()
                                1 -> "${product.price}"
                                2 -> "${product.popularity}"
                                else -> ""
                            })
                        }
                    }
                }
            }

        }
    }.toString()
}

fun getTitleColor() = "#b9c9fe"
fun getCellColor(index: Int, row: Int) = if ((index + row) %2 == 0) "#dce4ff" else "#eff2ff"