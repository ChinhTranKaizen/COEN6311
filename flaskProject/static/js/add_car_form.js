document.addEventListener("DOMContentLoaded", function(){
    //browser handling of user input for KmDriven field
    let Entrydate = document.querySelector("#EntryDate");
    let Releaseyear = document.querySelector("#ReleaseYear");

    Entrydate.onblur = function(){
        if (Entrydate.value !== "" && Releaseyear.value !== ""){
            year = Entrydate.value.split('-')
            year = year[0]
            if (parseInt(year)<parseInt(Releaseyear.value)) {
                alert("A car's entry date should not be before car's release year");
                Entrydate.value = "";
                Releaseyear.value = "";
            }
        }
    }
    Releaseyear.onblur = function (){
        if (Entrydate.value !== "" && Releaseyear.value !== ""){
            year = Entrydate.value.split('-')
            year = year[0]
            if (parseInt(year)<parseInt(Releaseyear.value)) {
                alert("A car's entry date should not be before car's release year");
                Entrydate.value = "";
                Releaseyear.value = "";
            }
        }
    }
})