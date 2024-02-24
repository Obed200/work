const subscribeBtn = document.querySelector(".btn2");
const emailContent = document.querySelector(".email-content");

subscribeBtn.addEventListener("click", () => {
    if (emailContent.value !== "") {
        alert(`${emailContent.value} is subscribed to our platform sucessfully`);
        emailContent.value = "";
    } else {
        alert("Please provide your email address");
    }
})