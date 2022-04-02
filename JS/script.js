const button = document.querySelector("[data-sub]")
const input = document.querySelector("[data-input]")

button.addEventListener("click", () => {
    input.value = eval(input.value)
})