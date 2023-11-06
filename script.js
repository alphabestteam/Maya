/*
Your job for today is to finish the starSign function.

Find the astrological sign, given the birth details as a Date object.
Start and end dates for zodiac signs very on different resources, 
so we will use this table to get consistent testable results:

Aquarius ----- 21 January - 19 February
Pisces ----- 20 February - 20 March
Aries ----- 21 March - 20 April
Taurus ----- 21 April - 21 May
Gemini ----- 22 May - 21 June
Cancer ----- 22 June - 22 July
Leo ----- 23 July - 23 August
Virgo ----- 24 August - 23 September
Libra ----- 24 September - 23 October
Scorpio ------ 24 October - 22 November
Sagittarius ----- 23 November - 21 December
Capricon ------ 22 December - 20 January
*/

function starSign(date){
    day_in_month = date.getDate();
    month = date.getMonth(); 
        if ((month == 0 && day_in_month >= 21) || (month == 1 && day_in_month <= 19))
            console.log("Aquarius");
        else if ((month == 1 && day_in_month >= 20) || (month == 2 && day_in_month <= 20))
            console.log("Pisces");
        else if ((month == 2 && day_in_month >= 21) || (month == 3 && day_in_month <= 20))
            console.log("Aries");
        else if ((month == 3 && day_in_month >= 21) || (month == 4 && day_in_month <= 21))
            console.log("Taurus");
        else if ((month == 4 && day_in_month >= 22) || (month == 5 && day_in_month <= 21))
            console.log("Gemini");
        else if ((month == 5 && day_in_month >= 22) || (month == 6 && day_in_month <= 22))
            console.log("Cancer");
        else if ((month == 6 && day_in_month >= 23) || (month == 7 && day_in_month <= 23))
            console.log("Leo");
        else if ((month == 7 && day_in_month >= 24) || (month == 8 && day_in_month <= 23))
            console.log("Virgo");
        else if ((month == 8 && day_in_month >= 24) || (month == 9 && day_in_month <= 23))
            console.log("Libra");
        else if ((month == 9 && day_in_month >= 24) || (month == 10 && day_in_month <= 22))
            console.log("Scorpio");
        else if ((month == 10 && day_in_month >= 23) || (month == 11 && day_in_month <= 21))
            console.log("Sagittarius");
        else
            console.log("Capricorn");
}


const today = new Date();
const random_date = new Date("2021-03-25");
starSign(today);
starSign(random_date);