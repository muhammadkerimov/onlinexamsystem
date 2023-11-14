var endtime = new Date('{{examend}}').getTime();

// Set the countdown duration to 1 hour (60 minutes * 60 seconds * 1000 milliseconds)
// Calculate the end time

// Update the countdown every second

var x = setInterval(function() {
    var now = new Date().getTime();
    var distance = endtime - now;
    if (distance <= 0) {
        clearInterval(x);
        alert('Time has run out. Your submitted answers have been recorded.');
        document.getElementById("submitexam").click();
    } else {
        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);

        hours = (hours < 10) ? "0" + hours : hours;
      minutes = (minutes < 10) ? "0" + minutes : minutes;
      seconds = (seconds < 10) ? "0" + seconds : seconds;

        document.getElementById("timer").innerHTML = hours + ":" + minutes + ":" + seconds;

        if (minutes == 9 && seconds == 59) {
            alert('Less than 10 minutes left!');
        }
    }
}, 1000);
