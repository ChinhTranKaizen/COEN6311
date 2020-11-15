document.addEventListener("DOMContentLoaded", function(){
    document.querySelector(".delete_btn").onclick = verify_delete;
    document.querySelector("#test_js").onclick = name;
})
function name(){
    alert("something for testin js")
}
function verify_delete() {
    const form = document.querySelector("#delete_form");
    let carID = form.dataset.carID;
    let entryDate = form.dataset.entrydate;
    let kmDriven = form.dataset.kmdriven;
    let releaseYear = form.dataset.releaseyear;
    let condition = form.dataset.condition;
    let priceKm = form.dataset.pricekm;

    let carstr = carID +" - "+ entryDate+" - "+kmDriven +" - "+releaseYear +" - "+condition+" - "+priceKm
    
    alert(carstr)
    
    //let answer = confirm('Are you sure you want to delete this car: '+carstr+'?')
    // if (confirm('Are you sure you want to delete this car: '+carstr+'?')) {
    //     // delete the car
    //     document.querySelector("#delete_form").submit();
    //   } else {

    //   }
    //alert(answer)
}