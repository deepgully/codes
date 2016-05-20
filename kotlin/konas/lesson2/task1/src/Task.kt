data class MyDate(val year: Int, val month: Int, val dayOfMonth: Int) : Comparable<MyDate> {
    override fun compareTo(o: MyDate): Int {
        if (year != o.year ) return year - o.year
        if (month != o.month) return month - o.month
        return dayOfMonth - o.dayOfMonth
    }
}

fun compare(date1: MyDate, date2: MyDate) = date1 < date2