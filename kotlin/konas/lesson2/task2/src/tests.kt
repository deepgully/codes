import org.junit.Assert
import org.junit.Test
import koans.util.inEquals

class TestInRange {
    fun doTest(date: MyDate, first: MyDate, last: MyDate, shouldBeInRange: Boolean) {
        val message = "${date} should${if (shouldBeInRange) "" else "n't"} be in ${DateRange(first, last)}".inEquals()
        Assert.assertEquals(message, shouldBeInRange, checkInRange(date, first, last))
    }

    @Test fun testInRange() {
        doTest(MyDate(2014, 3, 22), MyDate(2014, 1, 1), MyDate(2015, 1, 1), shouldBeInRange = true)
    }

    @Test fun testBefore() {
        doTest(MyDate(2013, 3, 22), MyDate(2014, 1, 1), MyDate(2015, 1, 1), shouldBeInRange = false)
    }

    @Test fun testAfter() {
        doTest(MyDate(2015, 3, 22), MyDate(2014, 1, 1), MyDate(2015, 1, 1), shouldBeInRange = false)
    }
}