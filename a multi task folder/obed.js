
let count=0;
document.querySelector('.decrease').onclick=function(){
count-=1;
document.querySelector('.label').innerHTML=count;
}
document.querySelector('.increase').onclick=function(){
    count+=1;
    document.querySelector('.label').innerHTML=count;
    }