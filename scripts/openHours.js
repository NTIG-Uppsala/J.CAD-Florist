document.addEventListener("DOMContentLoaded", function() {
    //Öppettider
    openHoursDict = {
        'Måndag': {'open': '10', 'close': '18'},
        'Tisdag': {'open': '10', 'close': '18'},
        'Onsdag': {'open': '10', 'close': '17'},
        'Torsdag': {'open': '10', 'close': '17'},
        'Fredag': {'open': '10', 'close': '18'},
        'Lördag': {'open': '12', 'close': '16'},
        'Söndag': {'open': '12', 'close': '15'}
    }

    //Stängda dagar
    closedDays = [
        "1/1",
        "6/1",
        "1/5",
        "6/6",
        "24/12",
        "25/12",
        "26/12",
        "31/12"
    ]
    //Får dagens datum
    const date = new Date();
    const month = date.getMonth();
    const dayOfMonth = date.getDate();
    const todaysDate = `${dayOfMonth}/${month + 1}`;

    //Får dag och tid
    const day = new Date().getDay();
    const currentTime = new Date().getHours();
    //Får dagens veckodag
    currentWeekDay = Object.keys(openHoursDict)[day - 1];
    //Får nästa veckodag
    nextDay = Object.keys(openHoursDict)[day];
    //Texten som ska stylas
    const openHoursText = document.getElementById("openOrClosed");


    function checkOpenHours() {
        //Kollar om det är en stängd dag
        if (closedDays.includes(todaysDate)) {
            console.log("Stängt för helgdag");
            console.log("Vi öppnar kl", openHoursDict[nextDay].open, "på", nextDay);
            openHoursText.innerHTML = "Stängt för helgdag, vi öppnar kl " + openHoursDict[nextDay].open + " på " + nextDay;
            return;
        }

        //Kollar om det är öppet eller stängt
        if (currentTime >= openHoursDict[currentWeekDay].open && currentTime < openHoursDict[currentWeekDay].close) {
            console.log("Öppet", currentTime, "vi stänger kl", openHoursDict[currentWeekDay].close);
            openHoursText.innerHTML = "Öppet, vi stänger kl " + openHoursDict[currentWeekDay].close;
        //Körs om det är stängt och innan öppningstid
        } else if(currentTime < openHoursDict[currentWeekDay].open) {
            console.log("Stängt, vi öppnar kl", openHoursDict[currentWeekDay].open, " idag");
            openHoursText.innerHTML = "Stängt, vi öppnar kl " + openHoursDict[currentWeekDay].open + " idag";
        //Körs om det är stängt och efter stängningstid
        } else {
            console.log();
            console.log("Stängt, vi öppnar kl", openHoursDict[nextDay].open, "på", nextDay);
            openHoursText.innerHTML = "Stängt, vi öppnar kl " + openHoursDict[nextDay].open + " på " + nextDay;
        }
    }
    checkOpenHours();
});
