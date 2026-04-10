## Problem
1. A board goes into SPI, and when it scans the QR code, it says "Serial Number Generation Not Allowed"

## Root Cause
1. The board is not registered in MES
	1. 1. The QR code did not get scanned at the scanner right before the SPI/after the printer shuttle
		1. An operator pushed the board through before it could scan
		2. The scanner is having trouble reading.

## Solution
1. Scan the QR code under the scanner at PCB loading
	1. Right after the PCB cleaner after the laser
	2. If that fails, ask IT
2. If the scanner is having issues reading the QR code even when right below it, please see [[Scanner Issues]].