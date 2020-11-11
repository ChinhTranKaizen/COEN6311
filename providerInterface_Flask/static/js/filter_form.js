document.addEventListener("DOMContentLoaded", function(){
    let KmDrivenMin = document.querySelector("#KmDrivenMin");
    let KmDrivenMax = document.querySelector("#KmDrivenMax");
    //Input form constraint for input value
    KmDrivenMax.onfocusout = function(){
        if( KmDrivenMin.value ==""||KmDrivenMin.value == null){
            KmDrivenMin.max.value = KmDrivenMax.value
        }
        else if (KmDrivenMax.value <= KmDrivenMin.value) {
            alert("The max value cannot be smaller than the min value")
            KmDrivenMax.value = ""
        }
    };

    
})