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



function getTodaysDate(date) {
    const month = date.getMonth();  // 0-11
    const dayOfMonth = date.getDate();
    const todaysDate = `${dayOfMonth}/${month + 1}`;  // lägger till 1 för att månaderna ska räknas som 1-12
    return todaysDate;
}


function checkOpenHours(date) {
    //räknar ut vilken veckodag det är idag och imorgon
    const day = date.getDay()
    const currentWeekDay = Object.keys(openHoursDict)[day - 1];
    const nextWeekDay = Object.keys(openHoursDict)[day];

    //Texten som ska stylas
    const openHoursText = document.getElementById("openOrClosed");

    const nextDayOpenHour = openHoursDict[nextWeekDay].open
    const currentDayOpenHour = openHoursDict[currentWeekDay].open;
    const currentDayCloseHour = openHoursDict[currentWeekDay].close;
    const currentHour = date.getHours();

    if (closedDays.includes(getTodaysDate(date))) {  // helgdag
        openHoursText.innerHTML = "Stängt för helgdag, vi öppnar kl " + nextDayOpenHour + " på " + nextWeekDay;
    } else if (currentHour >= currentDayCloseHour) { // efter stängningstid
        openHoursText.innerHTML = "Stängt, vi öppnar kl " + nextDayOpenHour + " på " + nextWeekDay;
    } else if(currentHour < currentDayOpenHour) {  // innan öppningstid
        openHoursText.innerHTML = "Stängt, vi öppnar kl " + currentDayOpenHour + " idag";
    } else { // öppet
        openHoursText.innerHTML = "Öppet, vi stänger kl " + currentDayCloseHour + " idag";
    }
}

document.addEventListener("DOMContentLoaded", function() {
    //Öppettider
    


    
    checkOpenHours(new Date());
});
