document.addEventListener("DOMContentLoaded", function() {
    //Öppettider
    openHoursDict = {
        'måndag': {'open': '10', 'close': '18'},
        'tisdag': {'open': '10', 'close': '18'},
        'onsdag': {'open': '10', 'close': '17'},
        'torsdag': {'open': '10', 'close': '17'},
        'fredag': {'open': '10', 'close': '18'},
        'lördag': {'open': '12', 'close': '16'},
        'söndag': {'open': '12', 'close': '15'},
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
        "31/12",
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
            openHoursText.innerHTML = "Stängt för helgdag, vi öppnar klockan " + openHoursDict[nextDay].open + " på " + nextDay;
            return;
        }

        //Kollar om det är öppet eller stängt
        if (currentTime >= openHoursDict[currentWeekDay].open && currentTime < openHoursDict[currentWeekDay].close) {
            openHoursText.innerHTML = "Vi har just nu öppet!"+" Butiken stänger klockan " + openHoursDict[currentWeekDay].close;
        //Körs om det är stängt och innan öppningstid
        } else if(currentTime < openHoursDict[currentWeekDay].open) {
            openHoursText.innerHTML = "Butiken är stängd men vi öppnar klockan " + openHoursDict[currentWeekDay].open + " idag";
        //Körs om det är stängt och efter stängningstid
        } else {
            openHoursText.innerHTML = "Butiken är stängd men vi öppnar klockan " + openHoursDict[nextDay].open + " på " + nextDay;
        }
    }
    checkOpenHours();
});
