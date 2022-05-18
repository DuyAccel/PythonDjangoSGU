const input = document.querySelectorAll(".form-qualtity-details input");
const btnUp = document.querySelectorAll(".quantity-btn-up");
const btnDown = document.querySelectorAll(".quantity-btn-down");


for(let i =0 ; i < btnUp.length;i++)
{
    btnUp[i].addEventListener("click",()=>{
        input[i].value++;
    })
    btnDown[i].addEventListener("click",()=>{
        input[i].value--;
        if(input[i].value <= 0 )
        {
            input[i].value =1;
        }
    })
}

const deliveryBox = document.querySelectorAll(".delivery-box");
const deliveryboxcheck = document.querySelectorAll(".delivery-box-check");
const deliveryboxdetals = document.querySelectorAll(".delivery-box-details");

for(let i = 0 ; i< deliveryBox.length; i++)
{
    deliveryboxcheck[i].addEventListener("click",()=>{
        activeAllBox(i);
    })
    deliveryboxdetals[i].addEventListener("click",()=>{
        activeAllBox(i);
    })
}

const test = document.querySelector(".delivery-price").innerHTML;

const activeAllBox = (i) =>{
    for(let i = 0 ; i< deliveryBox.length; i++)
    {
        deliveryBox[i].classList.remove("active");
    }
    deliveryBox[i].classList.add("active");

}  


const changeBtn = document.querySelector(".content-info-change h4");
const contentInfo = document.querySelector(".content-info");
const contentAddress = document.querySelector(".content-address");
const CancelBtn = document.querySelector(".address-remove");

changeBtn.addEventListener("click",()=>{
    contentAddress.classList.add("active");
    contentInfo.classList.add("hidden");
})


CancelBtn.addEventListener("click",()=>{
    contentAddress.classList.remove("active");
    contentInfo.classList.remove("hidden");



})
