const  result=document.getElementById("result");
const  input=document.getElementById("input");
const  submitBtn=document.getElementById("submitbtn"); 
const getName=document.getElementById("input-name");

submitBtn.addEventListener(`click`, () => {
    let intAge;

    intAge=input.value;

    if (getName.value !=="" & input.value !==""){

    if (intAge >=18){
        result.textContent=`Hello ${getName.value} you're ${intAge} and you are eligible`;
    }
    if(intAge >65){
        result.textContent=`Hello ${getName.value} you're ${intAge} and you are retired`;
        }
    if (intAge>100){
        result.textContent=`Hello ${getName.value} you're ${intAge} and too old`;
    }
    if(intAge==0){
        result.textContent=`Hello ${getName.value} you're ${intAge} and you are just born`;
    }
     if (intAge<18) {
        result.textContent=`Hello ${getName.value} you're ${intAge} and still young`;
     }
    } else {
        alert("Please provide data")
    }
});