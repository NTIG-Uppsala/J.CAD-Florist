// List of closed days
// month: [days]
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

// Object with opening hours for each day
// day: { index: number, open: boolean, from: { hour: number, minute: number }, to: { hour: number, minute: number }, name: string }
const openHours = {
    monday: { index: 1, open: true, from: { hour: 10, minute: 0 }, to: { hour: 18, minute: 0 }, name: "måndag" },
    tuesday: { index: 2, open: true, from: { hour: 10, minute: 0 }, to: { hour: 18, minute: 0 }, name: "tisdag" },
    wednesday: { index: 3, open: true, from: { hour: 10, minute: 0 }, to: { hour: 17, minute: 0 }, name: "onsdag" },
    thursday: { index: 4, open: true, from: { hour: 10, minute: 0 }, to: { hour: 17, minute: 0 }, name: "torsdag" },
    friday: { index: 5, open: true, from: { hour: 10, minute: 0 }, to: { hour: 18, minute: 0 }, name: "fredag" },
    saturday: { index: 6, open: true, from: { hour: 12, minute: 0 }, to: { hour: 16, minute: 0 }, name: "lördag" },
    sunday: { index: 0, open: true, from: { hour: 12, minute: 0 }, to: { hour: 15, minute: 0 }, name: "söndag" },
};

// Get the current date and time
const now = new Date();

// Function to update the text field with the current status
const updateCurrentStatus = () => {
    // Get the output text field
    const outputTextField = document.querySelector("#open-or-closed");

    // Get the current day, date, hour, minute, month and the opening hours for the current day
    const currentDay = now.getDay();
    const currentDate = now.getDate();
    const currentHour = now.getHours();
    const currentMinute = now.getMinutes();
    const currentMonth = now.getMonth();
    const currentDayObject = openHours[Object.keys(openHours).find((key) => openHours[key].index === currentDay)];

    // Create a new date object
    let tempDate = new Date(now);
    let nextOpenDayObject = currentDayObject;
    let nextOpenDay = currentDay;

    // Loop through the days until we find the next open day
    while (
        !nextOpenDayObject.open ||
        closedDays[tempDate.getMonth()].includes(tempDate.getDate()) ||
        (tempDate.getDate() === currentDate && (currentHour > currentDayObject.to.hour || (currentHour === currentDayObject.to.hour && currentMinute >= currentDayObject.to.minute)))
    ) {
        nextOpenDay = (nextOpenDay + 1) % 7;

        tempDate.setDate(tempDate.getDate() + 1);

        nextOpenDayObject = openHours[Object.keys(openHours).find((key) => openHours[key].index === nextOpenDay)];
    }

    // Get the name of the next open day, the opening time and the closing time
    const nextOpenDayName = nextOpenDayObject.name;
    const nextOpenMinute = nextOpenDayObject.from.minute;
    const nextOpenString = `${nextOpenDayObject.from.hour}:${nextOpenMinute < 10 ? "0" + nextOpenMinute : nextOpenMinute}`;
    const nextCloseMinute = nextOpenDayObject.to.minute;
    const nextCloseString = `${nextOpenDayObject.to.hour}:${nextCloseMinute < 10 ? "0" + nextCloseMinute : nextCloseMinute}`;

    // Check if the store is closed for a holiday
    if (closedDays[currentMonth].includes(currentDate)) {
        outputTextField.innerHTML = `Idag har vi stängt p.g.a helgdag. Vi öppnar kl. ${nextOpenString} på ${nextOpenDayName}`;
        return;
    }

    // Check if the store has not opened for the day yet
    if (currentHour < currentDayObject.from.hour || (currentHour === currentDayObject.from.hour && currentMinute < currentDayObject.from.minute)) {
        outputTextField.innerHTML = `Vi har stängt. Vi öppnar kl. ${currentDayObject.from.hour}:${currentDayObject.from.minute < 10 ? "0" + currentDayObject.from.minute : currentDayObject.from.minute} idag`;
        return;
    }

    // Check if the store has closed for the day
    if (currentHour >= currentDayObject.to.hour || (currentHour === currentDayObject.to.hour && currentMinute >= currentDayObject.to.minute)) {
        outputTextField.innerHTML = `Vi har stängt. Vi öppnar kl. ${nextOpenString} på ${nextOpenDayName}`;
        return;
    }

    // The store is open
    outputTextField.innerHTML = `Vi har öppet. Vi stänger kl. ${nextCloseString} idag`;
};

// Update the current status
updateCurrentStatus();
