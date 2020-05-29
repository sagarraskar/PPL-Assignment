airport_data(toronto,50,60).
airport_data(madrid,75,45).
airport_data(barcelona,40,30).
airport_data(valencia,40,20).
airport_data(malega,50,30).
airport_data(london,75,80).
airport_data(paris,50,60).
airport_data(tolouse,40,30).


dir(toronto,london).
dir(toronto,madrid).
dir(barcelona,london).
dir(barcelona,madrid).
dir(barcelona,valencia).
dir(madrid,valencia).
dir(madrid,malega).
dir(valencia,malega).
dir(paris,tolouse).


route(toronto,london,aircanada,500,360).
route(toronto,london,united,650,420).
route(toronto,madrid,united,950,540).
route(toronto,madrid,iberia,800,480).
route(toronto,madrid,aircanada,900,480).
route(madrid,barcelona,aircanada,100,60).
route(madrid,barcelona,iberia,120,65).
route(barcelona,valencia,iberia,110,75).
route(madrid,malega,iberia,50,60).
route(malega,valencia,iberia,80,120).
route(barcelona,london,iberia,220,240).
route(paris,tolouse,united,35,120).



;rules
routes(X,Y,A,B,C) :- route(Y,X,A,B,C) ; route(X,Y,A,B,C).

flight(X,Y,A,B,C) :- routes(X,Y,A,B,C).
airport(A,B,C) :- airport_data(A,B,C).

check_flight(X,Y) :- routes(X,Y,A,B,C) -> write('Flight is available') ; write('Flight is not available').

cheap_flight(X,Y,A) :- routes(X,Y,A,B,C) , B < 400 -> write('Flight is cheap') ; write('Flight is not cheap').

direct(X,Y) :- dir(Y,X) ; dir(X,Y).
two_flights(X,Y) :- direct(X,Z) ; direct(Z,Y).

preferred(X,Y,A) :- cheap_flight(X,Y,A) ; A == aircanada.

