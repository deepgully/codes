import java.util.*

fun getList(): List<Int> {
    val arrayList = arrayListOf(1, 5, 2)
    Collections.sort(arrayList, object: Comparator<Int> {
        override fun compare(o1:Int, o2:Int):Int {
            return o2 - o1
        }
    })
    return arrayList
}


