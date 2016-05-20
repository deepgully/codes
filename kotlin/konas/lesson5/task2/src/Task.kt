import java.util.HashMap

fun buildMap(init: MutableMap<Int, String>.() -> Unit): Map<Int, String> {
    val m = HashMap<Int, String>()
    m.init()
    return m
}

fun usage(): Map<Int, String> {
    return buildMap {
        put(0, "0")
        for (i in 1..10) {
            put(i, "$i")
        }
    }
}