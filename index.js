const button = document.querySelector("[data-sub]")
const input = document.querySelector("[data-input]")

function calculate() {
    const item = String(input.value)
    op = checkForSymbols(item)
    n1 = parseInt(item.slice(0, parseInt(item.indexOf(op))))
    n2 = parseInt(item.slice(parseInt(item.indexOf(op))+1, parseInt(item.length)))
    console.log(n1,op,n2)
    input.value = calculator(n1,op,n2)
}

checkForSymbols = (item) => {
    if (item.includes("+")) {
        return "+"
    } else if (item.includes("-")) {
        return "-"
    } else if (item.includes("*")) {
        return "*"
    } else if (item.includes("**")) {
        return "**"
    } else if (item.includes("/")) {
        return "/"
    } else {
        return null
    }
}

function calculator(n1,op,n2) {
    switch (op) {
        case "+":
            return n1 + n2
        case "-":
            return n1 - n2
        case "*":
            return n1 * n2
        case "/":
            return n1 / n2
        default:
            return null
    }
}

button.addEventListener("click", () => {
    calculate()
})