const entryInput = document.querySelector('.content-form__textarea');
const errorMessage = document.querySelector(
  '.form__textarea ~ .form-error__message'
);

const re = /^\b.{20,}\b/;

function validateTextarea() {
    if (errorMessage) {
      entryInputValue = entryInput.value;
      if (!re.test(entryInputValue)) {
        entryInput.classList.add('invalid-textarea');
        errorMessage.style.display = 'inline'
      } else {
        entryInput.classList.remove('invalid-textarea');
        errorMessage.style.display = 'none'
      }
    }
}

validateTextarea()

entryInput.addEventListener("input", validateTextarea)