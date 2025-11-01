 // Set the offer end time (yyyy-mm-ddThh:mm:ss format)
  var countDownDate = new Date("2025-07-10T23:59:59").getTime();

  var x = setInterval(function () {
    var now = new Date().getTime();
    var distance = countDownDate - now;

    if (distance < 0) {
      clearInterval(x);
      document.getElementById("countdown").innerHTML = "🎉 Offer Expired!";
      return;
    }

    var days = Math.floor(distance / (1000 * 60 * 60 * 24));
    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);

    document.getElementById("countdown").innerHTML =
      days + "d " + hours + "h " + minutes + "m " + seconds + "s ";
  }, 1000);

// visit for popup message
   document.addEventListener("DOMContentLoaded", function () {
    // Check if the user has visited before
    if (!localStorage.getItem("visited")) {
      // Show popup
      alert("👋 Welcome to Dax's Ice Cream World!");

      // Set the flag
      localStorage.setItem("visited", "true");
    }
  });