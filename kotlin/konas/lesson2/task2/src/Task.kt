class DateRange(val start: MyDate, val endInclusive: MyDate) {
    operator fun contains(d: MyDate):Boolean {
        return d >= start && d <= endInclusive
    }
}

fun checkInRange(date: MyDate, first: MyDate, last: MyDate): Boolean {
    return date in DateRange(first, last)
}