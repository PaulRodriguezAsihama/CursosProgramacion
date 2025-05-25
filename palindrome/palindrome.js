// Add UI elements dynamically
const appContainer = document.createElement("div");
appContainer.innerHTML = `
  <input id="text-input" type="text" />
  <button id="check-btn">Check</button>
  <div id="result"></div>
`;
document.body.appendChild(appContainer);

const textInput = document.getElementById("text-input");
const checkBtn = document.getElementById("check-btn");
const resultDiv = document.getElementById("result");

const isPalindrome = (str) => {
  const cleaned = str.replace(/[^A-Za-z0-9]/g, "").toLowerCase();
  return cleaned === cleaned.split("").reverse().join("");
};

checkBtn.addEventListener("click", () => {
  const value = textInput.value;
  if (!value) {
    alert("Please input a value.");
    return;
  }
  const palindrome = isPalindrome(value);
  resultDiv.textContent = `${value} is${
    palindrome ? "" : " not"
  } a palindrome.`;
});
