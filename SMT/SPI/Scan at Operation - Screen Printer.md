## Problem
1. A board goes into SPI, and when it scans the QR code, it says "Scan at operation - Screen Printer"

## Root Cause
1. The QR code did not get scanned at the scanner right before the SPI/after the printer shuttle
	1. The printer is having an issue with MES
	2. An operator pushed the board through before it could scan
	3. The scanner is having trouble reading.

## Solution
1. Scan the QR code under the scanner at PCB loading
	1. Located right after the PCB cleaner after the laser
	2. If that fails, ask IT
2. If operators are pushing them through prematurely, verify everything is alright on MES at screen print and that the boards are scanning alright
3. If the scanner is having issues reading the QR code even when right below it, please see [[Scanner Issues]].