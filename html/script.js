$(".menu").mouseenter(function(){
	$("#welcome").fadeOut("slow");
	$(".menu").stop().animate({width:"8vw"}, 600);
	$(this).stop().animate({width:"82vw"}, 600);
});

function ajax(r) {
 var text = $("#tb").val();
 var voice = $("#voices").val();
 var request = new XMLHttpRequest();
 request.open( "GET" , "ajax.php?v=" + voice + "&r=" + r +"&t=" + text +"&x=" + Math.random(), true);
 request.send(null);
 request.onreadystatechange = function () {
         if (request.readyState == 4 && request.status == 200) {
                console.log("ok");
         }
 }
}

$("#over").click(function(){
 $("#over").fadeOut();
 $( "#photo" ).hide( "puff", 300);
 $("#photob").fadeOut();
});

$("#snap").click(function(){
 $("#photob").append("<img src='http://192.168.0.7:8080/?action=snapshot' id='photo'/>");
 $("#over").fadeIn();
 $("#photob").fadeIn();
 $( "#photo" ).delay(100).show("puff",300);
});

$("#over2").fadeIn();

$("#man").click(function(){
 $("#man").fadeOut();
 $("#auto").fadeIn();
 $("#over2").fadeOut();
});

$("#auto").click(function(){
 $("#auto").fadeOut();
 $("#man").fadeIn();
 $("#over2").fadeIn();
});
