# Attribute Description Table

| Variable        | Type        | Description                   |
|:----------------|:------------|:------------------------------|
| IsCanceled      | Categorical | Indicator if customer canceled booking or not   |
| LeadTime        | Integer | Number of days between arrival date and the date the booking was made  |
| ArrivalDateYear | Integer   | Year  |
| ArrivalDateMonth| Categorical | Month   |
| ArrivalDateWeekNumber | Integer | Week number of the year |
| ArrivalDateDayOfMonth | Integer | Day  |
| StaysInWeekendNights | Integer | Number of weekend nights stayed or booked to stay |
| StaysInWeekNights | Integer | Number of weekday nights stayed or booked to stay |
| Adults | Integer | Number of adults |
| Children | Integer | Number of children |
| Babies |  Integer | Number of babies |
| Meal | Categorical | Indicator if a meal package was booked or not |
| IsRepeatedGuest | Categorical | Indicator if booking name was from a repeated guest or not |
| PreviousCancellations | Integer | Number of bookings the customer canceled prior to the current booking |
| PreviousBookingsNotCanceled | Integer | Number of bookings the customer did not cancel prior to the current booking |
| BookingChanges | Integer | Number of changes made to the booking |
| Agent | Categorical | Indicator if the booking was made with  agent |
| Company | Categorical | Indicator if a company made or paid for the booking |
| DaysInWaitingList | Integer | Number of days the booking was on the waiting list |
| ADR | Real | Average Daily Rate |
| RequiredCarParkingSpaces | Integer | Number of parking spaces customer required. |
| TotalOfSpecialRequests | Integer | Number of special requests made by the customer |
| Corporate | Categorical | Indicator if the booking was made by a company |
| Direct | Categorical | Indicator if the booking was made directly through the hotel |
| GDS<sup>1</sup> | Categorical | Indicator if booking was made through a Global Distribution System |
| TA/TO | Categorical | Indicator if the booking was made through a travel agent or tour operator |
| Deposit | Categorical | Indicator if the customer made a deposit or not |
| RoomTypeDifference | Categorical | Indicator if the customer received a different room than the one reserved |
| Contract | Categorical | Indicator if the type of booking has a contract associated to it  |
| Group | Categorical | Indicator if booking is associated with a group |
| Transient | Categorical | Indicator if booking is not associated with a group or contract and not with another transient booking|
| Transient-Party | Categorical | Indicator if booking is transient and associated with at least another transient booking |

<sup>1</sup>`GDS` only appears in H2.