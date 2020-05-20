%Creating a prolog database of a flight network

/*flight(city_name1, city_name2, airline_name, price, duration) -- flight(A,B,C,D,E).*/

flight(toronto, aircanada, madrid,  900, 480).
flight(toronto, united,  madrid, 950, 540).
flight(toronto, iberia, madrid, 800, 480).

flight(toronto, aircanada, london, 500, 360).
flight(toronto, united, london, 650, 420).

flight(madrid, aircanada, barcelona, 100, 60).
flight(madrid, iberia, barcelona, 120, 65).

flight(london, iberia, barcelona, 220, 240).

flight(barcelona, iberia, valencia, 110, 75).

flight(madrid , iberia, valencia, 40, 50).

flight(madrid, iberia, malaga, 50, 60).

flight(malaga, iberia, valencia, 80, 120).

flight(paris, united, toulouse, 35, 120).


/* airport(city,airporttax,minsecuritydelay) ----  airport(X,Y,Z).*/

airport(toronto, 50, 60).
airport(barcelona, 40, 30).
airport(madrid, 75, 45).
airport(valencia, 40, 20).
airport(malaga, 50, 30).
airport(paris, 50, 60).
airport(toulouse, 40, 30).
airport(london, 75, 80).

/*writing Prolog clauses to express the following sentences */


is_flight_from_x_to_y(X, Y) :- flight(X, _, Y, _, _).

is_cheap(A, C, B):-flight(A, C, B, P, _), P < 400.

is_possible_from_x_to_y_intwo_flight(A, B):-flight(A, _,Z, _, _),flight(Z, _, B, _, _). 

is_preferred(A, C, B,P) :-flight(A, C, B, P, _), P < 400; C == aircanada.

is_united_is_aircanada(A, B):-flight(A, united, B, _, _).  /* wrong for paris, toulouse case */

is_flight_through_aircanada_if_through_united(A, B) :- flight(A, united, B, _, _) -> flight(A, aircanada, B, _, _).












