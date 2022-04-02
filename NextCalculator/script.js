const all = document.querySelectorAll("[data-thing]")
const input = document.getElementById("inp")
const submit = document.querySelector("[data-submit]")
const clear = document.querySelector("[data-clear]")

let str = ""

all.forEach(element => {
  element.addEventListener("click", () => {
    str += element.innerHTML
    input.value = str
    submit.addEventListener("click", () => {
      input.value = eval(str)
    })
  })
})

function clearing() {
  input.value = ""
  str = ""
  console.clear()
}

function deleting() {
  str = str.slice(0, str.length-1)
  input.value = str
  console.clear()
}