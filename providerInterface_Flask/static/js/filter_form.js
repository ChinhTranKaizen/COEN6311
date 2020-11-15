
document.addEventListener("DOMContentLoaded", function(){
    //browser handling of user input for KmDriven field
    let KmDrivenMin = document.querySelector("#KmDrivenMin");
    let KmDrivenMax = document.querySelector("#KmDrivenMax");

    KmDrivenMax.onblur = function(){
      let kmMax = (KmDrivenMax.value === "") ? 0 : parseInt(KmDrivenMax.value);
      let kmMin = (KmDrivenMin.value === "") ? 0 : parseInt(KmDrivenMin.value);

      if (kmMax < kmMin) {
        alert("Maximum km cannot be smaller than minimum km for filter");
        KmDrivenMax.value = "";
        KmDrivenMin.value = "";
      };

    };
    KmDrivenMin.onblur = function(){
      let kmMin = (KmDrivenMin.value === "") ? 0 : parseInt(KmDrivenMin.value);
      if (KmDrivenMax.value !== ""){
        let kmMax = (KmDrivenMax.value === "") ? 0 : parseInt(KmDrivenMax.value);
        if (kmMax < kmMin) {
          alert("Maximum km cannot be smaller than minimum km for filter");
          KmDrivenMax.value = "";
          KmDrivenMin.value = "";
        };
      };

    };
    //browser handling of user input for entrydate field

    let EntryDateMin = document.querySelector("#EntryDateMin");
    let EntryDateMax = document.querySelector("#EntryDateMax");

    EntryDateMax.onblur = checkEntryDate;
    EntryDateMin.onblur = checkEntryDate;

    let ReleaseYearMin = document.querySelector("#ReleaseYearMin");
    let ReleaseYearMax = document.querySelector("#ReleaseYearMax");

    ReleaseYearMin.onblur = function (){
      if (ReleaseYearMax.value !== "" && ReleaseYearMin.value !== ""){
        if (ReleaseYearMax.value < ReleaseYearMin.value) {
          alert("Maximum release year cannot be smaller than minimum release year for filter");
          ReleaseYearMax.value = "";
          ReleaseYearMin.value = "";
        }
      }
    }
    ReleaseYearMax.onblur = function (){
      if (ReleaseYearMax.value !== "" && ReleaseYearMin.value !== ""){
        if (ReleaseYearMax.value < ReleaseYearMin.value) {
          alert("Maximum release year cannot be smaller than minimum release year for filter");
          ReleaseYearMax.value = "";
          ReleaseYearMin.value = "";
        }
      }
    }

    let PriceKmMin = document.querySelector("#PriceKmMin");
    let PriceKmMax = document.querySelector("#PriceKmMax");

    PriceKmMin.onblur = function (){
      if (PriceKmMax.value !== "" && PriceKmMin.value !== ""){
        if (PriceKmMax.value < PriceKmMin.value) {
          alert("Maximum price per km cannot be smaller than minimum price per km for filter");
          PriceKmMax.value = "";
          PriceKmMin.value = "";
        }
      }
    }
    PriceKmMax.onblur = function (){
      if (PriceKmMax.value !== "" && PriceKmMin.value !== ""){
        if (PriceKmMax.value < PriceKmMin.value) {
          alert("Maximum price per km cannot be smaller than minimum price per km for filter");
          PriceKmMax.value = "";
          PriceKmMin.value = "";
        }
      }
    }

    let PriceDayMin = document.querySelector("#PriceDayMin");
    let PriceDayMax = document.querySelector("#PriceDayMax");

    PriceDayMin.onblur = function (){
      if (PriceDayMax.value !== "" && PriceDayMin.value !== ""){
        if (PriceDayMax.value < PriceDayMin.value) {
          alert("Maximum price per day cannot be smaller than minimum price per day for filter");
          PriceDayMax.value = "";
          PriceDayMin.value = "";
        }
      }
    }
    PriceDayMax.onblur = function (){
      if (PriceDayMax.value !== "" && PriceDayMin.value !== ""){
        if (PriceDayMax.value < PriceDayMin.value) {
          alert("Maximum price per day cannot be smaller than minimum price per day for filter");
          PriceDayMax.value = "";
          PriceDayMin.value = "";
        }
      }
    }


  })

  // parse a date in yyyy-mm-dd format
  function parseDate(input) {

    let parts = input.split('-');

    // new Date(year, month [, day [, hours[, minutes[, seconds[, ms]]]]])
    return new Date(parts[0], parts[1]-1, parts[2]); // Note: months are 0-based
  }

  function checkEntryDate(){
    let datemax = (EntryDateMax.value !== "") ? parseDate(EntryDateMax.value) : ""
    let datemin = (EntryDateMin.value !== "") ? parseDate(EntryDateMin.value) : ""

    if (datemax != "" && datemin != ""){
      if (datemax < datemin){
        alert("Maximum entry date cannot be smaller than minimum entry date for filter");
        EntryDateMax.value = "";
        EntryDateMin.value = "";
      };
    };
  }
