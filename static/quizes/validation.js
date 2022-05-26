function numberValidation() {
  var n = document.myForm.num.value;
  console.log(n);
  if (isNaN(n)) {
    document.getElementById("numberText").innerHTML =
      "Please enter Numeric value";
    return false;
  } else {
    return true;
  }
}

const input = document.querySelector(".telefon");
const valid = document.getElementById("validation");

input.addEventListener("input", updateValue);

function updateValue(e) {
  if (!isNaN(e.target.value)) {
    valid.innerHTML = `Sanlar durıs kirtilgenin tekserip barıń`;
    if ((valid.classList.contains = "red")) {
      valid.classList.remove("red");
      valid.classList.add("succes");
    } else {
      valid.classList.add("succes");
    }
  } else {
    valid.classList.add("red");
    valid.innerHTML = `Iltimas tek ǵana sanlardı kiritiń`;
    if ((valid.classList.contains = "succes")) {
      valid.classList.add("red");
      valid.classList.remove("succes");
    } else {
      valid.classList.add("red");
    }
  }
}