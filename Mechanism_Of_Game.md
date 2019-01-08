#How The Game Works? (Step by Step)
* ## Lobby
  * There are game rooms created by different people and its allowed to create your own room.
  * All rooms have one creator and as long as creator isn't deletes room or moderator deletes room. Room stays alive. Otherwise room is deleted.
  * Game starts as you enter a room or create your own and get ready. (In order to play there should be atleast 4 people in server)
* ## Game Starts
  * One random participant gets selected in the background after that participant gets to choose whether to kill one person (himself included) silently (This is just meaning that other people doesnt see who the choosen one fires at) or publicly (Just shooting in front of everyone)
  * After the choice action happens as game lets you choose one person, and if gun doesnt fail (Which has a chance but we can decide later on numbers) other participant dies and switches to spectator mode (which is just watching from the eyes of choosen one as game advances)
  * Spectators cannot chat
  * Players who enter after round started has to watch that round as spectator.
  * If a participants connection to game is lost. Participant dies and exits room.
  * Last two survivors get points equally.
  * Points get bigger as player count increases.
##Note
Choosing random players can work like this:
Round 1
a b c d e f   ->  arrayofPeopleThatAreNotShootedYet={a,b,c,d,e,f}
a shoots f
Round 2
a b c d e     ->  arrayofPeopleThatAreNotShootedYet={b,c,d,e}
c shoots e but fails
Round 3
a b c d e     ->  arrayofPeopleThatAreNotShootedYet={b,d,e}
d shoots e
Round 4
a b c d       ->  arrayofPeopleThatAreNotShootedYet={b,d}
b shoots d
Round 5
a b c         ->  arrayofPeopleThatAreNotShootedYet={} so then new arrayofPeopleThatAreNotShootedYet=people that are living={a,b,c}
a shoots c    ->  arrayofPeopleThatAreNotShootedYet={b}
people that are alive == 2 so game over
Final
a and b gets points
