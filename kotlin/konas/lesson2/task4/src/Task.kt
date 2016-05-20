class DateRange(var start: MyDate, val end: MyDate):Iterable<MyDate> {
    override fun iterator(): Iterator<MyDate> = object: Iterator<MyDate> {
        override fun hasNext():Boolean {
            return start <= end
        }
        override fun next(): MyDate {
            val res = start
            start = start.nextDay()
            return res
        }
    }
}

fun iterateOverDateRange(firstDate: MyDate, secondDate: MyDate, handler: (MyDate) -> Unit) {
    for (date in firstDate..secondDate) {
        handler(date)
    }
}