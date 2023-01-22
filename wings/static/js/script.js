/* scripts js */ 
// if no patients show the messages
$(document).ready(function(){
    var verify = $("#chk_td").length;
    if (verify==0){
        $("#no_data").text("No Patients Found Plz Register Patient First")
    }
});


//2) Time running at realtime
//setInterval(function() {
  //  var date=new Date();
   // $("#clock").html (
     //   (date.getHours() < 10 ? '0':'') + date.getHours() + ":" + (date.getMinutes() < 10 ? '0':''+ date.getMinutes() +":"+ (date.getSeconds() < 10 ? '0':'')+date.getSeconds()
       // )
    //})