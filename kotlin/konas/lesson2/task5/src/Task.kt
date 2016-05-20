import TimeInterval.*

data class MyDate(val year: Int, val month: Int, val dayOfMonth: Int)

enum class TimeInterval { DAY, WEEK, YEAR }

data class MulTimeInterval(val ti:TimeInterval, val n:Int)

operator fun TimeInterval.times(n:Int): MulTimeInterval = MulTimeInterval(this, n)

operator fun MyDate.plus(ti: TimeInterval): MyDate = this.addTimeIntervals(ti, 1)

operator fun MyDate.plus(mt: MulTimeInterval): MyDate = this.addTimeIntervals(mt.ti, mt.n)


fun task1(today: MyDate): MyDate {
    return today + YEAR + WEEK
}

fun task2(today: MyDate): MyDate = today + YEAR * 2 + WEEK * 3 + DAY * 5
