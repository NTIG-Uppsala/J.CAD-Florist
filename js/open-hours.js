const closedDays = {
    0: [1, 6],
    1: [],
    2: [],
    3: [],
    4: [1],
    5: [6],
    6: [],
    7: [],
    8: [],
    9: [],
    10: [],
    11: [24, 25, 26, 31],
};

const openHours = {
    monday: { index: 1, open: true, from: { hour: 10, minute: 0 }, to: { hour: 18, minute: 0 }, name: "måndag" },
    tuesday: { index: 2, open: true, from: { hour: 10, minute: 0 }, to: { hour: 18, minute: 0 }, name: "tisdag" },
    wednesday: { index: 3, open: true, from: { hour: 10, minute: 0 }, to: { hour: 17, minute: 0 }, name: "onsdag" },
    thursday: { index: 4, open: true, from: { hour: 10, minute: 0 }, to: { hour: 17, minute: 0 }, name: "torsdag" },
    friday: { index: 5, open: true, from: { hour: 10, minute: 0 }, to: { hour: 18, minute: 0 }, name: "fredag" },
    saturday: { index: 6, open: true, from: { hour: 12, minute: 0 }, to: { hour: 16, minute: 0 }, name: "lördag" },
    sunday: { index: 0, open: true, from: { hour: 12, minute: 0 }, to: { hour: 15, minute: 0 }, name: "söndag" },
};

const now = new Date();

const updateCurrentStatus = () => {
    const outputTextField = document.querySelector("#openOrClosed");
    const currentDay = now.getDay();
    const currentDate = now.getDate();
    const currentHour = now.getHours();
    const currentMinute = now.getMinutes();
    const currentMonth = now.getMonth();
    const currentDayObject = openHours[Object.keys(openHours).find((key) => openHours[key].index === currentDay)];

    let tempDate = new Date(now);
    let nextOpenDayObject = currentDayObject;
    let nextOpenDay = currentDay;

    while (
        !nextOpenDayObject.open ||
        closedDays[tempDate.getMonth()].includes(tempDate.getDate()) ||
        (tempDate.getDate() === currentDate && (currentHour > currentDayObject.to.hour || (currentHour === currentDayObject.to.hour && currentMinute >= currentDayObject.to.minute)))
    ) {
        nextOpenDay = (nextOpenDay + 1) % 7;

        tempDate.setDate(tempDate.getDate() + 1);

        nextOpenDayObject = openHours[Object.keys(openHours).find((key) => openHours[key].index === nextOpenDay)];
    }
<<<<<<< HEAD:js/open-hours.js
    const nextWeekDay = Object.keys(openHoursDict)[day];
    
    const openHoursText = document.getElementById("open-or-closed"); //Texten som ska stylas
=======
>>>>>>> df3a7e4 (Funktionell datum- och tidshantering):js/openHours.js

    const nextOpenDayName = nextOpenDayObject.name;
    const nextOpenMinute = nextOpenDayObject.from.minute;
    const nextOpenString = `${nextOpenDayObject.from.hour}:${nextOpenMinute < 10 ? "0" + nextOpenMinute : nextOpenMinute}`;
    const nextCloseMinute = nextOpenDayObject.to.minute;
    const nextCloseString = `${nextOpenDayObject.to.hour}:${nextCloseMinute < 10 ? "0" + nextCloseMinute : nextCloseMinute}`;
    if (closedDays[currentMonth].includes(currentDate)) {
        outputTextField.innerHTML = `Stängt för helgdag, vi öppnar kl ${nextOpenString} på ${nextOpenDayName}`;
        return;
    }
    if (currentHour < currentDayObject.from.hour || (currentHour === currentDayObject.from.hour && currentMinute < currentDayObject.from.minute)) {
        outputTextField.innerHTML = `Stängt, vi öppnar kl ${currentDayObject.from.hour}:${currentDayObject.from.minute < 10 ? "0" + currentDayObject.from.minute : currentDayObject.from.minute} idag`;
        return;
    }

    if (currentHour >= currentDayObject.to.hour || (currentHour === currentDayObject.to.hour && currentMinute >= currentDayObject.to.minute)) {
        outputTextField.innerHTML = `Stängt, vi öppnar kl ${nextOpenString} på ${nextOpenDayName}`;
        return;
    }

    outputTextField.innerHTML = `Öppet, vi stänger kl ${nextCloseString} idag`;
};

updateCurrentStatus();
