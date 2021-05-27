/*fun main() {
    println("Off to Mars")
} */

//top level variables
/*val name: String="Monk"
var greeting: String="Hello"

fun main() {
    //mutable and local variables

    //val name: String="Monk"

    // name= " "
    println(greeting)
    println(name)

    greeting = "hi"
    print(greeting)
    println(name)
} */

/*val name = "Jupiter"
var greeting: String? = null

fun main() {
    if (greeting != null) {
        println(greeting)
    } else {
        println("Hi")
    }
    println(name)
}  */

//when statement

/*
val name = "Jupiter"
var greeting: String? = null

fun main() {
    when (greeting) {
        null -> println("Hi")
        else -> println(greeting)

    }
    println(name)
} */

//if statement
/*
val name = "Jupiter"
var greeting: String? = null

fun main() {
    val greetingToPrint = if(greeting!=null) greeting
        else
            "Sup"
    println(greetingToPrint)
    println(name)
}  */

//Basic functions
 /*
fun getGreeting(): String {
    return "Sup Marians"
}

fun sayHi() {
    println(getGreeting())
}

fun main() {
    println("Off to Mars")
    println(getGreeting())
    sayHi()
}  */

// Defining function parameters

/*
fun sayHello(itemToGreet:String){
    val msg = "Hello " + itemToGreet
    println(msg)
}


fun main() {
    sayHello( " Elon")
    sayHello( " Musk")
} */

fun sayHello(greeting:String, itemToGreet:String) = println("$greeting $itemToGreet")

fun main() {
    val interestingThings = arrayOf("Kotlin", "Programming", "Developer" )
    println(interestingThings.size)
    println(interestingThings[0])
    println(interestingThings.get(1))

    for (interestingThing in interestingThings){
        println(interestingThing)
    }
}


