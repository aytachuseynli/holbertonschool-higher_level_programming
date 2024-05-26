document.addEventListener("DOMContentLoaded", () => {
  const btnTranslate = document.getElementById("btn_translate");
  const helloDiv = document.getElementById("hello");
  const languageCode = document.getElementById("language_code");

  btnTranslate.addEventListener("click", () => {
    const lang = languageCode.value;
    if (lang) {
      fetch(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`)
        .then(response => response.json())
        .then(data => {
          helloDiv.textContent = data.hello;
        })
        .catch(error => {
          console.error('Error fetching the translation:', error);
        });
    } else {
      helloDiv.textContent = 'Please select a language.';
    }
  });
});
