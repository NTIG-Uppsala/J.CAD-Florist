openHoursDict = {
    'måndag': {'open': '10', 'close': '18'},
    'tisdag': {'open': '10', 'close': '18'},
    'onsdag': {'open': '10', 'close': '17'},
    'torsdag': {'open': '10', 'close': '17'},
    'fredag': {'open': '10', 'close': '18'},
    'lördag': {'open': '12', 'close': '16'},
    'söndag': {'open': '12', 'close': '15'}
}

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
    let day = date.getDay()
    if (day == 0) { // day = 0 är söndag men i openHoursDict är söndag sista dagen (index 6)
        currentWeekDay = Object.keys(openHoursDict)[6];
    } else { // indexeringen i date.getDay() är 0-6 där 0 är söndag, så vi behöver subtrahera 1 för att få rätt index
        currentWeekDay = Object.keys(openHoursDict)[day - 1];
    }
    const nextWeekDay = Object.keys(openHoursDict)[day];
    
    const openHoursText = document.getElementById("openOrClosed"); //Texten som ska stylas

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
    checkOpenHours(new Date());
});
