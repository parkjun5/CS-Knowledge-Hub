private var index = 0

private class Animal(val name: String)

private fun recordAnimal(
    animal: Animal
) {
    println("Animal #$index: ${animal.name}"
            index++
}

fun recordAnimals() {
    recordAnimal(Animal("Tiger")
            recordAnimal(Animal("Antelope")
}

fun recordAnimalCount() {
    println("$index animal!")
}


fun main() {
    var a :List<String> = listOf("3" , "2")
    vararg b = arrayOf("1","2")
    recordAnimals()
}