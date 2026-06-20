## Problem:
1. Machine keeps reading that the part is out, when it is not
2. The part isn't picking up

## Root Cause:
1. The nozzle is trying to pick up the part at the wrong spot
2. Can't make/keep a vacuum seal
	1. Usually due to dirty nozzles
	2. The nozzle isn't sliding down fully, leaving a gap between the nozzle tip and the part, preventing part pickup

## Solution:
1. Verify pickup position is consistently centered in the socket/no offset on the module
	1. Step the feeder forward more than once to verify pitch is correct
2. Confirm part width, length and height in MEdit
3. Confirm there are no offsets in MEdit
4. Check nozzles are not clogged
	1. If the nozzle is clogged, unclog it with compressed air or pull a wire from a wire brush
	2. If that doesn't work, soak it in alcohol first. Same principle as cleaning with water pressure than just air pressure
5. Check nozzles are sliding correctly
	1. Take the nozzle nest and spray it with compressed air. The silver shaft inside the nozzles should slide up and down without difficulty as the compressed air moves over it
	2. If not, spray into the hole/nozzle above or below it with the compressed air to force the slider to move up.
	3. If it moves with great difficulty, keep on it until it is up fully, then push it back down with your finger. If done right, it should come back up faster next time, and faster the next until it has no difficulties
6. Verify there are no bent shafts
	1. Pull the module out and power it off by opening the bottom cover
	2. Pull the head off and manually check the shafts at the bottom
7. Verify the head has adequate airflow
	1. Take the head to the head cleaner. Follow the process at [[Head Cleaning]]
	2. If the air flow is under 1.4 L/minute, that shaft is probably dirty. Run an oil cleaning on the head cleaner. Follow the process at [[Head Cleaning]]
8. Verify the head is calibrated correctly
	1. Confirm there are adequate jigs in the nozzle nest to perform calibration
	2. If it succeeds, try again. If it fails, swap the head with a spare.